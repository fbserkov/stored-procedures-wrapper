from const import (
    B_C, B_P, B_S, C, C_C_D, C_D, DCDB_0C01, DCDB_0C05, DCDB_0C06, DCDB_0C08,
    DCDB_0C10, DCDB_0C20, DCDB_0C21, DCDB_0C23, DCDB_0T10, DCDB_1C10,
    DCDB_2C10, DCDB_ALL, E, M, M_P, M_R, PA, PR, P_A, P_A_M, P_A_P, P_S, R_B,
    RE, RO, STACK, STACK_MO, STACK_REGION, STACK_ZAGSER, T_B_S,
)
from sync import sync_data_source, sync_entity

# load_entity(A_D, ALL)  # no table in crude and heap

sync_entity(B_C, DCDB_ALL)  # 25.07 - 2 sec

sync_entity(B_P, DCDB_ALL)  # 25.07 - 1 sec

sync_entity(B_S, DCDB_0C01)  # 02.07 - 4 sec
sync_entity(B_S, DCDB_0C05)  # 02.07 - 4 sec
sync_entity(B_S, DCDB_0C06)  # 02.07 - 4 sec
sync_entity(B_S, DCDB_0C08)  # 02.07 - 6 sec
sync_entity(B_S, DCDB_0C10)  # 02.07 - 22 sec
sync_entity(B_S, DCDB_0C20)  # 02.07 - 13 sec
sync_entity(B_S, DCDB_0C21)  # 02.07 - 13 sec
sync_entity(B_S, DCDB_0C23)  # 28.06 - 7 sec
sync_entity(B_S, DCDB_0T10)  # 25.07 - 2 min
sync_entity(B_S, DCDB_1C10)  # 02.07 - 11 sec
sync_entity(B_S, DCDB_2C10)  # 02.07 - 6 sec

sync_entity(C, DCDB_ALL)  # 25.07 - 1 sec

sync_entity(C_C_D, DCDB_0C01, month=6, year=2019)  # 03.07 - 44 sec
sync_entity(C_C_D, DCDB_0C05, month=6, year=2019)  # 02.07 - 23 sec
sync_entity(C_C_D, DCDB_0C06, month=6, year=2019)  # 02.07 - 26 sec
sync_entity(C_C_D, DCDB_0C08, month=6, year=2019)  # 02.07 - 20 sec
sync_entity(C_C_D, DCDB_0C10, month=6, year=2019)  # 02.07 - 74 sec
sync_entity(C_C_D, DCDB_0C20, month=6, year=2019)  # 02.07 - 63 sec
sync_entity(C_C_D, DCDB_0C21, month=6, year=2019)  # 02.07 - 50 sec
sync_entity(C_C_D, DCDB_0C23, month=6, year=2019)  # 02.07 - 23 sec
sync_entity(C_C_D, DCDB_0T10, month=7, year=2019)  # 25.07 - 38 sec
sync_entity(C_C_D, DCDB_1C10, month=6, year=2019)  # 02.07 - 21 sec
sync_entity(C_C_D, DCDB_2C10, month=6, year=2019)  # 02.07 - 31 sec

