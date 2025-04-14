import os
from typing import Dict

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