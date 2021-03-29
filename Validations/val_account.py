from Operations import create_account
from Entities.violations import Violation
from Entities.account import Account

def is_already_initialized():
    lista = create_account.verify()
    if len(lista) > 1:
        return Violation.violations_dict['account']