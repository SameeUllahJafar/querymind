
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import SchemaEmbedding
from app.services.embedding import embed_text



def _describe_table(table: dict) -> str:
    column_descriptions = ", ".join(
        f"{col['name']} ({col['type']})" for col in table["columns"]
    )
    lines = [
        f"Table: {table['name']}",
        f"Columns: {column_descriptions}",
        f"Primary key: {', '.join(table['primary_key'])}",
    ]
    for fk in table["foreign_keys"]:
        lines.append(
            f"Foreign key: {', '.join(fk['columns'])} references "
            f"{fk['referred_to_table']}({', '.join(fk['referred_to_columns'])})"
        )
    return "\n".join(lines)


async def embed_schema(session: AsyncSession, tables: list[dict]) -> None:
    await session.execute(delete(SchemaEmbedding))

    for table in tables:
        description = _describe_table(table)
        vector = embed_text(description)
        session.add(
            SchemaEmbedding(
                table_name=table["name"],
                description=description,
                embedding=vector,
            )
        )

    await session.commit()