from repository import get_data_stock_market, get_company_financials_dfs
from constants import CONFIG_FILE
from view import display_chart_stock_market

data_stocks = get_data_stock_market()
print(data_stocks)

income_stmt_df, balance_sheet_df, cashflow_df = get_company_financials_dfs("ENGI.PA")
print("=== INCOME STATEMENT ===")
print(income_stmt_df.head())

print("=== BALANCE SHEET ===")
print(balance_sheet_df.head())

print("=== CASH FLOW ===")
print(cashflow_df.head())

display_chart_stock_market(data_stocks)