import asyncio
from typing import Optional

from .oauth_models import OAuthToken


class TokenCache:
    """
    Thread/task-safe in-memory token cache.

    Maintains:
    - Cached OAuth token
    - Dedicated refresh lock
    """

    def __init__(self) -> None:
        self._token: Optional[OAuthToken] = None
        self._cache_lock = asyncio.Lock()
        self._refresh_lock = asyncio.Lock()

    async def get(self) -> Optional[OAuthToken]:
        async with self._cache_lock:
            return self._token

    async def set(self, token: OAuthToken) -> None:
        async with self._cache_lock:
            self._token = token

    async def clear(self) -> None:
        async with self._cache_lock:
            self._token = None

    async def get_lock(self) -> asyncio.Lock:
        return self._refresh_lock