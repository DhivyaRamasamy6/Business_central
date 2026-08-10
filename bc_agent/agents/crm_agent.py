from agent_framework import Agent
from config.settings import foundry_client
from prompts.crm_instructions import instructions

agent = Agent(
    name="Business Central Agent",
    client=foundry_client,
    instructions=instructions,
)


