import json
import os
from collections.abc import Callable
from datetime import datetime, timedelta
from functools import wraps
from typing import Any, Optional

import pandas as pd

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_file_report = os.path.join(base_dir, "reports", "my_report.json")


def reports_decorator(filename: Optional[str] = None) -> Callable:
    """Декоратор для функций-отчетов, записывающий результат в файл,
    filename - имя файла для записи отчета. Если None, используется имя по умолчанию."""

    def my_decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            nonlocal filename
            try:
                result = func(*args, **kwargs)
                if filename is None:
                    file_name = f"{func.__name__}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
                    filename = os.path.join(base_dir, "reports", file_name)
                    os.makedirs(os.path.dirname(filename), exist_ok=True)
                if isinstance(result, pd.DataFrame):
                    with open(filename, "w", encoding="utf-8") as file:
                        json.dump(result.to_dict(orient="records"), file, ensure_ascii=False, indent=4)
                    print(f"Данные успешно записаны в файл: {filename}")
                    return result
            except TypeError as error:
                print(f"Данные не были записаны в файл из-за ошибки {error.__class__.__name__}")

        return wrapper

    return my_decorator


@reports_decorator(filename=path_file_report)
def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция возвращает траты по заданной категории за последние три месяца (от переданной даты)."""
    if date is None:
        date_obj = datetime.now().strftime("%Y-%m-%d")
    else:
        try:
            date_obj = datetime.strptime(date, "%d.%m.%Y")
            print(date)
        except ValueError:
            raise ValueError("Неверный формат даты. Используйте DD.MM.YYYY")
    try:
        transactions["Дата операции"] = pd.to_datetime(transactions["Дата операции"], dayfirst=True)
        # print(transactions['Дата операции'])
    except KeyError:
        raise KeyError("В DataFrame отсутствует колонка 'Дата операции'")
    starting_date = date_obj - timedelta(days=90)
    print(type(date_obj), type(timedelta))
    print(starting_date)
    filtered_transactions = transactions[
        (transactions["Дата операции"] >= starting_date)
        & (transactions["Дата операции"] <= date_obj)
        & (transactions["Категория"].str.upper() == category.upper())
    ]
    if filtered_transactions.empty:
        print("Нет транзакций по этой категории за указанный период.")
        return pd.DataFrame()
    result_transactions = pd.DataFrame(
        filtered_transactions.groupby("Категория", as_index=False).agg({"Сумма операции": "sum"})
    )
    # result_transactions = pd.DataFrame(filtered_transactions.groupby('Категория', as_index=False).
    #                                    sum(numeric_only=True)['Сумма операции'])
    print(result_transactions)
    result_dict = result_transactions.to_dict(orient="records")
    print(result_dict)
    return result_transactions


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path_file_excel = os.path.join(base_dir, "data", "Книга4.xlsx")
# path_file_excel = os.path.join(base_dir, "data", "operations.xlsx")
df_xls = pd.read_excel(path_file_excel)
df_xls.fillna(0, inplace=True)
spending_by_category(df_xls, "Каршеринг", "31.12.2021")

# Супермаркеты       -25510.56  ...                      25510.56
