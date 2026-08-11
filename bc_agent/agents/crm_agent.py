from agent_framework import Agent
from config.settings import foundry_client
from prompts.crm_instructions import instructions
from tool.bc_tool import create_business_central_mcp

business_central_mcp = create_business_central_mcp()

agent = Agent(
    name="Business Central Agent",
    client=foundry_client,
    instructions=instructions,
    tools=[business_central_mcp],
)


