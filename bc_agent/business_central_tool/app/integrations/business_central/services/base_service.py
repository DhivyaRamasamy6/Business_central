from typing import Any

from ..client.business_central_client import BusinessCentralClient


class BaseBusinessCentralService:
    """
    Base service for Business Central resources.

    Provides access to the shared BusinessCentralClient.
    """

    def __init__(
        self,
        client: BusinessCentralClient,
    ) -> None:
        self.client = client

    @staticmethod
    def extract_value(
        response: dict[str, Any],
    ) -> list[dict[str, Any]]:

        return response.get("value", [])