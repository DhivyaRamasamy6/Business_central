from datetime import datetime, timedelta, timezone

from business_central_tool.app.core.exceptions import AuthenticationError
from business_central_tool.app.core.http import HTTPClient

from .credential_provider import CredentialProvider
from .oauth_models import OAuthToken, TokenResponse
from .token_manager import TokenManager


class AuthenticationService:
    """
    Handles Business Central OAuth 2.0
    Client Credentials authentication.

    Responsibilities:
    - Retrieve cached tokens.
    - Generate new tokens when required.
    - Refresh tokens before expiry.
    - Prevent concurrent token generation.
    - Force token refresh after HTTP 401.
    """

    SCOPE = "https://api.businesscentral.dynamics.com/.default"

    def __init__(
        self,
        token_manager: TokenManager,
    ) -> None:
        self._token_manager = token_manager

    def _token_url(self) -> str:
        tenant_id = CredentialProvider.get_tenant_id()

        return (
            "https://login.microsoftonline.com/"
            f"{tenant_id}"
            "/oauth2/v2.0/token"
        )

    async def get_access_token(self) -> str:
        """
        Return a valid Business Central access token.

        Uses the cached token whenever possible.
        Generates a new token only when required.
        """

        # --------------------------------------------------
        # Fast path: use cached token
        # --------------------------------------------------

        cached = await self._token_manager.get_valid_token()

        if cached:
            return cached.access_token

        # --------------------------------------------------
        # Slow path: acquire refresh lock
        # --------------------------------------------------

        lock = self._token_manager.get_refresh_lock()

        async with lock:

            # --------------------------------------------------
            # Double-check after acquiring refresh lock.
            #
            # Another concurrent request may have generated
            # the token while this request was waiting.
            # --------------------------------------------------

            cached = await self._token_manager.get_valid_token()

            if cached:
                return cached.access_token

            # --------------------------------------------------
            # Generate new token
            # --------------------------------------------------

            token = await self._request_new_token()


            await self._token_manager.set_token(token)

            return token.access_token

    async def force_refresh(self) -> str:
        """
        Force token invalidation and generate a new token.

        Used after Business Central returns HTTP 401.
        """

        lock = self._token_manager.get_refresh_lock()

        async with lock:

            await self._token_manager.invalidate()

            token = await self._request_new_token()

            await self._token_manager.set_token(token)

            return token.access_token

    async def _request_new_token(self) -> OAuthToken:
        token_url = self._token_url()


        response = await HTTPClient.post_form(
            url=token_url,
            data={
                "grant_type": "client_credentials",
                "client_id": CredentialProvider.get_client_id(),
                "client_secret": CredentialProvider.get_client_secret(),
                "scope": self.SCOPE,
            },
        )

        if response.status_code != 200:
            raise AuthenticationError(
                f"Business Central authentication failed. "
                f"HTTP {response.status_code}: {response.text}"
            )

        try:
            token_data = TokenResponse.model_validate(response.json())
        except Exception as exc:
            raise AuthenticationError(
                "Invalid token response received."
            ) from exc

        expires_at = datetime.now(timezone.utc) + timedelta(
            seconds=token_data.expires_in
        )

        return OAuthToken(
            access_token=token_data.access_token,
            token_type=token_data.token_type,
            expires_in=token_data.expires_in,
            expires_at=expires_at,
        )