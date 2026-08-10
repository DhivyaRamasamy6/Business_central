from typing import Dict
from agent_framework import AgentSession

class SessionManager:

    def __init__(self):

        self._sessions: Dict[str, AgentSession] = {}

    def get_or_create(
        self,
        session_id: str,
        agent,
    ):

        if session_id not in self._sessions:

            self._sessions[session_id] = agent.create_session()

        return self._sessions[session_id]

    def delete(
        self,
        session_id: str,
    ):

        self._sessions.pop(session_id, None)
session_manager = SessionManager()