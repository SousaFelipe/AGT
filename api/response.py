import json


class Response:

    def __init__(self, payload: str):
        if payload is None or payload.__contains__('</div>') or len(payload) == 0:
            self.total: int = 0
            self.records: list = []
        else:
            dataset = json.loads(payload)
            if dataset['total']:
                self.total: int = int(dataset['total'])
                self.records: list = dataset['registros']

    def get_total(self) -> int:
        return self.total

    def get_records(self) -> list:
        return self.records
