import pytest


@pytest.fixture
def sample_data():
    return [
        {
            'date': '2019-07-03T18:35:29.512364',
            'description': 'Перевод организации',
            'from': 'Visa Platinum 7000791163616361',
            'to': 'Счет 64686473678894779589',
            'operationAmount': {'amount': '82771.72', 'currency': {'name': 'руб'}}
        },
        {
            'date': '2018-07-03T18:35:29.512364',
            'description': 'Перевод организации',
            'from': 'Visa Platinum 8900791163616361',
            'to': 'Счет 64686473678894779589',
            'operationAmount': {'amount': '82771.72', 'currency': {'name': 'usd'}}
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "to": "Счет 11776614605963066702"
        }
    ]