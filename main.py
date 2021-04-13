import json
from Entities.account import Account
from Operations import create_account, transaction_history
from Validations.val_account import is_already_initialized
from Validations import val_transaction
from Operations import violations_list

def deserializer():
    """[summary]
    Al ser ejecutada la funcion estara en espera de recibir una entrada en formato JSON
    valida que exista una cuenta inicialmente para realizar otras operaciones
    Returns:
        [Dict]: [Convierte la entrada en formato JSON a una variable de tipo Dict]
    """
    entry = input('\nRequest...\n')
    data = json.loads(entry)
    if len(create_account.account_list) > 0 or 'account' in data:
        return data
    print('Please, first give me an account')


def selector():
    """[summary]
    Ejecuta la funcion deserializer almacena su dato de retorno y compara si este contiene
    información para generar una cuenta o una transaccion
    Returns:
        [List]: [Lista de los values() almacenados en el diccionario recibido]
    """
    result = deserializer()
    if result != None:
        if 'account' in result:
            list_details = result['account'].values()
            serializer_account(list_details)
        elif 'activeCard' in result:
            details = result['activeCard']['active']
            print(details)
            serializer_status(details)
        elif 'transaction' in result:
            list_details = result['transaction'].values()
            serializer_transaction(list_details)

def serializer_account(list_details):
    """[summary]
    Controla la creacion de una nueva cuenta
    Args:
        list_details ([List]): [Lista con los datos necesarios para generar una nueva cuenta]

    Returns:
        [Account]: [Retorna un dato de tipo Account]
    """
    account = create_account.new_account(list_details)
    
    dict_a = {'account':{ 'activeCard': account.activeCard, 'availableLimit': account.availableLimit }, 'violations':violations_list.list_violations }
    return account

#recibe una lista con unico valor
def serializer_status(details):
    status_card = details
    create_account.change_status(status_card)

def serializer_transaction(list_details):
    """[summary]
    Controla la ejecucion de una nueva transaccion
    Args:
        list_details ([List]): [Lista con los datos necesarios para que se produzca 
        una nueva transaccion]

    Returns:
        [Transaction]: [Retorna un dato de tipo Transaction]
    """
    violations_list.violation_status()
    transaction = transaction_history.new_transaction(list_details)
    return transaction

def printer():
    """[summary]
    Se ocupa de mostrar la informacion pertinente por consola stdout
    """
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