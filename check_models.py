import asyncio
from open_notebook.database.repository import db_connection

async def get_models():
    async with db_connection() as client:
        models = await client.select('model')
        print("--- Models ---")
        for model in models:
            print(model)
        
        defaults = await client.select('default_models')
        print("\n--- Default Models ---")
        for default in defaults:
            print(default)

if __name__ == "__main__":
    asyncio.run(get_models())
