from datetime import datetime

from pydantic import BaseModel, Field


class OAuthToken(BaseModel):
    access_token: str
    token_type: str
    expires_in: int
    expires_at: datetime


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
    expires_in: int = Field(gt=0)