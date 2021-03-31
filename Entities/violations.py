from dataclasses import dataclass

class Violation:
    violations_dict = {
            'account': 'account-already-initialized',
            'status': 'inactive-card',
            'amount': 'insufficient-limit',
            'purchase': 'double-purchase'
        }