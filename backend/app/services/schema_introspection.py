from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import AsyncConnection

def _reflect_schema(sync_conn)-> list[dict]:
    inspector = inspect(sync_conn)
    tables = []

    for table_name in inspector.get_table_names(schema="public"):
        columns=[
            {
                "name": col["name"],
                "type": str(col["type"]),
                "nullable": col["nullable"],
            }
            for col in inspector.get_columns(table_name, schema="public")

        ]
        primary_key = inspector.get_pk_constraint(table_name, schema="public")
        foreign_key= inspector.get_foreign_keys(table_name, schema="public")


        tables.append(
            {
                "name": table_name,
                "columns": columns,
                "primary_key": primary_key["constrained_columns"],
                "foreign_keys": [
                    {
                        "columns": fk["constrained_columns"],
                        "referred_to_table": fk["referred_table"],
                        "referred_to_columns": fk["referred_columns"],
                    }
                    for fk in foreign_key
                ],
            }
        )

    return tables

async def get_schema(conn:AsyncConnection) -> list[dict]:
    """Get the database schema."""
    return await conn.run_sync(_reflect_schema)
    