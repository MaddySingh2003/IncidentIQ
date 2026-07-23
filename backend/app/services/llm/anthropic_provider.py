import os
from app.services.llm.base import BaseLLMProvider
from dotenv import load_dotenv

load_dotenv()

from anthropic import Anthropic

class AnthropicProvider(BaseLLMProvider):
    def __init__(self):
        self.client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    
    async def generate(self, prompt: str):
        response = self.client.messages.create(
            model="claude-3-5-sonnet-latest",
            max_tokens=1200,
            temperature=0.2,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.content[0].text