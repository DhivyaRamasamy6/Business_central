from agent_framework import Agent
from config.settings import foundry_client
from prompts.crm_instructions import instructions
from tool.bc_tool import create_business_central_mcp
from tool.business_central.companies.read import list_companies,get_company
from tool.business_central.customers.read import list_customers,get_customer
from tool.business_central.sales_orders.read import list_sales_order,get_sales_order
from tool.business_central.invoices.read import list_invoices,get_invoice


agent = Agent(
    name="Business Central Agent",
    client=foundry_client,
    instructions=instructions,
    tools=[list_companies,get_company,list_customers,get_customer,list_invoices,get_invoice,list_sales_order,get_sales_order],
)


