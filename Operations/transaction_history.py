from Entities.transaction import Transaction
from Operations import violations_list

transaction_list = list()
last_amount_list = list()
last_merchant_list = list()
last_time_list = list()

def new_transaction(params: list):
    merchant, amount, time = params
    transaction = Transaction(merchant, amount, time)
    if len(violations_list.list_violations) == 0:
        transaction_list.append(transaction)
        last_amount_list.insert(0, amount)
        last_merchant_list.insert(0, merchant)
        last_time_list.insert(0, time)
    
    violations_list.violations_transaction()
    return transaction
