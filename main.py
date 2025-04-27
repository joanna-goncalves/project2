from model import net_debt
from repository import get_data_stock_market, get_company_financials_dfs

from constants import CONFIG_FILE

from view import display_chart_stock_market, display_data_company1, display_data_company2, display_ebitda_chart

from model import net_debt, leverage

data_stocks = get_data_stock_market()
print(data_stocks)
display_chart_stock_market(data_stocks)

display_data_company1()
display_data_company2()

income_stmt_df1, _, _ = display_data_company1()
income_stmt_df2, _, _ = display_data_company2()

display_ebitda_chart(income_stmt_df1, income_stmt_df2)

_, balance_sheet1, _ = display_data_company1()
_, balance_sheet2, _ = display_data_company2()

print(net_debt(balance_sheet1, balance_sheet2))

print(leverage(income_stmt_df1, income_stmt_df2, balance_sheet1, balance_sheet2))