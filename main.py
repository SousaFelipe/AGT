import sys

from api.connection import Connection
from app.terminal import terminal


def read():
    table: str = sys.argv[2]
    params: str = sys.argv[3]
    connection = Connection(table)

    print('Preparing to {} data in table "{}"...'.format(command, table))

    conditions: list = params.split(',')

    for conditon in conditions:
        cmd = terminal(conditon)
        connection.where(column=cmd['c'], operator=cmd['o'], value=cmd['v'])

    first_read = connection.read()

    for record in first_read.get_records():
        print(record['login'])


if __name__ == '__main__':

    command: str = sys.argv[1]

    if command == 'read':
        read()
