from pydantic import HttpUrl
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.ollama import OllamaProvider

from src.core.factory import SingletonMeta
from src.core.format import serialize


class AgentClient(metaclass=SingletonMeta):
    _initialized: bool = False
    _agent: Agent

    def __init__(self, llm_base_url: HttpUrl) -> None:
        if self._initialized:
            return
        config = {
            "model_name": "getrobi/lexa-1.5b",
            "provider": OllamaProvider(base_url=serialize(llm_base_url))
        }
        model = OpenAIChatModel(**config)
        self._agent: Agent = Agent(
            model=model,
            system_prompt="Answer concisely.",
        )
        self._initialized = True

    async def run(self, prompt: str) -> str:
        result = await self._agent.run(
            user_prompt=prompt
        )
        return result.output
