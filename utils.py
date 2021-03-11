from config import DCDB, SERVER, SQL01COMFORT
from const import CODES_DCDB, CODES_SERVER, CODES_SQL01COMFORT

from datetime import datetime
from sys import stderr, stdout


def flush_std():
    stderr.flush()
    stdout.flush()


def get_server_name(code):
    if code in CODES_DCDB:
        return DCDB
    if code in CODES_SERVER:
        return SERVER
    if code in CODES_SQL01COMFORT:
        return SQL01COMFORT


def now2str():
    return datetime.now().strftime('%d.%m.%Y %H:%M:%S')
