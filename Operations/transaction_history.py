from Entities.transaction import Transaction
from Operations import violations_list

"""[summary]
    Modulo que procesa la petición de una nueva transaccion
"""
transaction_list = list()
last_amount_list = list()
last_merchant_list = list()
last_time_list = list()

def new_transaction(params: list):
    """[summary]
    Funcion que procesa la ejecucion de una nueva transaccion
    Args:
        params (list): [Recibe una lista de parametros claves para generar la transaccion]

    Returns:
        [Transaction]: [Retorna un objeto de tipo Transaction]
    """
    merchant, amount, time = params
    transaction = Transaction(merchant, amount, time)
    if len(violations_list.list_violations) == 0:
        transaction_list.append(transaction)
        last_amount_list.insert(0, amount)
        last_merchant_list.insert(0, merchant)
        last_time_list.insert(0, time)
    violations_list.violations_transaction()
    return transaction
