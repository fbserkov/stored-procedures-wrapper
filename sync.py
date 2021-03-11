from datetime import date
from sqlalchemy.exc import OperationalError

from const import (
    AB, B_C, B_D, B_P, B_S, C, C_C_D, C_D, NAMES_DATED, E, HCS, NAMES_HCS_ONLY,
    M, M_P, M_R, PA, PR, P_A, P_A_M, P_A_P, P_S, RE, RO, R_B, CODES_SERVER,
    CODES_SQL01COMFORT, CODES_STACK, STACK_ZAGSER, T_B_S,
)
from core import dispose_engines, get_session
from utils import now2str


def _sync_core(database_code, command, params=None):
    print(f'{now2str()}-> - {command} {params}')
    session = get_session(database_code)
    try:
        session.execute(command, params)
        session.commit()
    except OperationalError as error:
        session.rollback()
        print(error)
    session.close()


def _sync_hcs_heap(database_code, name, code, month, year):
    if name == B_C:
        name = B_D
    export_name = 'dbo.sp_export_to_bill_ab_' + name
    if name in NAMES_DATED:
        assert month and year, 'No date!'
        command = (
            'EXECUTE ' + export_name + ' @CurDataAreaId = :code,'
            ' @period_month = :month, @period_year = :year'
        )
        params = dict(code=code, month=month, year=year)
    else:
        command = 'EXECUTE ' + export_name + ' @CurDataAreaId = :code'
        params = dict(code=code)
    _sync_core(database_code, command, params)


def _sync_stack_prep(name, code, month):
    if code == STACK_ZAGSER:
        export_name = 'prep.sp_export_to_prep_' + name
    else:
        if name in [P_A_M, P_A_P, RE, T_B_S]:
            export_name = 'prep.sp_export_to_prep_' + name
        else:
            export_name = 'dbo.sp_export_to_bill_ab_' + name

    if name in NAMES_DATED:
        assert month, 'No date!'
        if name in (C_D, P_S):
            command = 'EXECUTE ' + export_name + ' @month = :month'
        else:
            command = 'EXECUTE ' + export_name + ' @date_of_month = :month'
        params = dict(month=month)
    else:
        command = 'EXECUTE ' + export_name
        if name == P_A_P:
            line = 'SET FORCEPLAN'
            command = f'{line} ON; {command}; {line} OFF;'
        params = None
    _sync_core(code, command, params)


def _sync_ab_crude(name):
    command = 'EXECUTE crude.sp_load_datasource_' + name
    _sync_core(AB, command)


def _sync_ab_heap(name):
    command = 'EXECUTE heap.sp_load_to_heap_from_crude_' + name
    _sync_core(AB, command)


def _full_sync(name, code, month=None, year=None):
    if code in CODES_STACK:
        if month:
            month = date(year, month, 1).strftime('%Y%m%d')
        _sync_stack_prep(name, code, month)
    else:
        _sync_hcs_heap(HCS, name, code, month, year)

    _sync_ab_crude(name)
    _sync_ab_heap(name)


def _check_prep(name, code):
    if code in CODES_SERVER:
        session = get_session(code)
        command = (
            'SELECT TOP(1) date_modification '
            f'FROM prep.{name} '
            'ORDER BY date_modification DESC'
        )
        params = None
    elif code in CODES_SQL01COMFORT:
        session = get_session(code)
        command = (
            'SELECT TOP(1) date_modification '
            f'FROM prep.{name} '
            'ORDER BY date_modification DESC'
        )
        params = None
    else:
        session = get_session(HCS)
        if name == B_C:
            name = B_D
        if name in [B_D, B_P, C, E, PR, RO]:
            # load simultaneously for all data areas
            command = (
                'SELECT TOP(1) date_modification '
                f'FROM heap.{name} '
                'ORDER BY date_modification DESC'
            )
            params = None
        else:
            command = (
                'SELECT TOP(1) date_modification '
                f'FROM heap.{name} '
                'WHERE bill_datasource_section = :code '
                'ORDER BY date_modification DESC'
            )
            params = dict(code=code)
    result = session.execute(command, params)
    row = result.fetchone()
    if row is None:  # str() + ' - ' +
        print(f'->{now2str()} - check_prep - no value')
    else:
        print(f'->{now2str()} - check_prep - {row[0]}')
    session.close()


