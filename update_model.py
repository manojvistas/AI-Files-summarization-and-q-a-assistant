import asyncio
from open_notebook.database.repository import db_connection

async def update_model_name():
    async with db_connection() as client:
        await client.query("UPDATE model SET name = 'gemini-2.5-flash' WHERE name = 'gemini-1.5-flash'")
        print("Model name updated successfully.")

if __name__ == "__main__":
    asyncio.run(update_model_name())
