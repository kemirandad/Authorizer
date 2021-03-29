from Validations.val_account import is_already_initialized
from Entities.violations import Violation

class ListViolation(object):
    def __init__(self):
        self.__list_violations = []
        
    @property
    def list