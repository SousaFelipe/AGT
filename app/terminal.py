

def get_operator(param: str) -> str:
    if param.__contains__('>'):
        return '>'
    elif param.__contains__('<'):
        return '<'
    elif param.__contains__('!='):
        return '!='
    elif param.__contains__('!!'):
        return 'LE'
    return '='


def get_column(param: str) -> str:
    spl_params: list[str] = param.split(get_operator(param))
    if len(spl_params) == 2:
        return spl_params[0]
    return 'id'


def get_value(param: str) -> str:
    spl_params: list[str] = param.split(get_operator(param))
    if len(spl_params) == 2:
        return spl_params[1]
    return '0'


def terminal(cmd: str):
    return {
        'c': get_column(cmd),
        'o': get_operator(cmd),
        'v': get_value(cmd)
    }
