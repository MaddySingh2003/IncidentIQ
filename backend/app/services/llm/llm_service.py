from app.services.analytics_service import AnalyticsService
from app.repositories.log_repository import LogRepository
from app.services.clustering_service import ClusteringService
from app.services.prompt_builder import build_prompt

from app.services.llm.anthropic_provider import AnthropicProvider

class LLMService:

    provider=AnthropicProvider()

    @classmethod

    async def analyze(cls,incident_id):

        analytics=await AnalyticsService.get_incident_analytics(incident_id)

        logs=await LogRepository.get_log_by_incidents(incident_id)

        clusters=ClusteringService.cluster(logs)

        prompt=build_prompt(analytics,clusters)

        answer=await cls.provider.generate(prompt)

        return {
            "analytics":analytics,
            "clusters":clusters,
            "answer":answer
        }
    
