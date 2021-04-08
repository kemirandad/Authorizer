from Operations import create_account
from Entities.violations import Violation
from Entities.account import Account

"""[summary]
    Modulo controlador de las operaciones ejecutadas mediante la creacion de cuentas
"""
def is_already_initialized():
    """[summary]
    Verifica si existen cuentas creadas a través de la dimension de la lista
    account_list
    Returns:
    [String]: [Retorna un valor del diccionario de violaciones si no se puede crear la cuenta]
    """
    account_list = create_account.verify()
    if len(account_list) > 1:
        return Violation.violations_dict['account']
    