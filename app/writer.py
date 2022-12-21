import math

from api.connection import Connection
from api.status import Status
from app.terminal import terminal


def update(table: str, source: list):
    print('UPDATE\'s (separados por vírgula):', end=' ')
    values: str = str(input())
    output: list = []

    r_connection = Connection(table=table)
    w_connection = Connection(table=table)

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


def loop(table: str, replace: str | None = None) -> list:
    source: list = []

    print('WHERE\'s (separados por vírgula):', end=' ')
    params: str = str(input())

    first_conn = Connection(table=table)

    for conditon in params.split(','):
        cmd: dict[str, str] = terminal(conditon)
        first_conn.where(column=cmd['field'], operator=cmd['operator'], value=cmd['value'])

    pg_numb: int = 1
    pg_data = first_conn.read(page=pg_numb)

    if pg_data.get_total() > 0:
        page_total = math.ceil(pg_data.get_total() / 20)

        if replace is None:
            for record in pg_data.get_records():
                source.append(record)

            while pg_numb < page_total:
                pg_data = first_conn.read(page=pg_numb + 1)
                for record in pg_data.get_records():
                    source.append(record)
                pg_numb += 1

        else:
            col_target_repl: str = replace.split('=')[0]
            source_repl: str = replace.split('=')[1]
            tab_source_repl: str = source_repl.split('.')[0]
            col_source_repl: str = source_repl.split('.')[1]

            merge_conn = Connection(table=tab_source_repl)

            for record in pg_data.get_records():
                merge = merge_conn.find(record[col_target_repl])
                record[col_target_repl] = merge[col_source_repl]
                source.append(record)

            while pg_numb < page_total:
                pg_data = first_conn.read(page=pg_numb + 1)
                for record in pg_data.get_records():
                    merge = merge_conn.find(record[col_target_repl])
                    record[col_target_repl] = merge[col_source_repl]
                    source.append(record)
                pg_numb += 1

    return source
