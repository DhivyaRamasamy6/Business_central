from agent_framework import MCPStdioTool
from logger import get_logger
logger = get_logger(__name__)

def business_tool():
    logger.info("Business Tool is invoking")
    return MCPStdioTool(
        name="Business Central",
        command="python",
        args=["server.py"],
        approval_mode={
            "always_require_approval": [
                # Company information — contains address, tax ID, etc.
                "get_company_information",
                # Contacts — PII (names, phone, email, address)
                "list_contacts",
                "get_contact",
                "list_contact_information",
                # Invoices — financial/sensitive
                "list_sales_invoices",
                "get_sales_invoice",
                "list_purchase_invoices",
                "get_purchase_invoice",
            ],
            "never_require_approval": [
                "list_companies",
                "list_customers", "get_customer",
                "list_vendors", "get_vendor",
                "list_items", "get_item",
                "list_salespeople", "get_salesperson",
                "list_sales_quotes", "get_sales_quote",
                "list_sales_orders", "get_sales_order",
                "list_sales_credit_memos", "get_sales_credit_memo",
                "list_sales_shipments", "get_sales_shipment",
                "list_journals", "get_journal",
                "list_currencies", "get_currency",
            ],
        },
    )