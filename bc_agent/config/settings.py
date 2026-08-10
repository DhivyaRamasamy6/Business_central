import os
from agent_framework_foundry import FoundryChatClient
from azure.identity import ClientSecretCredential
from dotenv import load_dotenv 
load_dotenv()

credential = ClientSecretCredential(
    tenant_id=os.environ["AZURE_TENANT_ID"],
    client_id=os.environ["AZURE_CLIENT_ID"],
    client_secret=os.environ["AZURE_CLIENT_SECRET"],
)

#Foundry
foundry_client=FoundryChatClient(
    project_endpoint=os.getenv("FOUNDRY_PROJECT_ENDPOINT"),
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    credential=credential,
)