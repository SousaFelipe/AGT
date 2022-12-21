import sys

import app.writer

from app.excel import Excel


def show(dataset: list):
    print('SELECT\'s (separados por vírgula):', end=' ')
    fields: str = str(input())
    field_list: list[str] = fields.split(',')

    current_item: str = ''
    for item in dataset:
        for field in field_list:
            current_item = current_item + '- {} '.format(item[field])
        print(current_item)
        current_item = ''


def store(dataset: list):
    print('\nPlanilha...')
    print('COLUNAS:', end=' ')
    headers: str = str(input())
    header_list: list[str] = headers.split(',')

    print('\nSalvar como...')
    print('Nome do arquivo:', end=' ')
    filename: str = str(input())

    excel = Excel(headers=header_list)
    excel.add(data=dataset)
    excel.save(sheet=filename)


if __name__ == '__main__':

    command: str = sys.argv[1]
    target: str = sys.argv[2]

    print('\n')

    if len(sys.argv) > 4 and sys.argv[3] == 'REPLACE':
        data: list = app.writer.loop(table=target, replace=sys.argv[4])
    else:
        data: list = app.writer.loop(table=target)

    if len(data) > 0:

        if command == 'VIEW':
            show(dataset=data)

        elif command == 'SAVE':
            store(dataset=data)
