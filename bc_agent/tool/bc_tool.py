from agent_framework import MCPStdioTool


def create_business_central_mcp() -> MCPStdioTool:
    return MCPStdioTool(
        name="business-central",
        command="python",
        args=[
            r"C:\Users\Converse\Documents\Business_central\bc_agent\business_central_tool\app\integrations\business_central\main.py"
        ],
    )