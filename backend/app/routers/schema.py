from fastapi import APIRouter,Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.services.schema_introspection import get_schema

router = APIRouter()

@router.get("/schema")
async def get_database_schema(db: AsyncSession = Depends(get_db)) -> list[dict]:
    """Get the database schema."""
    conn = await db.connection()
    return await get_schema(conn)
