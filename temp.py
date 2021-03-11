from sqlalchemy import Table
from sqlalchemy.ext.declarative import declarative_base

from const import STACK
from core import _get_engine, _get_metadata, get_session

Base = declarative_base()
engine = _get_engine('ab')
metadata = _get_metadata(engine, 'heap')
session = get_session(engine)


class ListDatasource(Base):
    __table__ = Table('list_datasource', metadata, autoload=True)


class PersonalAccount(Base):
    __table__ = Table('personal_account', metadata, autoload=True)


def name_to_code(name):
    result = []
    for item in session.query(PersonalAccount).filter(
            PersonalAccount.personal_account_name == name):
        result.append(item.personal_account_code)
    return result


# print(name_to_code('9008005033'))


def test_return_value():
    engine = _get_engine(STACK)
    # session = get_session(engine)
    # sql = 'SELECT 1'
    # sql = 'EXECUTE crude.sp_load_datasource_meter; SELECT 1'
    # sql = 'DECLARE @i int; SET NOCOUNT ON; EXECUTE @i = crude.sp_load_datasource_meter; SET NOCOUNT OFF; SELECT @i;'
    # result = session.execute(sql)
    # print(result.fetchall())


test_return_value()


from sqlalchemy import Column, Integer, Table
from sqlalchemy.ext.declarative import declarative_base

from const import HCS
from init import metadatas

Base = declarative_base()


# class Payment(Base):
#     __table__ = Table('payment', metadatas[HCS], autoload=True)
#     id = Column(Integer, primary_key=True)
