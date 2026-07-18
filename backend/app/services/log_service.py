from app.repositories.log_repository import LogRepository
from datetime import datetime


class LogService:
    @staticmethod
    async def get_logs(incident_id):

      return await LogRepository.get_logs(incident_id)
    @staticmethod
    async def save_logs(incident_id,paresd_logs):

        documents=[]
        
        for log in paresd_logs:
            documents.append({
                "incident_id":incident_id,
                "timestamp":log["timestamp"],
                "level":log["level"],
                "service":log["service"],
                "message":log["message"],

                "raw_log":
                f'{log["timestamp"]} {log["level"]} {log["service"]} {log["message"]}',
                "normalized_log":log["message"].lower(),
                "created_at":datetime.utcnow()

            })
        ids=await LogRepository.insert_many(documents)
        return len(ids)
    