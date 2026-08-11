import uuid

from app.core.logging import setup_logger

logger = setup_logger(__name__)


class LoggingMiddleware:

    @staticmethod
    def before_request(
        method: str,
        url: str,
    ) -> str:

        correlation_id = str(uuid.uuid4())

        logger.info(
            f"[{correlation_id}] {method} {url}"
        )

        return correlation_id

    @staticmethod
    def after_response(
        correlation_id: str,
        status: int,
    ):

        logger.info(
            f"[{correlation_id}] Response {status}"
        )