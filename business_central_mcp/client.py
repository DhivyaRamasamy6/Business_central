import requests
import os
from auth import BusinessCentralAuth
from dotenv import load_dotenv
from logger import get_logger
logger=get_logger(__name__)
load_dotenv()

TENANT_ID = os.getenv("DYNAMICS_TENANT_ID")
ENVIRONMENT = os.getenv("ENVIRONMENT")
BASE_URL = os.getenv("BASE_URL")

class BusinessCentralClient:
    def __init__(self):
        self.auth = BusinessCentralAuth()

    def headers(self):
        return {
            "Authorization": f"Bearer {self.auth.get_access_token()}",
            "Accept": "application/json",
        }

    # def get(self, endpoint):
    #     url = f"{BASE_URL}/v2.0/{TENANT_ID}/{ENVIRONMENT}/api/v2.0/{endpoint}"
    #     response = requests.get(url, headers=self.headers())
    #     response.raise_for_status()
    #     return response.json()


    def get(self, endpoint):
        url = f"{BASE_URL}/v2.0/{TENANT_ID}/{ENVIRONMENT}/api/v2.0/{endpoint}"

        logger.info("Calling URL: %s", url)

        try:
            response = requests.get(
                url,
                headers=self.headers(),
                timeout=30,
            )

            logger.info("Status Code: %s", response.status_code)

            response.raise_for_status()

            data = response.json()

            logger.info("Success. Response keys: %s", list(data.keys()))

            return data

        except Exception:
            logger.exception("Business Central API call failed")
            raise
