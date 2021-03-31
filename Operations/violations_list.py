from Validations.val_account import is_already_initialized
from Validations.val_transaction import status_card, set_disponible, double_transaction, entry_point, time_validation_double, time_validation_frequency
from Entities.violations import Violation
from Entities.account import Account
from dataclasses import dataclass
from Operations import create_account, transaction_history

list_violations = []

def violations_account():
    if len(create_account.account_list) > 0:
        violation_account_exist()

def violations_transaction():
    #if len(transaction_history.transaction_list) > 0:
    violation_status()
    violation_double()
    violation_limit()
    
        
def violation_account_exist(lista = list_violations):
    already_exist = is_already_initialized()
    if already_exist != None:
        lista.append(already_exist) 
    return lista
        
def violation_limit(lista = list_violations):
    status = status_card()
    if status == True:
        without_limit = set_disponible()
        if without_limit != None:
            lista.append(without_limit)
        return lista

def violation_status(lista = list_violations):
    status = status_card()
    if status != True:
        lista.append(status)
    return lista

def violation_double(lista = list_violations):
    double_purchase = double_transaction()
    if double_purchase != None:
        lista.append(double_purchase)
    return lista

def violation_frequency(lista = list_violations):
    high_frequency = time_validation_double()
    if high_frequency != None:
        lista.append(high_frequency)
    return lista
