from repository import get_data_stock_market, get_company_financials_dfs
from constants import CONFIG_FILE
from view import display_chart_stock_market, display_data_company1, display_data_company2

data_stocks = get_data_stock_market()
print(data_stocks)
display_chart_stock_market(data_stocks)

display_data_company1()
display_data_company2()