import os
import pandas as pd

from typing import Any, Dict, List

from src.services import analyze_cashback_categories
from src.reports import spending_by_category
from src.utils import get_read_excel


base_dir = os.path.dirname(os.path.abspath(__file__))
path_file_excel = os.path.join(base_dir, "data", "Книга2.xlsx")
# path_file_excel = os.path.join(base_dir, "data", "operations.xlsx")
path_log_file = os.path.join(base_dir, "logs", "services.log")


def main() -> None:
    """"""
    # data = get_read_excel(path_file_excel)
    # print(data)
    # analyze_cashback_categories(data, 2019, 8)
    df_xls = pd.read_excel(path_file_excel)
    # df_shape = df_xls.shape
    # print(df_shape)
    df_xls.fillna(0, inplace=True)
    # print(dict(df_xls))
    spending_by_category(df_xls, "Супермаркеты", "31.12.2021" )





main()
