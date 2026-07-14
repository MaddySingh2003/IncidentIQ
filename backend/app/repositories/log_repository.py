from app.core.database import db
log_collection = db["logs"]

class LogRepository:
    @staticmethod
    async def insert_many(logs):
        result = await log_collection.insert_many(logs)
        return result.inserted_ids
    