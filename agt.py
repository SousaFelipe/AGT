import sys

import app.reader
import app.writer


if __name__ == '__main__':

    command: str = sys.argv[1]

    if command == 'read':
        app.reader.loop(table=sys.argv[2])

    if command == 'update':
        app.writer.loop(table=sys.argv[2])
