from app.repositories.log_repository import LogRepository

class LogService:
    @staticmethod
    async def save_logs(logs):
        
        return await LogRepository.insert_many(logs)