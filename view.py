from typing import Dict

import matplotlib

import numpy as np
import pandas as pd

import seaborn as sns

from matplotlib import pyplot as plt
from repository import get_config
from repository import get_company_financials_dfs

#graphique cours des actions
def display_chart_stock_market(data):
    config: Dict = get_config()
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    ax[0].plot(
        data.index,
        data[config["chart"]["column3"]],
        color=config["chart"]["colorCAC40"],
        label=config["chart"]["label3"],
    )
    ax[0].legend(loc=config["chart"]["legend_loc1"])
    ax2 = ax[0].twinx()
    ax2.plot(
        data.index,
        data[config["chart"]["column1"]],
        color=config["chart"]["colorCompany1"],
        label=config["chart"]["label1"],
    )
    ax2.legend(loc=config["chart"]["legend_loc2"])
    ax[0].tick_params(axis="x", rotation=config["chart"]["rotation"])
    ax[1].plot(
        data.index,
        data[config["chart"]["column3"]],
        color=config["chart"]["colorCAC40"],
        label=config["chart"]["label3"],
    )
    ax[1].legend(loc=config["chart"]["legend_loc1"])
    ax3 = ax[1].twinx()
    ax3.plot(
        data.index,
        data[config["chart"]["column2"]],
        color=config["chart"]["colorCompany2"],
        label=config["chart"]["label2"],
    )
    ax[1].tick_params(axis="x", rotation=config["chart"]["rotation"])
    ax3.legend(loc=config["chart"]["legend_loc2"])

    plt.legend()
    plt.show()

#montrer les données financières des deux entreprises
def display_data_company1():
    config: Dict = get_config()
    income_stmt_df1, balance_sheet_df1, cashflow_df1 = get_company_financials_dfs(config["portfolio"]["ticker1"])
    return income_stmt_df1, balance_sheet_df1, cashflow_df1

def display_data_company2():
    config: Dict = get_config()
    income_stmt_df2, balance_sheet_df2, cashflow_df2 = get_company_financials_dfs(config["portfolio"]["ticker2"])
    return income_stmt_df2, balance_sheet_df2, cashflow_df2


#graphique de comparaison de l'évolution de l'EBITDA des deux entreprises
def display_ebitda_chart(income_stmt_df1, income_stmt_df2):
    config: Dict = get_config()

    income_stmt_df1 = income_stmt_df1.transpose().reset_index()
    income_stmt_df2 = income_stmt_df2.transpose().reset_index()

    income_stmt_df1[config["chart_ebitda"]["x"]] = pd.to_datetime(income_stmt_df1['index']).dt.year
    income_stmt_df2[config["chart_ebitda"]["x"]] = pd.to_datetime(income_stmt_df2['index']).dt.year

    income_stmt_df1[config["chart_ebitda"]["y"]] = income_stmt_df1[config["chart_ebitda"]["y"]] / 1000000000
    income_stmt_df2[config["chart_ebitda"]["y"]] = income_stmt_df2[config["chart_ebitda"]["y"]] / 1000000000

    income_stmt_df1 = income_stmt_df1[[config["chart_ebitda"]["x"], config["chart_ebitda"]["y"]]]
    income_stmt_df2 = income_stmt_df2[[config["chart_ebitda"]["x"], config["chart_ebitda"]["y"]]]

    income_stmt_df1.columns = [config["chart_ebitda"]["x"], config["chart_ebitda"]["y"]]
    income_stmt_df2.columns = [config["chart_ebitda"]["x"], config["chart_ebitda"]["y"]]

    fig, ax = plt.subplots(figsize=(10, 6))

    sns.lineplot(
        ax=ax,
        x=income_stmt_df1[config["chart_ebitda"]["x"]],
        y=income_stmt_df1[config["chart_ebitda"]["y"]],
        marker=config["chart_ebitda"]["marker"],
        label=config["portfolio"]["ticker1"]
    )

    sns.lineplot(
        ax=ax,
        x=income_stmt_df2[config["chart_ebitda"]["x"]],
        y=income_stmt_df2[config["chart_ebitda"]["y"]],
        marker=config["chart_ebitda"]["marker"],
        label=config["portfolio"]["ticker2"]
    )

    ax.set_xlabel(config["chart_ebitda"]["label1"])
    ax.set_ylabel(config["chart_ebitda"]["label2"])
    ax.set_title(config["chart_ebitda"]["title"])

    plt.legend()
    plt.show()
