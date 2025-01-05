# import os

from datetime import datetime
from typing import Any, Dict, List

import pandas as pd


def get_read_excel(path_file_excel: str) -> List[Dict[str, Any]]:
    """Функция чтения EXCEL-файла"""
    try:
        df_xls = pd.read_excel(path_file_excel)
        # df_shape = df_xls.shape
        # print(df_shape)
        df_xls.fillna(0, inplace=True)
    except Exception as e:
        print(type(e).__name__)
        return []
    dict_read_excel = df_xls.to_dict(orient="records")
    return dict_read_excel


# base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# path_file_excel = os.path.join(base_dir, "data", "Книга4.xlsx")
# path_file_excel = os.path.join(base_dir, "data", "operations.xlsx")
# read_excel_transaction = get_read_excel(path_file_excel)
# print(read_excel_transaction)


def date_conversions(transactions: Dict[str, Any]) -> datetime | None:
    """Преобразование даты в объект datetime"""
    try:
        if transactions["Дата операции"] != 0:
            date_operation = transactions["Дата операции"].split(" ")
            date_obj = datetime.strptime(date_operation[0], "%d.%m.%Y")
            return date_obj
        else:
            return None
    except Exception as e:
        print(type(e).__name__)
        return None
