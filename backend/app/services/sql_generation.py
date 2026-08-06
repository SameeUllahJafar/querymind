from google import genai
from google.genai import types
from pydantic import BaseModel

from app.config import settings
from app.models import SchemaEmbedding

client = genai.Client(api_key=settings.gemini_api_key)

class sqlGeneration(BaseModel):
    query: str

def generate_sql(question: str, tables: list[SchemaEmbedding]) -> str:
    schema_context = "\n\n".join(table.description for table in tables)

    prompt = (
        "You are a SQL assistant. Given the database schema below and a question, "
        "write a single read-only PostgreSQL SELECT query that answers the question. "
        "Only use the tables and columns shown. Do not use INSERT, UPDATE, DELETE, "
        "DROP, or any other statement that modifies data.\n\n"
        f"Schema:\n{schema_context}\n\n"
        f"Question: {question}"
    )

    response = client.models.generate_content(
        model=settings.gemini_model,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_json_schema=SqlGeneration.model_json_schema(),
        ),
    )

    result = SqlGeneration.model_validate_json(response.text)
    return result.sql