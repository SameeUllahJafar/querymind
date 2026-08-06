from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.services.retrieval import retrieve_relevant_tables
from app.services.schema_embedding import generate_sql

router = APIRouter()

class QueryRequest(BaseModel):
    question: str


@router.post("/query")
async def query_database(request: QueryRequest, db: AsyncSession = Depends(get_db)) -> dict[str, str]:
    tables = await retrieve_relevant_tables(db, request.question)
    sql= generate_sql(request.question, tables)
    return {"sql": sql}

