from Entities.account import Account
from Operations.violations_list import violations_account
from Validations.val_transaction import entry_point

"""[summary]
    Modulo que procesa la creación de la cuenta
"""
account_list = list()


def new_account(params: list):
    """[summary]
    Funcion que crea una nueva cuenta
    Args:
        params (list): [Recibe una lista de parametros claves para crear la cuenta]

    Returns:
        [Account]: [Retorna un objeto de tipo Account]
    """
    if len(params) == 1:
        params_list = list(params)
        available_limit = params_list[0]
    else:
        _, available_limit = params
    account = Account(False, available_limit)
    account_list.append(account)
    violations_account()
    return account


def change_status(status: bool):
    account = entry_point()
    account.activeCard = status
    return account.activeCard


def verify(lista=account_list):
    """[summary]
    Verifica en cada iteración el comportamiento de lista de cuentas
    Args:
        lista ([List], optional): [description]. Defaults to account_list.

    Returns:
        [List]: [Retorna la lista para verificarse de ser necesario]
    """
    return lista
