import math
import sys


from api.connection import Connection
from api.response import Response
from app.excel import Excel
from app.terminal import terminal


def do_print(data: Response):
    for record in data.get_records():
        print(record['login'])


def loop(table: str):
    params: str = sys.argv[3]
    action: str = sys.argv[4]
    connection = Connection(table)

    print('\nPreparing to READ data in table "{}"...\n'.format(table))

    for conditon in params.split(','):
        cmd = terminal(conditon)
        connection.where(column=cmd['c'], operator=cmd['o'], value=cmd['v'])

    pg_numb: int = 1
    pg_data = connection.read(page=pg_numb)

    if pg_data.get_total() > 0:
        page_total = math.ceil(pg_data.get_total() / 20)

        if action == 'show':
            do_print(data=pg_data)
            while pg_numb < page_total:
                pg_data = connection.read(page=pg_numb + 1)
                if action == 'show':
                    do_print(data=pg_data)
                pg_numb += 1

        elif action == 'store':
            excel = Excel(headers=sys.argv[5].split(','))
            excel.add(data=pg_data.get_records())
            while pg_numb < page_total:
                pg_data = connection.read(page=pg_numb + 1)
                excel.add(data=pg_data.get_records())
                pg_numb += 1
            excel.save(sheet=table)
