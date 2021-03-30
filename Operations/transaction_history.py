from Entities.transaction import Transaction

transaction_list = []
last_amount_list = []
last_merchant_list = []

def new_transaction(params: list):
    merchant, amount, time = params
    print(merchant)
    transaction = Transaction(merchant, amount, time)
    last_amount_list.insert(0, amount)
    last_merchant_list.insert(0, merchant)
    transaction_list.append(transaction)
    return transaction

