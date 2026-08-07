import asyncio
import logging

from agent_framework import Agent
from business_tool import business_tool
from config import foundry_client
from logger import get_logger
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


async def main():

    logger.info("Starting Customer Support Agent")

    tool = business_tool()

    async with tool:

        logger.info("Connected to MCP Tool")

        agent = Agent(
            name="Customer Support Agent",
            instructions="""
            You are a Business Central assistant with read-only access to ERP/CRM data.

            Capabilities:
            - Company information
            - Customers
            - Vendors
            - Items
            - CRM
            - Sales Orders
            - Sales Invoices
            - Journals
            - Currency

            Always use the available tools.
            Never guess Business Central data.
            """,
            tools=[tool],
            client=foundry_client,
        )

        logger.info("Agent created")

        session = agent.create_session()

        logger.info("Session created")

        while True:

            query = input("\nQuery: ")

            if query.lower() == "exit":
                logger.info("Stopping agent")
                break

            logger.info("User Query: %s", query)

            try:

                result = await agent.run(
                    query,
                    session=session,
                )

                logger.info("Agent execution completed")

                result = await handle_approvals(
                    agent,
                    result,
                    session,
                )

                logger.info("Final Response:")
                logger.info(result.text)

                print("\nAssistant:")
                print(result.text)

            except Exception:

                logger.exception(
                    "Agent execution failed"
                )


if __name__ == "__main__":
    asyncio.run(main())