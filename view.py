from typing import Dict
import matplotlib

import numpy as np
import pandas as pd

from matplotlib import pyplot as plt
from repository import get_config

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