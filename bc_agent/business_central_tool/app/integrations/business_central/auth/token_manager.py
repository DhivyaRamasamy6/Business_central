from datetime import datetime, timedelta, timezone
from typing import Optional
import asyncio

from business_central_tool.app.core.config import settings

from .oauth_models import OAuthToken
from .token_cache import TokenCache


class TokenManager:
    """
    Manages the Business Central access-token lifecycle.

    Responsibilities:
    - Retrieve cached access tokens.
    - Validate token expiry.
    - Refresh before token expiry.
    - Store refreshed tokens.
    - Invalidate tokens after authentication failures.
    - Prevent concurrent token refresh operations.

    Design:
    - TokenCache owns cache synchronization.
    - TokenManager owns refresh synchronization.
    """

    def __init__(self, cache: TokenCache) -> None:
        self._cache = cache

        # Dedicated lock for token refresh.
        #
        # This MUST be separate from TokenCache's internal
        # cache lock to avoid re-entrant locking/deadlocks.
        self._refresh_lock = asyncio.Lock()

    async def get_valid_token(
        self,
    ) -> Optional[OAuthToken]:
        """
        Return a valid cached token.

        Returns None when:
        - no token exists
        - token is expired
        - token is inside the configured refresh buffer
        """

        token = await self._cache.get()

        if token is None:
            return None

        refresh_at = token.expires_at - timedelta(
            seconds=settings.token_refresh_buffer
        )

        now = datetime.now(timezone.utc)

        if now >= refresh_at:
            return None

        return token

    async def set_token(
        self,
        token: OAuthToken,
    ) -> None:
        """
        Store a newly generated token.
        """

        await self._cache.set(token)

    async def invalidate(self) -> None:
        """
        Remove the cached token.
        """

        await self._cache.clear()

    def get_refresh_lock(self) -> asyncio.Lock:
        """
        Return the lock used to synchronize token refresh.

        This lock belongs to TokenManager, not TokenCache.
        """

        return self._refresh_lock