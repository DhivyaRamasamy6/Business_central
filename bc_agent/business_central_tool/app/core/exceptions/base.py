class BusinessCentralError(Exception):
    """Base exception for the Business Central SDK."""

    def __init__(
        self,
        message: str,
        *,
        status_code: int | None = None,
        correlation_id: str | None = None,
    ) -> None:
        super().__init__(message)

        self.message = message
        self.status_code = status_code
        self.correlation_id = correlation_id