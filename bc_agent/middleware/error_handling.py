from collections.abc import Awaitable, Callable
from agent_framework import (
    AgentContext,
    AgentResponse,
    Message,
)


async def error_handling_middleware(
    context: AgentContext,
    call_next: Callable[[AgentContext], Awaitable[None]],
) -> None:

    try:

        await call_next(context)

    except PermissionError as exc:

        print(
            f"[ERROR] Authorization/security failure: {exc}"
        )

        context.result = AgentResponse(
            messages=[
                Message(
                    role="assistant",
                    contents=[
                        "You are not authorized to perform "
                        "this operation."
                    ],
                )
            ]
        )

    except ValueError as exc:

        print(
            f"[ERROR] Validation failure: {exc}"
        )

        context.result = AgentResponse(
            messages=[
                Message(
                    role="assistant",
                    contents=[
                        "The request contains invalid information. "
                        "Please check the provided details."
                    ],
                )
            ]
        )

    except Exception as exc:

        print(
            f"[ERROR] Unexpected agent error: {exc}"
        )

        context.result = AgentResponse(
            messages=[
                Message(
                    role="assistant",
                    contents=[
                        "I couldn't complete the request. "
                        "Please try again or provide more information."
                    ],
                )
            ]
        )