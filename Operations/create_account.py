from Entities.account import Account

account_list = list()

def new_account(params: list):
    active_card, available_limit = params
    account = Account(active_card, available_limit)
    account_list.append(account)
    return account

def verify(lista = account_list):
    return lista
