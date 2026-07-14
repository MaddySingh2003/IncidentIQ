from app.core.database import db
collection=db.incidents

class IncidentRepository:

    @staticmethod
    async def create(doucment):
        result = await collection.insert_one(doucment)
        return result.inserted_id
    
    @staticmethod
    async def find_all():
        return collection.find()
    
    @staticmethod
    async def find_by_id(id):
        from bson import ObjectId
        return await collection.find_one({"_id": ObjectId(id)})
    