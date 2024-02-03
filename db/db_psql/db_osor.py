import asyncpg

class Database:
    def __init__(self, dsn):
        self.dsn = dsn
        self.pool = None

    async def connect(self):
        try:
            self.pool = await asyncpg.create_pool(self.dsn)
            print('База подключена')
        except Exception as e:
            print(f"Ошибка при подключении к базе данных: {e}")

    async def close(self):
        try:
            await self.pool.close()
        except Exception as e:
            print(f"Ошибка при закрытии соединения с базой данных: {e}")

    async def execute(self, query, *args):
        async with self.pool.acquire() as connection:
            return await connection.execute(query, *args)

    async def fetch(self, query, *args):
        async with self.pool.acquire() as connection:
            return await connection.fetch(query, *args)
