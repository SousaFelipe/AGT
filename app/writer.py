import math
import sys

from api.connection import Connection
from api.response import Response
from app.excel import Excel
from app.terminal import terminal



def loop(table: str):
    params: str = sys.argv[3]
    values: str = sys.argv[4]
    action: str = sys.argv[5]

    r_connection = Connection(table)
    w_connection = Connection(table)

    print('\nPreparing to UPDATE data in table "{}"...\n'.format(table))

    for value in values.split(','):
        cmd: dict[str, str] = terminal(value)
        r_connection.where(column=cmd['c'], operator='!=', value=cmd['v'])

    for conditon in params.split(','):
        cmd: dict[str, str] = terminal(conditon)
        r_connection.where(column=cmd['c'], operator=cmd['o'], value=cmd['v'])

    pg_numb: int = 1
    pg_data = r_connection.read(page=pg_numb)

    if pg_data.get_total() > 0:
        page_total = math.ceil(pg_data.get_total() / 20)
        while pg_numb < page_total:
            status = w_connection.update(target=)
