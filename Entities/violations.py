from dataclasses import dataclass
"""[summary]
    Modulo que almacena las restricciones de la aplicación
"""
class Violation:
    """[summary]
    Data class contenedora de las violaciones que puede producir el usuario
    violations_dict ([dict]) = [Diccionario con las violaciones]
    """
    violations_dict = {
            'account': 'account-already-initialized',
            'status': 'card-not-active',
            'amount': 'insufficient-limit',
            'purchase': 'double-purchase',
            'time_frequency': 'high-frequency-small-interval',
            'time-double': 'double-transaction'
        }