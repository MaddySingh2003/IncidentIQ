from datetime import datetime
from bson import ObjectId

from app.core.database import db


class IncidentService:

    collection = db.incidents

    @classmethod
    async def create_incident(cls, incident):

        document = incident.model_dump()

        document["status"] = "Open"
        document["created_at"] = datetime.utcnow()

        result = await cls.collection.insert_one(document)

        document["id"] = str(result.inserted_id)
        if "_id" in document:
            document.pop("_id")


        return document

    @classmethod
    async def get_all_incidents(cls):

        incidents = []

        async for incident in cls.collection.find():

            incident["id"] = str(incident["_id"])
            incident.pop("_id")

            incidents.append(incident)

        return incidents

    @classmethod
    async def get_incident(cls, incident_id):

        incident = await cls.collection.find_one(
            {"_id": ObjectId(incident_id)}
        )

        if incident is None:
            return None

        incident["id"] = str(incident["_id"])
        incident.pop("_id")

        return incident