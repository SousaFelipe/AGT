import math

from api.connection import Connection
from app.terminal import terminal


def loop(table: str) -> list:
    output: list = []

    print('WHERE\'s (separadas por vírgula):', end=' ')
    params: str = str(input())

    r_connection = Connection(table)

    for conditon in params.split(','):
        cmd = terminal(conditon)
        r_connection.where(column=cmd['field'], operator=cmd['operator'], value=cmd['value'])

    pg_numb: int = 1
    pg_data = r_connection.read(page=pg_numb)

    if pg_data.get_total() > 0:
        page_total = math.ceil(pg_data.get_total() / 20)

        for record in pg_data.get_records():
            output.append(record)

        while pg_numb < page_total:
            pg_data = r_connection.read(page=pg_numb + 1)
            for record in pg_data.get_records():
                output.append(record)
            pg_numb += 1

    return output
