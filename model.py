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
def leverage(income_stmt1, income_stmt2, balance_sheet1, balance_sheet2):
    config: Dict = get_config()

    balance_sheet1 = balance_sheet1.transpose()
    balance_sheet2 = balance_sheet2.transpose()
    income_stmt1 = income_stmt1.transpose()
    income_stmt2 = income_stmt2.transpose()

    balance_sheet1[config["leverage"]["column1"]] = balance_sheet1.index
    balance_sheet2[config["leverage"]["column1"]] = balance_sheet2.index

    income_stmt1[config["net_debt"]["column1"]] = income_stmt1.index
    income_stmt2[config["net_debt"]["column1"]] = income_stmt2.index

    balance_sheet1 = balance_sheet1[[config["leverage"]["column1"], config["leverage"]["column2"]]]
    balance_sheet2 = balance_sheet2[[config["leverage"]["column1"], config["leverage"]["column2"]]]

    income_stmt1 = income_stmt1[[config["leverage"]["column1"], config["leverage"]["column3"]]]
    income_stmt2 = income_stmt2[[config["leverage"]["column1"], config["leverage"]["column3"]]]

    leverage1 = balance_sheet1[config["leverage"]["column2"]] / income_stmt1[config["leverage"]["column3"]]
    leverage2 = balance_sheet2[config["leverage"]["column2"]] / income_stmt2[config["leverage"]["column3"]]

    return leverage1, leverage2



