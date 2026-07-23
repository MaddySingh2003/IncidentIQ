from collections import Counter
from app.repositories.log_repository import LogRepository




class AnalyticsService:
    @staticmethod
    async def get_incident_analytics(incident_id):
        logs = await LogRepository.get_log_by_incidents(incident_id)

        if not logs:
            return {"message":"No logs found for the given incident ID."}
        

        level_counter=Counter()
        service_counter=Counter()


        timestamps=[]

        for log in logs:

            level_counter[log["level"]]+=1
            service_counter[log["service"]]+=1
            timestamps.append(log["timestamp"])

        return {
            "total_logs":len(logs),
            "error_logs":level_counter["ERROR"],
            "warn_count":level_counter["WARN"],
            "info_count":level_counter["INFO"],

            "service":dict(service_counter),

            "top_service":service_counter.most_common(1)[0][0],

            "first_log":min(timestamps),
            "last_log":max(timestamps)
            
        }