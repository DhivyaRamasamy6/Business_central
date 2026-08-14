from fastapi import APIRouter,FastAPI
from model.request import ChatRequest
from models.response import ChatResponse
from agents.crm_agent import agent
from utils.human_approval import handle_approvals
from utils.session_manager import session_manager

router = APIRouter(prefix="/Agent_Response",tags=["Business Central Agent"])
@router.post("/chat",response_model=ChatResponse,)
async def chat(request:ChatRequest):

    session = session_manager.get_or_create(
        request.session_id,
        agent,
    )
    print(f"Session ID: {session.session_id}")
    result = await agent.run(
        request.message,
        session=session,
    )
    print(f"Agent Result: {result.text}")

    result = await handle_approvals(
        agent,
        result,
        session,
    )

    return ChatResponse(
        response=result.text,
    )

