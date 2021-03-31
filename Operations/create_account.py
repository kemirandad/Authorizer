from Entities.account import Account
from Operations.violations_list import violations_account

account_list = list()

def new_account(params: list):
    active_card, available_limit = params
    account = Account(active_card, available_limit)
    account_list.append(account)
    violations_account()
    return account

def verify(lista = account_list):
    return lista
