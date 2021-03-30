from Operations.create_account import *
from Entities.violations import Violation
from Operations.transaction_history import *
from Operations.create_account import *
from Entities.account import Account

def entry_point():
    my_account = Account(True, 0)
    return my_account

def limit_disponible():
    my_account = entry_point()
    amount = last_amount[0]    
    if amount > my_account.availableLimit:
        return Violation.violations_dict['amount']
    else:
        my_account.availableLimit = amount
        
def inactive_card():
    my_account = entry_point()
    if my_account.activeCard == False:
        return Violation.violations_dict['status']

def double_transaction():
    pass