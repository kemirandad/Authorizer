from Validations.val_account import is_already_initialized
from Validations.val_transaction import inactive_card, limit_disponible
from Entities.violations import Violation
from Entities.account import Account
from dataclasses import dataclass
from Operations import create_account, transaction_history


list_violations = []

def violations_account():
    if len(create_account.account_list) != False:
        violation_account_exist()

def violations_transaction():
    if len(transaction_history.transaction_list) != False:
        violation_status()
        violation_limit()
        
def violation_account_exist(lista = list_violations):
    already_exist = is_already_initialized()
    if already_exist != None:
        lista.append(already_exist) 
    return lista
        
def violation_limit(lista = list_violations):
    without_limit = limit_disponible()
    if without_limit != None:
        lista.append(without_limit)
    return lista

def violation_status(lista = list_violations):
    status_false = inactive_card()
    if status_false != None:
        lista.append(status_false)
    return lista
    
def run():
    list_violations.clear()
    violations_account()
    violations_transaction()
