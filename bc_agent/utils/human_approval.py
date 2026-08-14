from common.logger import get_logger
logger = get_logger(__name__)
async def handle_approvals(agent, result, session):
    """
    Loop until all pending approval requests are resolved.
    """

    while result.user_input_requests:

        logger.info(
            "Approval requests pending: %s",
            len(result.user_input_requests),
        )

        for request in result.user_input_requests:

            logger.info(
                "Tool requested: %s",
                request.function_call.name,
            )

            logger.info(
                "Arguments: %s",
                request.function_call.arguments,
            )

            decision = (
                input("Approve? (y/n): ").strip().lower() == "y"
            )

            logger.info(
                "Approval decision: %s",
                "Approved" if decision else "Rejected",
            )

            approval = request.to_function_approval_response(
                approved=decision
            )

            result = await agent.run(
                approval,
                session=session,
            )

    return result

