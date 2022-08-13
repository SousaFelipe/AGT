import json



class Status:


    def __init__(self, payload: str):
        if payload is None or payload.__contains__('</div>') or len(payload) == 0:
            self.type: str = 'error'
            self.message: str = 'Ocorreu um erro na requisição'
        else:
            dataset = json.loads(payload)
            if dataset['type']:
                self.type: str = dataset['type']
            if dataset['message']:
                self.message: str = dataset['message']


    def get_type(self):
        return self.type


    def get_message(self):
        return self.message


    def is_ok(self):
        return self.type and self.type == 'success'
