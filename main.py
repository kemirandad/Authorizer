import json
from Entities.account import Account
from Operations import create_account, transaction_history
from Validations.val_account import is_already_initialized
from Validations import val_transaction
from Operations import violations_list

dict_account = {}

#Retorna un diccionario
def deserializer():
    entry = input('Request...\n')
    data = json.loads(entry)
    return data

#Recibe el diccionario, toma sus valores y retorna una lista
def selector():
    result = deserializer()
    if 'account' in result:
        list_details = result['account'].values()
        serializer_account(list_details)
    elif 'transaction' in result:
        list_details = result['transaction'].values()
        serializer_transaction(list_details)

def serializer_account(list_details):
    account = create_account.new_account(list_details) 
    validations_list = violations_list.run()  
    dict_a = {'account':{ 'activeCard': account.activeCard, 'availableLimit': account.availableLimit }, 'violations':violations_list.list_violations }
    dict_account.update(dict_a)
    return account

def serializer_transaction(list_details):
    transaction = transaction_history.new_transaction(list_details)
    validations_list = violations_list.run()
    return transaction

def printer():
    my_account = val_transaction.entry_point()
    dict_a = {'account':{ 'activeCard': my_account.activeCard, 'availableLimit': my_account.availableLimit }, 'violations':violations_list.list_violations }
    console = json.dumps(dict_a)
    print(console)
    
def main():
    selector()

if __name__ == '__main__':
    while True:
        main()
        printer()