sync_entity(C_D, DCDB_0C01, month=6, year=2019)  # 01.07 - 7 min
sync_entity(C_D, DCDB_0C05, month=6, year=2019)  # 01.07 - 65 sec
sync_entity(C_D, DCDB_0C06, month=6, year=2019)  # 01.07 - 66 sec
sync_entity(C_D, DCDB_0C08, month=6, year=2019)  # 01.07 - 61 sec
sync_entity(C_D, DCDB_0C10, month=6, year=2019)  # 01.07 - 11 min
sync_entity(C_D, DCDB_0C20, month=6, year=2019)  # 02.07 - 4 min
sync_entity(C_D, DCDB_0C21, month=9, year=2019)  # 17.09 - 36 min
sync_entity(C_D, DCDB_0C23, month=6, year=2019)  # 02.07 - 33 sec
sync_entity(C_D, DCDB_0T10, month=7, year=2019)  # 25.07 - 3 min
sync_entity(C_D, DCDB_1C10, month=6, year=2019)  # 02.07 - 27 sec
sync_entity(C_D, DCDB_2C10, month=6, year=2019)  # 02.07 - 45 sec
sync_entity(C_D, STACK, month=9, year=2019)  # 12.09 - 26 sec
sync_entity(C_D, STACK_MO, month=7, year=2019)  # 08.07 - 35 sec
sync_entity(C_D, STACK_REGION, month=6, year=2019)  # 02.07 - 58 sec
sync_entity(C_D, STACK_ZAGSER, month=6, year=2019)  # 04.07 - 53 sec

sync_entity(E, DCDB_ALL)  # 25.07 - 3 sec
sync_entity(E, STACK)  # 28.06 - 64 sec
sync_entity(E, STACK_MO)  # 08.07 - 9 sec
sync_entity(E, STACK_REGION)  # 28.06 - 3 min
sync_entity(E, STACK_ZAGSER)  # 28.06 - 28 sec

sync_entity(M, DCDB_0C01)  # 20.06 - 1 min
sync_entity(M, DCDB_0C08)  # 15.07 - 32 sec
sync_entity(M, DCDB_0C10)  # 08.11 - 1 min
sync_entity(M, DCDB_0T10)  # 25.07 - 32 sec
sync_entity(M, DCDB_2C10)  # 20.06 - 1 min
sync_entity(M, STACK)  # 20.06 - 1 min
sync_entity(M, STACK_MO)  # 08.07 - 11 min
sync_entity(M, STACK_REGION)  # 20.06 - 2 min
sync_entity(M, STACK_ZAGSER)  # 20.06 - 44 sec

sync_entity(M_P, DCDB_0C01)  # no value
sync_entity(M_P, DCDB_0C05)  # no value
sync_entity(M_P, DCDB_0C06)  # no value
sync_entity(M_P, DCDB_0C08)  # no value
sync_entity(M_P, DCDB_0C10)  # no value
sync_entity(M_P, DCDB_0C20)  # no value
sync_entity(M_P, DCDB_0C21)  # no value
sync_entity(M_P, DCDB_0C23)  # 28.06 - 2 sec
sync_entity(M_P, DCDB_0T10)  # 25.07 - 1 sec
sync_entity(M_P, DCDB_1C10)  # no value
sync_entity(M_P, DCDB_2C10)  # no value

sync_entity(M_R, DCDB_0C01, month=6, year=2019)  # 20.06 - 1 min
sync_entity(M_R, DCDB_0C10, month=10, year=2018)  # 08.11 - 3 min
sync_entity(M_R, DCDB_0T10, month=10, year=2019)  # 10.10 - 1 min
sync_entity(M_R, DCDB_2C10, month=9, year=2019)  # 17.09 - 3 min
sync_entity(M_R, STACK, month=8, year=2019)  # 11.11 - 3 min
sync_entity(M_R, STACK_MO, month=8, year=2019)  # 11.11 - 9 min
sync_entity(M_R, STACK_REGION, month=6, year=2019)  # 20.06 - 1 min
sync_entity(M_R, STACK_ZAGSER, month=6, year=2019)  # 01.07 - 20 sec
# STACK uploads data for three months!

sync_entity(PA, DCDB_0C01, month=6, year=2019)  # 20.06 - 1 min
sync_entity(PA, DCDB_0C05, month=1, year=2019)  # 29.08 - 2 min
sync_entity(PA, DCDB_0C06, month=6, year=2019)  # 12.07 - 15 sec
sync_entity(PA, DCDB_0C10, month=6, year=2019)  # 20.06 - 1 min
sync_entity(PA, DCDB_0T10, month=7, year=2019)  # 25.07 - 1 min
sync_entity(PA, DCDB_2C10, month=6, year=2019)  # 20.06 - 1 min
sync_entity(PA, STACK, month=6, year=2019)  # 27.08 - 43 sec
sync_entity(PA, STACK_MO, month=3, year=2019)  # 04.09 - 1 min
sync_entity(PA, STACK_REGION, month=6, year=2019)  # 27.08 - 44 sec
sync_entity(PA, STACK_ZAGSER, month=9, year=2019)  # 10.09 - 50 sec

