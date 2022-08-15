import requests
import base64
import json

from api.response import Response
from api.status import Status



URI = 'https://agilityquixeramobim.com.br/webservice/v1'
TOKEN = '6:d94f8ccff332c49a266088ea3e0afaa2bdac77157bc4c698d7ab7e35971192bd'.encode('utf-8')
AUTHORIZATION = 'Basic {}'.format(base64.b64encode(TOKEN).decode('utf-8'))



def headers(request: str = ''):
    return {
        'ixcsoft': request,
        'Authorization': AUTHORIZATION,
        'Content-Type': 'application/json'
    }



class Connection:


    def __init__(self, table: str):
        self.table: str = table
        self.grid: list = []


    def where(self, column: str, operator: str, value: any):
        self.grid.append({
            'TB': '{}.{}'.format(self.table, column),
            'OP': operator,
            'P': value
        })


    def create(self, payload: dict) -> Status:
        response = requests.post(
            url='{}/{}'.format(URI, self.table),
            data=json.dumps(payload),
            headers=headers()
        )
        return Status(response.text)


    def read(self, page: int = 1, rows: int = 20, sort_name: str = 'id', sort_order: str = 'asc') -> Response:
        payload: object = {
            'qtype': self.table,
            'query': '',
            'oper': '',
            'page': page,
            'rp': rows,
            'sortname': '{}.{}'.format(self.table, sort_name),
            'sortorder': sort_order,
            'grid_param': json.dumps(self.grid)
        }
        response = requests.post(
            url='{}/{}'.format(URI, self.table),
            data=json.dumps(payload),
            headers=headers('listar')
        )
        return Response(response.text)


    def update(self, target: int | str, payload: dict) -> Status:
        response = requests.put(
            url='{}/{}/{}'.format(URI, self.table, target),
            data=json.dumps(payload),
            headers=headers()
        )
        return Status(response.text)


    def detele(self):
        pass
