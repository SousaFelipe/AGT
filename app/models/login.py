from api.connection import Connection


class Login(Connection):

    def __init__(self):
        super().__init__('radusuarios')
