from mcp.server.fastmcp import FastMCP

from client import BusinessCentralClient

mcp = FastMCP(
    "Business Central MCP Server",
)
bc = BusinessCentralClient()


#npx @modelcontextprotocol/inspector python server.py 
# ==========================
# Company
# ==========================

@mcp.tool(name="list_companies")
def list_companies():
    """List all companies in this Business Central environment. Call this first to get a company_id."""
    return bc.get("companies")


@mcp.tool(name="get_company_information")
def get_company_information(company_id: str):
    """Get the company information object (name, address, currency, fiscal year start, etc.) for a company."""
    return bc.get(f"companies({company_id})/companyInformation")


# ==========================
# Customers
# ==========================

@mcp.tool(name="list_customers")
def list_customers(company_id: str):
    """List all customers for a company."""
    return bc.get(f"companies({company_id})/customers")


@mcp.tool(name="get_customer")
def get_customer(company_id: str, customer_id: str):
    """Get a single customer by ID."""
    return bc.get(f"companies({company_id})/customers({customer_id})")


# ==========================
# Vendors
# ==========================

@mcp.tool(name="list_vendors")
def list_vendors(company_id: str):
    """List all vendors for a company."""
    return bc.get(f"companies({company_id})/vendors")


@mcp.tool(name="get_vendor")
def get_vendor(company_id: str, vendor_id: str):
    """Get a single vendor by ID."""
    return bc.get(f"companies({company_id})/vendors({vendor_id})")


# ==========================
# Items
# ==========================

@mcp.tool(name="list_items")
def list_items(company_id: str):
    """List all inventory items for a company."""
    return bc.get(f"companies({company_id})/items")


@mcp.tool(name="get_item")
def get_item(company_id: str, item_id: str):
    """Get a single inventory item by ID."""
    return bc.get(f"companies({company_id})/items({item_id})")


# ==========================
# Contacts (CRM)
# ==========================

@mcp.tool(name="list_contacts")
def list_contacts(company_id: str):
    """List all contacts (people/companies in the CRM relationship graph) for a company."""
    return bc.get(f"companies({company_id})/contacts")


@mcp.tool(name="get_contact")
def get_contact(company_id: str, contact_id: str):
    """Get a single contact by ID."""
    return bc.get(f"companies({company_id})/contacts({contact_id})")


@mcp.tool(name="list_contact_information")
def list_contact_information(company_id: str,customer_id:str):
    """List contact-to-customer/vendor/bank/employee relationship records for a company."""
    return bc.get(f"companies({company_id})/customers({customer_id})/contactsInformation")


# ==========================
# Salespeople (CRM)
# ==========================

@mcp.tool(name="list_salespeople")
def list_salespeople(company_id: str):
    """List all salespeople (salesperson/purchaser records) for a company."""
    return bc.get(f"companies({company_id})/salespeoplePurchasers")


@mcp.tool(name="get_salesperson")
def get_salesperson(company_id: str, salesperson_id: str):
    """Get a single salesperson by ID."""
    return bc.get(f"companies({company_id})/salespeoplePurchasers({salesperson_id})")


# ==========================
# Sales Quotes (CRM)
# ==========================

@mcp.tool(name="list_sales_quotes")
def list_sales_quotes(company_id: str):
    """List all sales quotes for a company."""
    return bc.get(f"companies({company_id})/salesQuotes")


@mcp.tool(name="get_sales_quote")
def get_sales_quote(company_id: str, quote_id: str):
    """Get a single sales quote by ID."""
    return bc.get(f"companies({company_id})/salesQuotes({quote_id})")


# ==========================
# Sales Orders
# ==========================

@mcp.tool(name="list_sales_orders")
def list_sales_orders(company_id: str):
    """List all sales orders for a company."""
    return bc.get(f"companies({company_id})/salesOrders")


@mcp.tool(name="get_sales_order")
def get_sales_order(company_id: str, sales_order_id: str):
    """Get a single sales order by ID."""
    return bc.get(f"companies({company_id})/salesOrders({sales_order_id})")


# ==========================
# Sales Invoices
# ==========================

@mcp.tool(name="list_sales_invoices")
def list_sales_invoices(company_id: str):
    """List all sales invoices for a company."""
    return bc.get(f"companies({company_id})/salesInvoices")


@mcp.tool(name="get_sales_invoice")
def get_sales_invoice(company_id: str, invoice_id: str):
    """Get a single sales invoice by ID."""
    return bc.get(f"companies({company_id})/salesInvoices({invoice_id})")


# ==========================
# Sales Credit Memos (CRM)
# ==========================

@mcp.tool(name="list_sales_credit_memos")
def list_sales_credit_memos(company_id: str):
    """List all sales credit memos for a company."""
    return bc.get(f"companies({company_id})/salesCreditMemos")


@mcp.tool(name="get_sales_credit_memo")
def get_sales_credit_memo(company_id: str, credit_memo_id: str):
    """Get a single sales credit memo by ID."""
    return bc.get(f"companies({company_id})/salesCreditMemos({credit_memo_id})")


# ==========================
# Sales Shipments (CRM)
# ==========================

@mcp.tool(name="list_sales_shipments")
def list_sales_shipments(company_id: str):
    """List all sales shipments for a company."""
    return bc.get(f"companies({company_id})/salesShipments")


@mcp.tool(name="get_sales_shipment")
def get_sales_shipment(company_id: str, shipment_id: str):
    """Get a single sales shipment by ID."""
    return bc.get(f"companies({company_id})/salesShipments({shipment_id})")


# ==========================
# Purchase Invoices
# ==========================

@mcp.tool(name="list_purchase_invoices")
def list_purchase_invoices(company_id: str):
    """List all purchase invoices for a company."""
    return bc.get(f"companies({company_id})/purchaseInvoices")


@mcp.tool(name="get_purchase_invoice")
def get_purchase_invoice(company_id: str, invoice_id: str):
    """Get a single purchase invoice by ID."""
    return bc.get(f"companies({company_id})/purchaseInvoices({invoice_id})")


# ==========================
# Journals
# ==========================

@mcp.tool(name="list_journals")
def list_journals(company_id: str):
    """List all journals for a company."""
    return bc.get(f"companies({company_id})/journals")


@mcp.tool(name="get_journal")
def get_journal(company_id: str, journal_id: str):
    """Get a single journal by ID."""
    return bc.get(f"companies({company_id})/journals({journal_id})")


# ==========================
# Currencies
# ==========================

@mcp.tool(name="list_currencies")
def list_currencies(company_id: str):
    """List all currencies configured for a company."""
    return bc.get(f"companies({company_id})/currencies")


@mcp.tool(name="get_currency")
def get_currency(company_id: str, currency_id: str):
    """Get a single currency by ID."""
    return bc.get(f"companies({company_id})/currencies({currency_id})")


if __name__ == "__main__":
    mcp.run()