def _check_crude(name, code):
    if name in (C, P_A):  # no date_load field
        print(f'->{now2str()} - check_crude - no value')
        return

    command = (
        'SELECT TOP(1) date_load '
        f'FROM crude.{name} AS c '
        'JOIN heap.list_datasource as l '
        'ON c.datasource_id = l.list_datasource_id '
        'WHERE l.datasource_section = :code '
        'ORDER BY c.date_load DESC'
    )
    params = dict(code=code)
    session = get_session(AB)
    result = session.execute(command, params)
    row = result.fetchone()
    if row is None:
        print(f'->{now2str()} - check_crude - no value')
    else:
        print(f'->{now2str()} - check_crude - {row[0]}')
    session.close()


def _check_heap(name, code):
    if name in (C_C_D, C_D, P_A_P, T_B_S):
        command = (
            'SELECT TOP(1) tbs.date_modification '
            f'FROM heap.{name} AS tbs '
            'JOIN heap.personal_account AS pa '
            'ON tbs.personal_account_id = pa.personal_account_id '
            'JOIN heap.list_datasource as ds '
            'ON pa.datasource_id = ds.list_datasource_id '
            'WHERE ds.datasource_section = :code '
            'ORDER BY tbs.date_modification DESC'
        )
    elif name in (B_P, C):
        command = (
            'SELECT TOP(1) date_modification '
            f'FROM heap.{name} '
            'ORDER BY date_modification DESC'
        )
    elif name == P_S:
        command = (
            'SELECT TOP(1) date_modification '
            f'FROM test.{name} AS h '
            'JOIN heap.list_datasource as l '
            'ON h.datasource_id = l.list_datasource_id '
            'WHERE l.datasource_section = :code '
            'ORDER BY h.date_modification DESC'
        )
    else:
        command = (
            'SELECT TOP(1) date_modification '
            f'FROM heap.{name} AS h '
            'JOIN heap.list_datasource as l '
            'ON h.datasource_id = l.list_datasource_id '
            'WHERE l.datasource_section = :code '
            'ORDER BY h.date_modification DESC'
        )
    params = dict(code=code)
    session = get_session(AB)
    result = session.execute(command, params)
    row = result.fetchone()
    if row is None:
        print(f'->{now2str()} - check_heap - no value')
    else:
        print(f'->{now2str()} - check_heap - {row[0]}')
    session.close()


def _full_check(name, code):
    _check_prep(name, code)
    _check_crude(name, code)
    _check_heap(name, code)


def sync_entity(name, code, month=None, year=None, run=False):
    if not run:
        return
    print(f'{now2str()}-> - START [{code}, {month}, {year}]')
    _full_check(name, code)
    _full_sync(name, code, month, year)
    _full_check(name, code)
    print(f'->{now2str()} - STOP {name}')
    dispose_engines()
    print()


def _run(name, code):
    return not (name in NAMES_HCS_ONLY and code in CODES_STACK)


def sync_data_source(code, month=None, year=None, run=False):
    if not run:
        return

    # Scheme 1
    # load_entity(A_D)
    sync_entity(B_C, 'all', run=_run(B_C, code))
    sync_entity(B_P, 'all', run=_run(B_P, code))
    sync_entity(B_S, code, run=_run(B_S, code))
    sync_entity(C, 'all', run=_run(C, code))
    sync_entity(E, 'all', run=_run(E, code))
    sync_entity(M, code, run=_run(M, code))
    sync_entity(M_P, code, run=_run(M_P, code))
    sync_entity(PR, 'all', run=_run(PR, code))
    sync_entity(P_A, code, run=_run(P_A, code))  # After PR in STACK!
    sync_entity(P_A_M, code, run=_run(P_A_M, code))
    sync_entity(P_A_P, code, run=_run(P_A_P, code))
    sync_entity(RO, 'all', run=_run(RO, code))

    # Scheme 2
    sync_entity(M_R, code, month, year, run=_run(M_R, code))
    sync_entity(PA, code, month, year, run=_run(PA, code))

    # Scheme 3
    sync_entity(C_C_D, code, month, year, run=_run(C_C_D, code))
    sync_entity(C_D, code, month, year, run=_run(C_D, code))
    sync_entity(P_S, code, month, year, run=_run(P_S, code))
    sync_entity(RE, code, month, year, run=_run(RE, code))
    sync_entity(R_B, code, month, year, run=_run(R_B, code))
    sync_entity(T_B_S, code, month, year, run=_run(T_B_S, code))
