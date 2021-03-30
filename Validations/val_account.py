from Operations import create_account
from Entities.violations import Violation
from Entities.account import Account

def is_already_initialized():
    account_list = create_account.verify()
    if len(account_list) > 1:
        return Violation.violations_dict['account']