import json
from datetime import datetime

def get_data(path):
    '''Получить путь к файлу json и вернуть данные в виде списка словарей'''

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def select_data(data):
    '''Получить данные о транзакциях и вернуть список успешно завершенных транзакций'''
    selected_data = []

    for transaction in data:
        if 'state' in transaction and transaction['state'] == 'EXECUTED':
            selected_data.append(transaction)

    return selected_data


def sort_data(data):
    '''Получить данные о транзакциях и вернуть список последних пяти транзакций'''
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:5]


def format_account(account: list):
    '''Получить данные о получателе или отправителе в формате списка и вернитуть их с частично скрытыми цифрами'''
    if len(account[-1]) == 20:
        formatted_account = " ".join(account[:-1]) + ' ' + f'**{account[-1][-4:]}'
    elif len(account[-1]) == 16:
        formatted_account = " ".join(
            account[:-1]) + ' ' + f'{account[-1][:4]} {account[-1][4:6]}** **** {account[-1][-4:]}'
    else:
        formatted_account = "Недопустимый формат"

    return formatted_account


def format_data(data):
    '''Получить данные транзакции и вернуть их в отформатированном виде'''
    formatted_data = []
    arrow = ' -> '
    for transaction in data:
        date = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = transaction['description']
        to = format_account(transaction['to'].split())

        if 'from' in transaction:
            where_from = format_account(transaction['from'].split())
            transaction_info = where_from + arrow + to
        else:
            transaction_info = to

        amount = transaction['operationAmount']['amount'] + ' ' + transaction['operationAmount']['currency']['name']
        formatted_data.append(f"""
{date} {description}
{transaction_info}
{amount}\n""")
    return formatted_data
