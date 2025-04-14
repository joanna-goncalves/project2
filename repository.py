import os
from typing import Dict

import pandas as pd

import numpy as np
import yfinance as yf

from constants import CONFIG_FILE
from helpers_serialize import get_serialized_data

def get_config() -> Dict:
    path: str = os.path.join(os.getcwd(), CONFIG_FILE)
    return get_serialized_data(path)



#téléchargement data du cours des actions
def get_data_stock_market():
    config: Dict = get_config()
    tickers = list(config["portfolio"].values())
    data_stock_market = yf.download(
        tickers,
        start=config["initialisation"]["begin_date"],
        end=config["initialisation"]["end_date"],
    )
    return data_stock_market[config["initialisation"]["field_to_keep"]]

#telechargement données des entreprises
def get_company_financials_dfs(ticker: str):
    config: Dict = get_config()
    start_date = config["initialisation"]["begin_date"]
    end_date = config["initialisation"]["end_date"]
    company = yf.Ticker(ticker)
    info_df = pd.DataFrame([company.info]).T
    income_stmt_df = company.income_stmt
    balance_sheet_df = company.balance_sheet
    cashflow_df = company.cashflow

    def filter_by_date(df):
        return df.loc[:, (df.columns >= pd.to_datetime(start_date)) & (df.columns <= pd.to_datetime(end_date))]

    income_stmt_df = filter_by_date(income_stmt_df)
    balance_sheet_df = filter_by_date(balance_sheet_df)
    cashflow_df = filter_by_date(cashflow_df)

    return income_stmt_df, balance_sheet_df, cashflow_df


