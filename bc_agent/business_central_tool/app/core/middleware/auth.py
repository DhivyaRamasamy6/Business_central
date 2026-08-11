from app.integrations.business_central.auth import AuthenticationService


class AuthenticationMiddleware:

    @staticmethod
    async def get_headers():

        token = await AuthenticationService.get_access_token()

        return {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }