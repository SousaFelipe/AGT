

def format_date(date: str) -> str:
    if date is None or len(date) < 10:
        return ''
    if date.__contains__('-'):
        splited: list = date.split('-')
        reverse: list = splited[::-1]
        return '/'.join(reverse)
    return date
