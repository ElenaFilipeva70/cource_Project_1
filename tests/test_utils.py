from typing import Any, Dict
from unittest.mock import patch

import pandas as pd

from src.utils import get_read_excel


@patch("pandas.read_excel")
def test_get_read_excel(mock_read_excel) -> None:
    """Тестируем чтение EXCEL-файла"""
    transaction_dict = {"key1": ["value1", "value2"], "key2": ["value1", "value2"]}
    mock_read_excel.return_value = pd.DataFrame(transaction_dict)
    assert get_read_excel("test.xlsx") == [{"key1": "value1", "key2": "value1"}, {"key1": "value2", "key2": "value2"}]
    mock_read_excel.assert_called_once()


def test_get_read_excel_empty() -> None:
    """Проверяем работу функции, если файл пустой"""
    result = get_read_excel("data/orders_empty.xlsx")
    assert result == []


def test_get_read_excel_not_found() -> None:
    """Проверяем работу функции, если файл не найден"""
    result = get_read_excel("data/orders_empty1.xlsx")
    assert result == []


# def test_date_conversions() -> None:
#     """Тестируем работу функции на преобразование даты в объект datetime"""
#     test_transaction: Dict[str, Any] = {
#         "Дата операции": "31.12.2021 16:44:00",
#         "Дата платежа": "31.12.2021",
#         "Номер карты": "*7197",
#         "Статус": "OK",
#         "Сумма операции": -160.89,
#         "Валюта операции": "RUB",
#         "Кэшбэк": 0,
#         "Категория": "Супермаркеты",
#     }
#     assert date_conversions(test_transaction) == datetime(2021, 12, 31, 0, 0)
#
#
# def test_date_conversions_empty() -> None:
#     """Проверяем работу функции, когда значение 'Дата операции' пустое в исходном файле транзакций"""
#     test_transaction: Dict[str, Any] = {
#         "Дата операции": 0,
#         "Дата платежа": "31.12.2021",
#         "Номер карты": "*7197",
#         "Статус": "OK",
#         "Сумма операции": -160.89,
#         "Валюта операции": "RUB",
#         "Кэшбэк": 0,
#         "Категория": "Супермаркеты",
#     }
#     assert date_conversions(test_transaction) == None
