from Operations.create_account import *
from Entities.violations import Violation
from Operations.transaction_history import *
from Operations.create_account import *
from Entities.account import Account
from Operations import violations_list
from datetime import datetime

def entry_point():
    my_account = Account(True, 0)
    return my_account

def set_disponible():
    my_account = entry_point()
    amount = last_amount_list[0]
    if amount > my_account.availableLimit: #and len(violations_list.list_violations) == 0:
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
        if validation_amount and validation_merchant and time_validation_double() == True and my_account.activeCard != False:
            return Violation.violations_dict['time-double']
        
def time_validation_frequency():
    my_account = entry_point()
    CONST = 200000000
    
    if len(last_time_list) > 2:
        last_three_purchase = last_time_list[:3]
        for time in range(len(last_three_purchase)):
            last_three_purchase[time] = datetime.strptime(last_three_purchase[time], '%Y-%m-%dT%H:%M:%S.%fZ')
            last_three_purchase[time] = last_three_purchase[time].strftime('%Y%m%d%H%M%S%f')
        times_diff = int(last_three_purchase[0]) - int(last_three_purchase[2])
        
        if times_diff <= CONST and my_account.activeCard != False:
            return Violation.violations_dict['time_frequency']
    
def time_validation_double():
    
    CONST = 200000000
    
    if len(last_time_list) > 1:
        last_two_purchase = last_time_list[:2]
        for time in range(len(last_two_purchase)):
            last_two_purchase[time] = datetime.strptime(last_two_purchase[time], '%Y-%m-%dT%H:%M:%S.%fZ')
            last_two_purchase[time] = last_two_purchase[time].strftime('%Y%m%d%H%M%S%f')
        times_diff = int(last_two_purchase[0]) - int(last_two_purchase[1])
        
        return False if times_diff > CONST else True
