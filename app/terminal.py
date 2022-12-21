

def get_operator(param: str) -> str:

    if param.__contains__('>'):
        if param.__contains__('>='):
            return '>='
        return '>'

    elif param.__contains__('<'):
        if param.__contains__('<='):
            return '<='
        return '<'

    elif param.__contains__('!='):
        return '!='

    elif param.__contains__('?'):
        return 'L'

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
    cmd = cmd.lstrip().rstrip()
    return {
        'field':    get_column(cmd),
        'operator': get_operator(cmd),
        'value':    get_value(cmd).replace('"', '')
    }
