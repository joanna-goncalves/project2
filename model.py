import numpy as np
import pandas as pd

from typing import Dict
from repository import get_config
from repository import get_company_financials_dfs

#calcul dette nette
def net_debt(balance_sheet1, balance_sheet2):
    config: Dict = get_config()

    balance_sheet1 = balance_sheet1.transpose()
    balance_sheet2 = balance_sheet2.transpose()

    balance_sheet1[config["net_debt"]["column1"]] = balance_sheet1.index
    balance_sheet2[config["net_debt"]["column1"]] = balance_sheet2.index

    balance_sheet1 = balance_sheet1[[config["net_debt"]["column1"], config["net_debt"]["column2"], config["net_debt"]["column3"]]]
    balance_sheet2 = balance_sheet2[[config["net_debt"]["column1"], config["net_debt"]["column2"], config["net_debt"]["column3"]]]

    net_debt1 = balance_sheet1[config["net_debt"]["column2"]] - balance_sheet1[config["net_debt"]["column3"]]
    net_debt2 = balance_sheet2[config["net_debt"]["column2"]] - balance_sheet2[config["net_debt"]["column3"]]

    return net_debt1, net_debt2

#calcul leverage
def leverage(income_stmt,balance_sheet):
    config: Dict = get_config()

    balance_sheet = balance_sheet.transpose()
    income_stmt = income_stmt.transpose()

    balance_sheet[config["leverage"]["column1"]] = balance_sheet.index
    income_stmt[config["leverage"]["column1"]] = income_stmt.index

    balance_sheet = balance_sheet[[config["leverage"]["column1"], config["leverage"]["column2"]]]
    income_stmt = income_stmt[[config["leverage"]["column1"], config["leverage"]["column3"]]]

    leverage = balance_sheet[config["leverage"]["column2"]] / income_stmt[config["leverage"]["column3"]]

    return leverage

def other_financial_ratios(income_stmt:pd.DataFrame, balance_sheet:pd.DataFrame)-> pd.DataFrame:
    config: Dict = get_config()
    balance_sheet = balance_sheet.transpose()
    income_stmt = income_stmt.transpose()

    balance_sheet[config["other_financial_ratios"]["column1"]] = balance_sheet.index
    income_stmt[config["other_financial_ratios"]["column1"]] = income_stmt.index

    financial_ratios = pd.DataFrame()

    financial_ratios["Current Ratio"]= balance_sheet[config["current_ratio"]["column1"]] / balance_sheet[config["current_ratio"]["column2"]]
    financial_ratios["Debt to Assets"] = balance_sheet[config["debt_to_assets"]["column1"]] / balance_sheet[config["debt_to_assets"]["column2"]]
    financial_ratios["Interest Coverage"] = income_stmt[config["interest_coverage"]["column1"]] / income_stmt[config["interest_coverage"]["column2"]]
    financial_ratios["ROE"] = income_stmt[config["ROE_ROA"]["column1"]] / balance_sheet[config["ROE_ROA"]["column2"]]
    financial_ratios["ROA"] = income_stmt[config["ROE_ROA"]["column1"]] / balance_sheet[config["ROE_ROA"]["column3"]]

    return financial_ratios