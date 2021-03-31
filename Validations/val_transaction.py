from Operations.create_account import *
from Entities.violations import Violation
from Operations.transaction_history import *
from Operations.create_account import *
from Entities.account import Account
from Operations import violations_list

def entry_point():
    my_account = Account(True, 0)
    return my_account

def set_disponible():
    my_account = entry_point()
    amount = last_amount_list[0]
    if amount > my_account.availableLimit:
        return Violation.violations_dict['amount']
    elif amount <= my_account.availableLimit and len(violations_list.list_violations) == 0:
        my_account.availableLimit = amount
        
def status_card():
    my_account = entry_point()
    if my_account.activeCard == False:
        return Violation.violations_dict['status']
    else:
        return True

def double_transaction():
    my_account = entry_point()
    if len(last_amount_list) > 1 and len(last_merchant_list) > 1:
        validation_merchant = last_merchant_list[0] == last_merchant_list[1]
        validation_amount = last_amount_list[0] == last_amount_list[1]
        if validation_amount == validation_merchant and my_account.activeCard == True:
            return Violation.violations_dict['purchase']
        