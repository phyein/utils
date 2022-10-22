from typing import Union

def get_credentials(env_var:str=None, domain:str=None) -> dict:
    '''
    Gets user credentials via the following methods:

    ENVIRONMENT VARIABLE (RECOMMENDED)
        get_credentials(env_var='VARIABLE') reads an environment variable.
        The variable must be formatted as a Python dictionary:
            "{'username':'YOUR_USERNAME', 'password':'YOUR_PASSWORD'}"

    DOMAIN AUTHENTICATION
        get_credentials(domain='DOMAIN') to get username from system.
        User will be prompted for password.

    MANUAL AUTHENTICATION
        If authentication method not specified or fails user
        will be prompted to manually input credentials.
    '''

    from ast import literal_eval
    from getpass import getpass,getuser
    from os import getenv

    try:

        if env_var != None:
            # ENVIRONMENT VARIABLE AUTHENTICATION
            credentials = literal_eval(getenv(env_var))
            uid = credentials['username']
            key = credentials['password']

        elif domain != None:
            # DOMAIN AUTHENTICATION
            uid = domain + getuser()
            key = getpass('Password for current user: ')

        else: raise Exception()
        
    except:
        # MANUAL AUTHENTICATION
        uid = input('Username: ')
        key = getpass('Password: ')

    credentials = {
        'username': uid,
        'user': uid,
        'uid': uid,
        'password': key,
        'pass': key,
        'key': key,
        }
    
    return credentials

def prompt_choice(options:Union[dict, list, tuple]) -> tuple:
    '''
    Presents multiple choice prompt to user.
    '''

    # convert lists & tuples to dictionary
    if type(options) == dict: pass
    if type(options) == list or type(options) == tuple:
        options = {i+1:item for i,item in enumerate(options)}

    # convert all keys,values to strings
    options = {str(key):str(value) for key,value in options.items()}

    # prompt user
    while True:
        print('Select one: ')
        for key,value in options.items():
            print(key + '. ' + value)
        
        print('----------------')
        
        choice = str(input())
        
        if choice in options.keys(): break
        if choice == 'exit': return 'exit'
        else: print('\nInvalid. Retry or input "exit" to exit.')

    return (choice, options[choice])

def indicate_progress(i:int, total:int) -> None:
    print(f'{100*i//total}%', end='\r')

class color:
    '''
    Print colored text.

    Examples
    --------
    - colors.[fore/back]ground.colorname
    - color.bg.black
    '''

    reset='\033[0m'
    bold='\033[01m'
    disable='\033[02m'
    underline='\033[04m'
    reverse='\033[07m'
    strikethrough='\033[09m'
    invisible='\033[08m'

    class fg:
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'

    class bg:
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'

