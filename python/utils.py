import logging
import pandas as pd
import tomllib as toml


def main(): pass
if __name__ == '__main__': main()


def init_logger() -> None:
    '''Initialize logger.'''

    with open('logging.toml', mode='rb') as logfile:
        log_config = toml.load(logfile)

    logging.config.dictConfig(log_config)

def get_credentials(env_var: str = None) -> tuple:
    '''
    Get user credentials via the following methods:

    ENVIRONMENT VARIABLE
        get_credentials(env_var='VARIABLE') reads an environment variable.
        The variable must be formatted as a Python dictionary:
            "{'username': 'YOUR_USERNAME', 'password': 'YOUR_PASSWORD'}"

    MANUAL
        If authentication fails for any reason, user
        will be prompted to manually input credentials.
    '''

    from ast import literal_eval
    from getpass import getpass
    from os import getenv

    try:
        # ENVIRONMENT VARIABLE AUTHENTICATION
        uid, key = literal_eval(getenv(env_var)).values()
        log.info('Credentials from environment variable.')

    except:
        # MANUAL AUTHENTICATION
        uid = input('Username: ')
        key = getpass('Password: ')
        log.info('Credentials from manual entry.')

    return (uid, key)

def to_dict(
    series: dict | float | int | list | set | tuple,
    length: int = None
) -> dict:
    '''Convert value(s) to type dict.'''

    if   isinstance(series, (dict)):
        return series

    elif isinstance(series, (int, float)):
        # interpret input as mean of series
        return {i + 1: series for i in range(length)}

    elif isinstance(series, (list, set, tuple)):
        return {i + 1: item for i, item in enumerate(series)}

    else:
        raise Exception(f'Invalid type: {type(series)}')

def prompt_choice(options: dict | list | set | tuple) -> tuple:
    '''Presents multiple choice prompt to user.'''

    # convert all keys, values to dictionary of strings
    options = to_dict(options)
    options = {str(key): str(value) for key, value in options.items()}

    # prompt user
    while True:
        print('Select: ')
        for key, value in options.items():
            print(f'{key}. {value}')

        print('----------------')

        # input() waits until user presses 'enter'
        choice = str(input())

        if choice in options.keys(): break
        if choice == 'exit': return 'exit'
        else: print('\nInvalid. Retry or input "exit" to exit.')

    return (choice, options[choice])

def indicate_progress(i: int, total: int) -> None:
    '''Put this inside of an iterator.'''

    print(f'{100 * i // total}%', end='\r')

def infer_dtypes(table: pd.DataFrame) -> pd.DataFrame:
    '''Infer data types for dataframes whose values consist only of strings.'''

    return table \
            .replace(to_replace('true', 'True'), value=True) \
            .replace(to_replace('false', 'False'), value=False) \
            .apply(pd.to_numeric, errors='ignore') \
            .convert_dtypes()

class color:
    '''
    Print colored text.

    Examples
    --------
    - colors.[fore/back]ground.colorname
    - color.bg.black
    '''

    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class fg:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'
