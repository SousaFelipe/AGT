import os
import pandas as pd


MAIN_PATH: str = os.path.expanduser('~\\Documents')


class Excel:

    def __init__(self, headers: list[str]):
        self.headers: list[str] = headers
        self.data: list[list[str]] = []
        self.size: int = 0

    def add(self, data: list[dict]):
        row: list[str] = []

        for item in data:
            for header in self.headers:
                row.append(item[header])
            self.data.append(row)
            self.size += 1
            row = []

    def save(self, sheet: str):
        filename: str = '{}\\{}.xlsx'.format(MAIN_PATH, sheet)
        df = pd.DataFrame(
            data=self.data,
            columns=self.headers
        )
        df.to_excel(
            excel_writer=filename,
            sheet_name=sheet
        )
        print('{} Linhas salvas no arquivo "{}"'.format(self.size, filename))
