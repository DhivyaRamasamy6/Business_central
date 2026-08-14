from pydantic import BaseModel
from typing import Any


class PendingApproval(BaseModel):
    request_id: str
    tool_name: str
    arguments: dict[str, Any]


class ApprovalDecision(BaseModel):
    session_id: str
    request_id: str
    approved: bool