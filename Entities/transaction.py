import datetime

class Transaction():
    def __init__(self, merchant: str, amount: int, time: datetime):
        self.__merchant = merchant
        self.__amount = amount
        self.__time = time
    
    @property
    def get_merchant(self):
        return self.__merchant
    
    @property.setter
    def set_merchant(self, new_merchant: str):
        self.__merchant = new_merchant
    
    @property
    def get_amount(self):
        return self.__amount
    
    @property.setter
    def set_amount(self, new_amount: int):
        self.__amount = new_amount
    
    @property
    def get_time(self):
        return self.__time
    
    @property.setter
    def set_time(self, new_time: datetime):
        self.__time = new_time