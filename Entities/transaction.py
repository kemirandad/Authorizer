import datetime

class Transaction():
    """[summary]
    Clase Transaction para controlar el flujo de transacciones y/o peticiones por consola
    Args:
        merchant ([String]): [Almacena el nombre de la tienda o comercio en el que se realiza la compra]
        amount ([Integer]): [Almacena la cantidad de dinero devengado por la compra]
        time ([String]): [Almacena el momento exacto de la compra YYYY-mm-DD-HH-MM-SS-%s]
    """
    def __init__(self, merchant: str, amount: int, time: datetime):
        self.__merchant = merchant
        self.__amount = amount
        self.__time = time
    
    @property
    def merchant(self):
        return self.__merchant
    
    @merchant.setter
    def merchant(self, merchant):
        self.__merchant = merchant
    
    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, amount):
        self.__amount = amount
    
    @property
    def time(self):
        return self.__time
    
    @time.setter
    def time(self, time):
        self.__time = time