import os
from datetime import datetime

import pandas as pd

from src.reports import spending_by_category
from src.services import analyze_cashback_categories
from src.utils import get_greeting, get_read_excel
from src.views import home_page

base_dir = os.path.dirname(os.path.abspath(__file__))
# path_file_excel = os.path.join(base_dir, "data", "Книга2.xlsx")
path_file_excel = os.path.join(base_dir, "data", "operations.xlsx")


def main() -> None:
    """Функция, которая отвечает за основную логику проекта и связывает функциональности между собой"""
    df_xls = pd.read_excel(path_file_excel)
    df_xls.fillna(0, inplace=True)
    current_time = datetime.now()
    greeting = get_greeting(current_time)
    home_page(df_xls, "2021-12-31 00:00:00", greeting)
    data_list = get_read_excel(path_file_excel)
    analyze_cashback_categories(data_list, 2021, 12)
    # spending_by_category(df_xls, "Аптеки", "2021-12-31 00:00:00" )
    spending_by_category(df_xls, "аптеки", "2018-07-30 00:00:00")


main()
