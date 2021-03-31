import json
from Entities.account import Account
from Operations import create_account, transaction_history
from Validations.val_account import is_already_initialized
from Validations import val_transaction
from Operations import violations_list

#Retorna un diccionario
def deserializer():
    entry = input('\nRequest...\n')
    data = json.loads(entry)
    if len(create_account.account_list) > 0 or 'account' in data:
        return data
    print('Please, first give me an account')


#Recibe el diccionario, toma sus valores y retorna una lista
def selector():
    result = deserializer()
    if result != None:
        if 'account' in result:
            list_details = result['account'].values()
            serializer_account(list_details)
        elif 'transaction' in result:
            list_details = result['transaction'].values()
            serializer_transaction(list_details)

def serializer_account(list_details):
    account = create_account.new_account(list_details) 
    dict_a = {'account':{ 'activeCard': account.activeCard, 'availableLimit': account.availableLimit }, 'violations':violations_list.list_violations }
    return account

def serializer_transaction(list_details):
    transaction = transaction_history.new_transaction(list_details)
    return transaction

def printer():
    if len(create_account.account_list) > 0:
        my_account = val_transaction.entry_point()
        dict_a = {'account':{ 'activeCard': my_account.activeCard, 'availableLimit': my_account.availableLimit }, 'violations':violations_list.list_violations }
        console = json.dumps(dict_a)
        print(f'\n{console}')
        
        
def clear_list_violations():
    violations_list.list_violations.clear()
    
def main():
    selector()

if __name__ == '__main__':
    while True:
        main()
        printer()
        clear_list_violations()