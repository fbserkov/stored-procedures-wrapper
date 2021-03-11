from config import TOKEN_TEST
import requests

LOCAL = True
if LOCAL:
    ip = '127.0.0.1'
    port = 8080  # 5000
else:
    from config import IP
    ip = IP
    port = 8080


def sync_status():
    temp = requests.get(f'http://{ip}:{port}/sync_status')
    print(temp.text)


def valid_codes():
    temp = requests.get(f'http://{ip}:{port}/valid_codes')
    print(temp.json())


def valid_names(code):
    temp = requests.get(f'http://{ip}:{port}/{code}/valid_names')
    print(temp.json())


def is_dated(name):
    temp = requests.get(f'http://{ip}:{port}/{name}/is_dated')
    print(temp.text)


def test_data_source_sync(code):
    temp = requests.post(
        f'http://{ip}:{port}/data_source_sync',
        json=dict(
            token=TOKEN_TEST, user='test_user',
            code=code, month=7, year=2019,
        ),
    )
    print(temp.text)


def test_entity_sync(name, code):
    temp = requests.post(
        f'http://{ip}:{port}/entity_sync',
        json=dict(
            token=TOKEN_TEST, user='test_user',
            name=name, code=code, month=7, year=2019,
        ),
    )
    print(temp.text)


# valid_codes()
# valid_names('0c06')
# is_dated('turnover_balance_sheet')  # personal_account, turnover_balance_sheet

from const import T_B_S, P_A_P
# test_data_source_sync('0c06')  # 0c06, zagser
# test_entity_sync(P_A_P, '0c10')
# test_entity_sync(T_B_S, 'stek')
# test_entity_sync(T_B_S, 'zagser')

sync_status()
