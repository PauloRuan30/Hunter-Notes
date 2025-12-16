from agno.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.models.ollama import Ollama
from agno.tools.duckduckgo import DuckDuckGoTools
from dotenv import load_dotenv
from schemas.monster_info import MonsterName, MonsterNameList, MonsterInfoList
load_dotenv()

agent = Agent(
    model=OpenRouter(
        id="openai/gpt-oss-120b:free",
    ),
    tools=[DuckDuckGoTools()],
    input_schema=MonsterNameList,
    output_schema=MonsterInfoList,
    markdown=True,
    reasoning=True,
    debug_mode=True,
    debug_level=2
)

monsters = MonsterNameList(names=[MonsterName(name="Alatreon"), MonsterName(name="Rathalos")])
response = agent.run(monsters)
print(response.content)