from Validations.val_account import is_already_initialized
from Validations.val_transaction import status_card, set_disponible, double_transaction, entry_point, time_validation_double, time_validation_frequency
from Entities.violations import Violation
from Entities.account import Account
from dataclasses import dataclass
from Operations import create_account, transaction_history

"""[summary]
    Modulo controlador de las validaciones producidas al generarse una nueva operacion
    bancaria
"""
list_violations = []

def violations_account():
    """[summary]
    Ejecuta la validación "Account exist" si la lista de cuentas es mayor a cero
    """
    if len(create_account.account_list) > 0:
        violation_account_exist()

def violations_transaction():
    """[summary]
    Ejecuta las dos violaciones independientes de otras:
    status de cuenta
    limite no disponible
    """
    violation_limit()
    
        
def violation_account_exist(lista = list_violations):
    """[summary]

    Args:
        lista ([type], optional): [description]. Defaults to list_violations.

    Returns:
        [type]: [description]
    """
    already_exist = is_already_initialized()
    if already_exist != None:
        lista.append(already_exist) 
    return lista
        
def violation_limit(lista = list_violations):
    """[summary]
    Verifica si la cuenta tiene saldo disponible para ejecutar la transacción
    Args:
        lista ([List], optional): [Recibe la lista de violaciones
        y agrega una nueva violacion si el limite disponible es menor
        al valor de la transferencia]. Defaults to list_violations.

    Returns:
        [List]: [Retorna la lista de violaciones]
    """
    status = status_card()
    if status == True:
        violation_double()
        violation_frequency()
        without_limit = set_disponible()
        if without_limit != None:
            lista.append(without_limit)
        return lista

def violation_status(lista = list_violations):
    """[summary]
    Verifica si la cuenta esta activa
    Args:
        lista ([List], optional): [Recibe la lista de violaciones
        y agrega una nueva violacion si el estatus de la tarjeta es distinto a 
        True]. Defaults to list_violations.

    Returns:
        [List]: [Retorna la lista de violaciones]
    """
    status = status_card()
    if status != True:
        lista.append(status)
    return lista

def violation_double(lista = list_violations):
    """[summary]
    Verifica si intento hacer una compra en una misma tienda un item con el mismo valor
    en menos de 2 minutos.
    Args:
        lista ([List], optional): [Recibe la lista de violaciones
        y agrega una nueva violacion]. Defaults to list_violations.

    Returns:
        [List]: [Retorna la lista de violaciones]
    """
    double_purchase = double_transaction()
    if double_purchase != None:
        lista.append(double_purchase)
    return lista

def violation_frequency(lista = list_violations):
    """[summary]
    Verifica si se ha intentado hacer 3 compras en menos de 2 minutos
    Args:
        lista ([List], optional): [Recibe la lista de violaciones
        y agrega una nueva violacion si se cumple la condicion inicial]. Defaults to list_violations.

    Returns:
        [List]: [Retorna la lista de violaciones]
    """
    high_frequency = time_validation_frequency()
    if high_frequency != None:
        lista.append(high_frequency)
    return lista
