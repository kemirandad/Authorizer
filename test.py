def singleton(cls):
    instances = dict()
    
    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrap

@singleton
class Account(object):
    
    def __init__(self, activeCard: bool, availableLimit: int):
        self.__activeCard = activeCard
        self.__availableLimit = availableLimit
    
    def __repr__(self):
        return str(self.__dict__)
    
    @property
    def activeCard(self):
        return self.__activeCard
    
    @activeCard.setter
    def activeCard(self, new_status):
        self.__activeCard = new_status
    
    @property
    def availableLimit(self):
        return self.__availableLimit
    
    @availableLimit.setter
    def availableLimit(self, new_disponible):
        self.__availableLimit -= new_disponible


if __name__ == '__main__':
    account1 = Account(True, 100)
    print(account1)
    
    account2 = Account(False, 500)
    print(account2)
