from agent_framework import MCPStdioTool
import os

def create_business_central_mcp() -> MCPStdioTool:
    return MCPStdioTool(
        name="business-central",
        command="python",
        args=[
            r"C:\Users\Dhivya\Documents\MAF_Tools\bc_agent\business_central_tool\app\integrations\business_central\main.py"
        ],
         env={
            **os.environ,          
            "BC_TENANT_ID":     os.environ["BC_TENANT_ID"],
            "BC_CLIENT_ID":     os.environ["BC_CLIENT_ID"],
            "BC_CLIENT_SECRET": os.environ["BC_CLIENT_SECRET"],
            "BC_COMPANY_ID":    os.environ["BC_COMPANY_ID"],
        },
    )