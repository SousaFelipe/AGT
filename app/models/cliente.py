from api.connection import Connection


class Cliente(Connection):

    def __init__(self):
        super().__init__('cliente')