sync_entity(PR, DCDB_ALL)  # 13.09 - 1 min
sync_entity(PR, STACK)  # 8 min (night history)
sync_entity(PR, STACK_MO)  # 08.11 - 19 min
sync_entity(PR, STACK_REGION)  # 08.11 - 3 min
sync_entity(PR, STACK_ZAGSER)  # 12.07 - 74 sec

sync_entity(P_A, DCDB_0C01)  # 22.08 - 79 sec
sync_entity(P_A, DCDB_0C05)  # 22.08 - 34 sec
sync_entity(P_A, DCDB_0C06)  # 22.08 - 40 sec
sync_entity(P_A, DCDB_0C08)  # 22.08 - 78 sec
sync_entity(P_A, DCDB_0C10)  # 14.10 - 91 sec
sync_entity(P_A, DCDB_0C20)  # 22.08 - 77 sec
sync_entity(P_A, DCDB_0C21)  # 22.08 - 20 sec
sync_entity(P_A, DCDB_0C23)  # 22.08 - 28 sec
sync_entity(P_A, DCDB_0T10)  # 22.08 - 23 sec
sync_entity(P_A, DCDB_1C10)  # 22.08 - 28 sec
sync_entity(P_A, DCDB_2C10)  # 22.08 - 17 sec
sync_entity(P_A, STACK)  # 27.06 - 14 min
sync_entity(P_A, STACK_MO)  # 08.11 - 32 min
sync_entity(P_A, STACK_REGION)  # 08.11 - 7 min
sync_entity(P_A, STACK_ZAGSER)  # 12.07 - 4 min

sync_entity(P_A_M, DCDB_0C01)  # 27.06 - 2 min
sync_entity(P_A_M, DCDB_0C05)  # 27.06 - 14 sec
sync_entity(P_A_M, DCDB_0C06)  # 27.06 - 13 sec
sync_entity(P_A_M, DCDB_0C08)  # 27.06 - 28 sec
sync_entity(P_A_M, DCDB_0C10)  # 10.07 - 12 sec
sync_entity(P_A_M, DCDB_0C20)  # 27.06 - 22 sec
sync_entity(P_A_M, DCDB_0C21)  # 27.06 - 15 sec
sync_entity(P_A_M, DCDB_0C23)  # 27.06 - 47 sec
sync_entity(P_A_M, DCDB_0T10)  # 25.07 - 53 sec
sync_entity(P_A_M, DCDB_1C10)  # 27.06 - 36 sec
sync_entity(P_A_M, DCDB_2C10)  # 27.06 - 18 sec
sync_entity(P_A_M, STACK)  # 27.06 - 29 sec
sync_entity(P_A_M, STACK_MO)  # 08.07 - 47 sec
sync_entity(P_A_M, STACK_REGION)  # 27.06 - 27 sec
sync_entity(P_A_M, STACK_ZAGSER)  # 19.08 - 21 sec

