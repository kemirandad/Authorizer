import json
from Entities.account import Account
from Operations import create_account
from Validations.val_account import is_already_initialized

def deserializer():
    entry = input('Request...\n')
    data = json.loads(entry)
    result = data['account'].values()
    return result

def serializer():
    account = create_account.new_account(deserializer())
    validate = is_already_initialized()
    dict_account = {'account': {'activeCard':account.activeCard, 'availableLimit':account.availableLimit}, 'violations':[validate]}
    return dict_account

def printer():
    console = json.dumps(serializer())
    print(console)
    
if __name__ == '__main__':
    while True:
        printer()
