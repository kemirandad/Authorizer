from Operations.create_account import *
from Entities.violations import Violation
from Operations.transaction_history import *
from Operations.create_account import *
from Entities.account import Account
from Operations import violations_list
from datetime import datetime

"""[summary]
    Modulo controlador de las operaciones ejecutadas mediante transacciones
"""

def entry_point():
    """[summary]
    Funcion que genera un nuevo objeto de tipo Account para acceder a los atributos de la clase
    unica debido al patron de diseño Singleton
    Returns:
        [Account]: [Regresa un objeto unico de tipo Account]
    """
    my_account = Account(True, 0)
    return my_account

def set_disponible():
    """[summary]
    Llama la función entry point, accede al ultimo valor de compra de la transaccion y verifica
    si existe saldo disponible para efectuar la compra
    Returns:
        [String]: [Retorna un valor del diccionario de violaciones si la compra no puede ejecutarse]
    """
    my_account = entry_point()
    amount = last_amount_list[0]
    if amount > my_account.availableLimit: #and len(violations_list.list_violations) == 0:
        return Violation.violations_dict['amount']
    elif amount <= my_account.availableLimit and len(violations_list.list_violations) == 0:
        my_account.availableLimit = amount
        
def status_card():
    """[summary]
    Llama la función entry point, accede a su parametro de activeCard y retorna True si es una
    cuenta activa.
    Returns:
        [String]: [Retorna un valor del diccionario de violaciones si la compra no puede ejecutarse]
    """
    my_account = entry_point()
    if my_account.activeCard == False:
        return Violation.violations_dict['status']
    else:
        return True

def double_transaction():
    """[summary]
    Llama la función entry point, accede a los dos ultimos valores de compra y las dos ultimas tiendas
    verifica si son las mismas, si se ha efectuado en menos de dos minutos y si el estado de la tarjeta
    es activo
    Returns:
        [String]: [Retorna un valor del diccionario de violaciones si la compra no puede ejecutarse]
    """
    my_account = entry_point()
    if len(last_amount_list) > 1 and len(last_merchant_list) > 1:
        validation_merchant = last_merchant_list[0] == last_merchant_list[1]
        validation_amount = last_amount_list[0] == last_amount_list[1]
        if validation_amount and validation_merchant and time_validation_double() == True and my_account.activeCard != False:
            return Violation.violations_dict['time-double']
        
def time_validation_frequency():
    """[summary]
    Llama la función entry point, accede a los tiempos de las 3 ultimas compras se parsean para convertirlos
    a datos tipo DateTime y luego nuevamente a String, se operan estos dos valores como enteros y se obtiene
    la diferencia entre ellos.
        [String]: [Retorna un valor del diccionario de violaciones si la compra no puede ejecutarse]
    """
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
    """[summary]
    Llama la función entry point, accede a los tiempos de las 2 ultimas compras se parsean para convertirlos
    a datos tipo DateTime y luego nuevamente a String, se operan estos dos valores como enteros y se obtiene
    la diferencia entre ellos.
    Returns:
        [Boolean]: [Si la diferencia es menor a 2 minutos retorna False, sino True]
    """
    CONST = 200000000
    
    if len(last_time_list) > 1:
        last_two_purchase = last_time_list[:2]
        for time in range(len(last_two_purchase)):
            last_two_purchase[time] = datetime.strptime(last_two_purchase[time], '%Y-%m-%dT%H:%M:%S.%fZ')
            last_two_purchase[time] = last_two_purchase[time].strftime('%Y%m%d%H%M%S%f')
        times_diff = int(last_two_purchase[0]) - int(last_two_purchase[1])
        
        return False if times_diff > CONST else True
