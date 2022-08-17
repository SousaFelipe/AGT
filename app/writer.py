import math

from api.connection import Connection
from api.status import Status
from app.terminal import terminal



def loop(table: str) -> list:
    output: list = []
    source: list = []

    print('WHERE\'s (separados por vírgula):', end=' ')
    params: str = str(input())

    print('UPDATE\'s (separados por vírgula):', end=' ')
    values: str = str(input())

    r_connection = Connection(table=table)
    w_connection = Connection(table=table)

    for conditon in params.split(','):
        cmd: dict[str, str] = terminal(conditon)
        r_connection.where(column=cmd['field'], operator=cmd['operator'], value=cmd['value'])

    pg_numb: int = 1
    pg_data = r_connection.read(page=pg_numb)

    if pg_data.get_total() > 0:
        page_total = math.ceil(pg_data.get_total() / 20)

        for record in pg_data.get_records():
            source.append(record)

        while pg_numb < page_total:
            pg_data = r_connection.read(page=pg_numb + 1)
            for record in pg_data.get_records():
                source.append(record)
            pg_numb += 1

    r_connection = Connection(table=table)

    for item in source:
        for value in values.split(','):
            cmd: dict[str, str] = terminal(value)
            item[cmd['field']] = cmd['value']

        status: Status = w_connection.update(target=item['id'], payload=item)

        if status.is_ok():
            output.append(r_connection.find(item['id']))
        else:
            print('\nOcorreu um erro ao ATUALIZAR o registro de número: "{}"!'.format(item['id']))
            print('IXC [{}]: {}\n'.format(status.get_type(), status.get_message()))

    return output
