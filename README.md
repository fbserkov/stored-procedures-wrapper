# stored-procedures-wrapper
Обёртка на языке Python для хранимых процедур агрегатной базы биллинга.
Для запуска хранимых процедур можно использовать board.py или web-API.

## Драйвер SQL Python
Для работы скрипта на компьютере пользователя должен быть установлен драйвер
SQL Python:
[инструкция](https://docs.microsoft.com/ru-ru/sql/connect/python/python-driver-for-sql-server?view=sql-server-2017)
(Microsoft). Здесь используется `pymssql`.

## board.py
Файл содержит перечень вызовов для синхронизации. Для активизации вызова
необходимо добавить параметр `run = True`.

### load_entity()
Функция используется для синхронизации отдельных сущностей (таблиц).

### load_data_source()
Этот файл используется для синхронизацию отдельных областей данных. Для СТЕК
под понятием области данных подразумевается конкретная БД того или иного СТЕК.

## Перенос файлов проекта на сервер

    scp <file> user@<server>:/home/user/spw

## Запуск web-сервера

Запуск сервера разработки:
`FLASK_APP=webapi.py FLASK_ENV=development flask run`  
Запуск рабочего сервера в фоновом режиме с дополнением журналов:
`python webapi.py >> stdout.log 2>> stderr.log &`  
Останов рабочего сервера: `kill <pid>` (идентификатор провесса `pid`)
можно узнать при помощи утилиты `htop`.

## Web-API

### sync_status
`http://<ip>:<port>/sync_status`

GET-запрос возвращает текущий статус процесса синхронизации. Статус
показывает не занят ли нужный процесс. На каждом сервере разрешён только
один процесс. При обработке запроса происходит "сброс" (flush) журналов
в файлы stdout.log и stderr.log.

### valid_codes
`http://<ip>:<port>/valid_codes`

GET-запрос возвращает словарь, ключами которого являются допустимые
коды областей данных. Значения - это описания областей данных (для
отображения в выпадающем списке).

### valid_names
`http://<ip>:<port>/<code>/valid_names`

GET-запрос возвращает словарь, ключами которого являются допустимые
наименования сущностей (таблиц) для указанной области данных. Значения -
это описания сущностей (для отображения в выпадающем списке).

### is_dated
`http://<ip>:<port>/<name>/is_dated`

GET-запрос возвращает 'True', если для сущности нужно указывать дату. И
'False', если дата не играет роли.

### data_source_sync
`http://<ip>:<port>>/data_source_sync`

POST-запрос запускает синхронизацию всех сущностей (таблиц) в указанной
области данных.

### entity_sync
`http://<ip>:<port>/entity_sync`

POST-запрос запускает синхронизацию отдельной сущности (таблицы) в
указанной области данных.

### POST-запросы
В POST-запросы вкладывается JSON-структура (словарь) со следующими ключами:

- token: секретный маркер авторизации (строка)
- user: читаемый человеком идентификатор пользователя (строка),
например, serfb
- name: наименование сущности (строка), например, personal_account (не обязательно для data_source_sync)
- code: код области данных (строка), например, 0c10
- month: месяц (число), например, 7 (не обязятельно при is_dated: False)
- year: год (число), например, 2019 (не обязятельно при is_dated: False)