sync_entity(P_A_P, DCDB_0C01)  # 15.10 - 18 sec - no value
sync_entity(P_A_P, DCDB_0C05)  # 15.10 - 5 sec
sync_entity(P_A_P, DCDB_0C06)  # 15.10 - 5 sec
sync_entity(P_A_P, DCDB_0C08)  # 15.10 - 7 sec
sync_entity(P_A_P, DCDB_0C10)  # 15.10 - 9 sec
sync_entity(P_A_P, DCDB_0C20)  # 15.10 - 5 sec
sync_entity(P_A_P, DCDB_0C21)  # 15.10 - 13 sec - no value
sync_entity(P_A_P, DCDB_0C23)  # 15.10 - 6 sec
sync_entity(P_A_P, DCDB_0T10)  # 15.10 - 12 sec
sync_entity(P_A_P, DCDB_1C10)  # 15.10 - 5 sec
sync_entity(P_A_P, DCDB_2C10)  # 15.10 - 12 sec - no value
sync_entity(P_A_P, STACK)  # 09.07 - 12 min
sync_entity(P_A_P, STACK_MO)  # 09.07 - 29 min
sync_entity(P_A_P, STACK_REGION)  # 09.07 - 4 min
sync_entity(P_A_P, STACK_ZAGSER)  # no value

sync_entity(P_S, DCDB_0C01, month=6, year=2019)  # 27.06 - 3 min
sync_entity(P_S, DCDB_0C05, month=6, year=2019)  # 27.06 - 2 min
sync_entity(P_S, DCDB_0C06, month=6, year=2019)  # 27.06 - 2 min
sync_entity(P_S, DCDB_0C08, month=6, year=2019)  # 27.06 - 2 min
sync_entity(P_S, DCDB_0C10, month=6, year=2019)  # 27.06 - 4 min
sync_entity(P_S, DCDB_0C20, month=6, year=2019)  # 27.06 - 3 min
sync_entity(P_S, DCDB_0C21, month=6, year=2019)  # 27.06 - 2 min
sync_entity(P_S, DCDB_0C23, month=6, year=2019)  # 27.06 - 2 min
sync_entity(P_S, DCDB_0T10, month=7, year=2019)  # 25.07 - 3 min
sync_entity(P_S, DCDB_1C10, month=6, year=2019)  # 27.06 - 2 min
sync_entity(P_S, DCDB_2C10, month=6, year=2019)  # 27.06 - 3 min
sync_entity(P_S, STACK, month=6, year=2019)  # 27.06 - 23 min
sync_entity(P_S, STACK_MO, month=7, year=2019)  # 08.07 - 15 min
sync_entity(P_S, STACK_REGION, month=6, year=2019)  # 27.06 - 6 min
sync_entity(P_S, STACK_ZAGSER, month=7, year=2019)  # 27.06 - 77 sec

sync_entity(RE, DCDB_0C01, month=6, year=2019)  # 21.06 - 5 sec
sync_entity(RE, DCDB_0C05, month=6, year=2019)  # 21.06 - 4 sec
sync_entity(RE, DCDB_0C06, month=10, year=2019, run=True)  # 11.11 - 9 sec
sync_entity(RE, DCDB_0C08, month=7, year=2019)  # no value
sync_entity(RE, DCDB_0C10, month=6, year=2019)  # 21.06 - 6 sec
sync_entity(RE, DCDB_0C20, month=6, year=2019)  # 21.06 - 5 sec
sync_entity(RE, DCDB_0C21, month=6, year=2019)  # 21.06 - 6 sec
sync_entity(RE, DCDB_0C23, month=6, year=2019)  # 21.06 - 4 sec
sync_entity(RE, DCDB_0T10, month=7, year=2019)  # 25.07 - 7 sec
sync_entity(RE, DCDB_1C10, month=6, year=2019)  # 21.06 - 4 sec
sync_entity(RE, DCDB_2C10, month=6, year=2019)  # no value
sync_entity(RE, STACK, month=9, year=2019)  # 24.09 - 15 sec
sync_entity(RE, STACK_MO, month=9, year=2019)  # 24.09 - error
sync_entity(RE, STACK_REGION, month=9, year=2019)  # 24.09 - error

sync_entity(RO, DCDB_ALL)  # 25.07 - 1 sec

