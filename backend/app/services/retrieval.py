from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.models import SchemaEmbedding
from app.services.embedding import embed_text

async def retrieve_relevant_tables(session: AsyncSession, question: str, top_k: int = 5) -> list[SchemaEmbedding]:
    query_vector = embed_text(question)

    stmt = (
        select(SchemaEmbedding)
        .order_by(SchemaEmbedding.embedding.cosine_distance(query_vector))
        .limit(top_k)
    )
    result = await session.execute(stmt)
    return result.scalars().all()   


