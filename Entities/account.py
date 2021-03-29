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
    
    @property
    def activeCard(self):
        return self.__activeCard
    
    @activeCard.setter
    def set_active_card(self, new_status):
        self.__activeCard = new_status
    
    @property
    def availableLimit(self):
        return self.__availableLimit
    
    @availableLimit.setter
    def set_available_limit(self, new_disponible):
        self.__availableLimit = new_disponible