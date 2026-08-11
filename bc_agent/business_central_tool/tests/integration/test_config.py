from business_central_tool.app.core.config import settings


def main() -> None:
    print("Configuration loaded successfully")

    print(
        "BC tenant configured:",
        bool(settings.bc_tenant_id)
        and settings.bc_tenant_id != "...",
    )

    print(
        "BC client configured:",
        bool(settings.bc_client_id)
        and settings.bc_client_id != "...",
    )

    print(
        "BC secret configured:",
        bool(settings.bc_client_secret)
        and settings.bc_client_secret != "...",
    )

    print(
        "BC company configured:",
        bool(settings.bc_company_id)
        and settings.bc_company_id != "...",
    )

    print("BC environment:", settings.bc_environment)
    print("BC API version:", settings.bc_api_version)


if __name__ == "__main__":
    main()