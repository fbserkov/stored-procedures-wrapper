from urllib.parse import quote_plus

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import MetaData

from config import DATABASES, USER
from const import AB, HCS, HEAP, STACK, STACK_MO, STACK_REGION, STACK_ZAGSER


def _get_engine(database):
    server = DATABASES[database]['host']
    database = DATABASES[database]['name']
    login = USER['login']
    password = USER['password']

    engine = None
    driver = 'pymssql'
    if driver == 'pyodbc':
        # https://docs.sqlalchemy.org/en/13/dialects/mssql.html#pass-through-exact-pyodbc-string
        params = quote_plus(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            f'SERVER={server};DATABASE={database};UID={login};PWD={password}'
        )
        engine = create_engine('mssql+pyodbc:///?odbc_connect=' + params)
    if driver == 'pymssql':
        # https://docs.sqlalchemy.org/en/13/dialects/mssql.html#module-sqlalchemy.dialects.mssql.pymssql
        engine = create_engine(
            f'mssql+pymssql://{login}:{password}@{server}/{database}')
    return engine


ENGINES = {
    AB: _get_engine(AB),
    HCS: _get_engine(HCS),
    STACK: _get_engine(STACK),
    STACK_MO: _get_engine(STACK_MO),
    STACK_REGION: _get_engine(STACK_REGION),
    STACK_ZAGSER: _get_engine(STACK_ZAGSER),
}


def _get_metadata(engine, schema):
    metadata = MetaData(bind=engine, schema=schema)
    return metadata


METADATAS = {
    HCS: _get_metadata(ENGINES[HCS], HEAP),
}


def get_session(database_code):
    engine = ENGINES[database_code]
    Session = sessionmaker(bind=engine)
    return Session()


def dispose_engines():
    for key in ENGINES:
        ENGINES[key].dispose()
