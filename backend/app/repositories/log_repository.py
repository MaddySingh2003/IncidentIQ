from app.core.database import db

class LogRepository:
    
    collection=db.logs


    @classmethod
    async def insert_many(cls, logs):
        result=await cls.collection.insert_many(logs)
        return result.inserted_ids
    
    @classmethod
    async def get_logs(cls,incidient_id):
        logs=[]

        async for log in cls.collection.find({"incident_id":incidient_id}):
            log["id"]=str(log["_id"])
            log.pop("_id")
            logs.append(log)
        return logs