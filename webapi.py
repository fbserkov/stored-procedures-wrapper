from config import TOKENS
from const import (
    CODES_ALL, CODES_DESC, CODES_STACK,
    NAMES_ALL, NAMES_COMMON, NAMES_DATED, NAMES_DESC,
)

from datetime import date
from threading import Thread

from flask import Flask, jsonify, request
from waitress import serve

from sync import sync_data_source, sync_entity
from utils import flush_std, now2str

APP = Flask(__name__)
APP.config['JSON_AS_ASCII'] = False

THREAD = None


def check_values(params):
    if 'token' not in params:
        return 'Authorization token is needed.'
    if params['token'] not in TOKENS:
        return 'Invalid token value.'

    if 'user' not in params:
        return 'User is not specified.'
    if not params['user']:
        return 'Invalid user value.'

    if params['code'] not in CODES_ALL:
        return f"Invalid code value: {params['code']}."

    if 'name' in params:
        if params['name'] not in NAMES_ALL:
            return f"Invalid name value: {params['name']}."

    if 'month' in params and 'year' in params:
        str_date = f"{params['year']}-{params['month']:02}"
        if not '201801' <= str_date <= date.today().strftime('%Y-%m'):
            return f"Invalid date value: {str_date}."

    if THREAD and THREAD.is_alive():
        return f'Thread is busy, try again later.'


@APP.route('/sync_status', methods=['GET'])
def sync_status():
    flush_std()
    if THREAD and THREAD.is_alive():
        return 'Synchronization is running.'
    return 'Synchronization is not running.'


@APP.route('/valid_codes', methods=['GET'])
def get_valid_codes():
    return jsonify(CODES_DESC)


@APP.route('/<code>/valid_names', methods=['GET'])
def get_valid_names(code):
    if code not in CODES_ALL:
        return jsonify(None)
    if code not in CODES_STACK:
        return jsonify(NAMES_DESC)
    return jsonify({
        key: NAMES_DESC[key] for key in NAMES_DESC if key in NAMES_COMMON})


@APP.route('/<name>/is_dated', methods=['GET'])
def is_dated(name):
    if name not in NAMES_ALL:
        return str(None)
    return str(name in NAMES_DATED)


@APP.route('/data_source_sync', methods=['POST'])
def data_source_synchronization():
    message = check_values(request.json)
    if message:
        return message

    global THREAD
    print(
        f'{now2str()} - *** call sync_data_source(): '
        f'{request.json["user"]} ***\n'
    )
    THREAD = Thread(
        target=sync_data_source,
        kwargs=dict(
            code=request.json['code'],
            month=request.json['month'],
            year=request.json['year'],
            run=True,
        )
    )
    THREAD.start()
    return 'Synchronization was started.'


@APP.route('/entity_sync', methods=['POST'])
def entity_synchronization():
    message = check_values(request.json)
    if message:
        return message

    global THREAD
    print(
        f'{now2str()} - *** call sync_entity(): '
        f'{request.json["user"]} ***\n'
    )
    THREAD = Thread(
        target=sync_entity,
        kwargs=dict(
            name=request.json['name'],
            code=request.json['code'],
            month=request.json.get('month'),
            year=request.json.get('year'),
            run=True,
        )
    )
    THREAD.start()
    return 'Synchronization was started.'


if __name__ == '__main__':
    serve(APP)