sync_entity(R_B, DCDB_0C01, month=6, year=2019)  # 21.06 - 2 min
sync_entity(R_B, DCDB_0C05, month=6, year=2019)  # 21.06 - 2 min
sync_entity(R_B, DCDB_0C06, month=6, year=2019)  # 21.06 - 3 min
sync_entity(R_B, DCDB_0C08, month=6, year=2019)  # 21.06 - 3 min
sync_entity(R_B, DCDB_0C10, month=6, year=2019)  # 21.06 - 2 min
sync_entity(R_B, DCDB_0C20, month=6, year=2019)  # 21.06 - 2 min
sync_entity(R_B, DCDB_0C21, month=6, year=2019)  # 21.06 - 2 min
sync_entity(R_B, DCDB_0C23, month=6, year=2019)  # 21.06 - 2 min
sync_entity(R_B, DCDB_0T10, month=7, year=2019)  # 25.07 - 5 min
sync_entity(R_B, DCDB_1C10, month=6, year=2019)  # 21.06 - 2 min
sync_entity(R_B, DCDB_2C10, month=6, year=2019)  # 21.06 - 2 min

sync_entity(T_B_S, DCDB_0C01, month=4, year=2019)  # 09.07 - 4 min
sync_entity(T_B_S, DCDB_0C05, month=4, year=2019)  # 09.07 - 6 min
sync_entity(T_B_S, DCDB_0C06, month=4, year=2019)  # 09.07 - 3 min
sync_entity(T_B_S, DCDB_0C08, month=4, year=2019)  # 09.07 - 12 min
sync_entity(T_B_S, DCDB_0C10, month=8, year=2019)  # 26.08 - 17 min
sync_entity(T_B_S, DCDB_0C20, month=7, year=2019)  # 22.07 - 6 min
sync_entity(T_B_S, DCDB_0C21, month=4, year=2019)  # 09.07 - 9 min
sync_entity(T_B_S, DCDB_0T10, month=7, year=2019)  # 25.07 - 37 min
sync_entity(T_B_S, DCDB_2C10, month=7, year=2019)  # 22.07 - 5 min
sync_entity(T_B_S, STACK, month=7, year=2019)  # 06.08 - 8 min
sync_entity(T_B_S, STACK_MO, month=7, year=2019)  # 06.08 - 8 min
sync_entity(T_B_S, STACK_REGION, month=7, year=2019)  # 06.08 - 6 min
sync_entity(T_B_S, STACK_ZAGSER, month=7, year=2019)  # 05.07 - 4 min
# STACK uploads data for three months!


sync_data_source(DCDB_0C01, month=7, year=2019)  # 04.07 - 16 min
sync_data_source(DCDB_0C05, month=7, year=2019)  # 26.07 - 29 min
sync_data_source(DCDB_0C06, month=7, year=2019)  # 04.07 - 10 min
sync_data_source(DCDB_0C08, month=7, year=2019)  # 04.07 - 35 min
sync_data_source(DCDB_0C10, month=7, year=2019)  # 08.07 - 25 min
sync_data_source(DCDB_0C20, month=7, year=2019)  # 04.07 - 19 min
sync_data_source(DCDB_0C21, month=7, year=2019)  # 04.07 - 36 min
sync_data_source(DCDB_0C23, month=7, year=2019)  # 04.07 - 26 min
sync_data_source(DCDB_0T10, month=7, year=2019)  # 25.07 - 55 min
sync_data_source(DCDB_1C10, month=7, year=2019)  # 04.07 - 21 min
sync_data_source(DCDB_2C10, month=7, year=2019)  # 04.07 - 12 min
sync_data_source(STACK, month=4, year=2019)  # 26.07 - 52 min
sync_data_source(STACK_MO, month=11, year=2019)  # 07.11 - 130 min
sync_data_source(STACK_REGION, month=7, year=2019)  # 08.07 - 29 min
sync_data_source(STACK_ZAGSER, month=4, year=2019)  # 26.07 - 21 min
