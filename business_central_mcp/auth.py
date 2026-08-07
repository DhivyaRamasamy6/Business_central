from azure.identity import ClientSecretCredential
import os
from dotenv import load_dotenv
load_dotenv()

TENANT_ID=os.getenv("DYNAMICS_TENANT_ID")
CLIENT_ID=os.getenv("DYNAMICS_CLIENT_ID")
CLIENT_SECRET=os.getenv("DYNAMICS_CLIENT_SECRET")
SCOPE=os.getenv("SCOPE")
class BusinessCentralAuth:

    def __init__(self):

        self.credential = ClientSecretCredential(
            tenant_id=TENANT_ID,
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
        )

    def get_access_token(self):

        token = self.credential.get_token(
            SCOPE
        )

        return token.token
if __name__=="__main__":
    bc=BusinessCentralAuth(
        
    )
    print(bc.get_access_token())