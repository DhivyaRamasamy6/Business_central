from httpx import Response

from business_central_tool.app.core.exceptions import (
    AuthenticationError,
    AuthorizationError,
    BadRequestError,
    BusinessCentralAPIError,
    ResourceNotFoundError,
)


class ResponseValidator:

    @staticmethod
    def validate(response: Response):

        status = response.status_code

        if status == 200:
            return

        if status == 201:
            return

        if status == 204:
            return

        if status == 400:
            raise BadRequestError(response.text)

        if status == 401:
            raise AuthenticationError(response.text)

        if status == 403:
            raise AuthorizationError(response.text)

        if status == 404:
            raise ResourceNotFoundError(response.text)

        raise BusinessCentralAPIError(response.text)