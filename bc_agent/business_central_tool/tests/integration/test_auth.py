import asyncio

from business_central_tool.app.integrations.business_central import (
    create_business_central_services,
)


async def main() -> None:

    services = create_business_central_services()

    token = await services["auth"].get_access_token()



if __name__ == "__main__":
    asyncio.run(main())