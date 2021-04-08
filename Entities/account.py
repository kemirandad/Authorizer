def singleton(cls):
    instances = dict()
    
    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrap

@singleton

class Account(object):
    """[summary]
    Clase Account para implementar un unico objeto usando el patron de diseño Singleton
    Args:
        activeCard ([Boolean]): [Determina el estado de la cuenta y si podrá o no hacer una transacción más adelante]
        availableLimit ([Integer]): [Almacena la cantidad de dinero disponible en la cuenta]
    """
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
        self.__availableLimit = self.__availableLimit - new_disponible