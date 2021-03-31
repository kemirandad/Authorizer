from dataclasses import dataclass

class Violation:
    violations_dict = {
            'account': 'account-already-initialized',
            'status': 'card-not-active',
            'amount': 'insufficient-limit',
            'purchase': 'double-purchase',
            'time_frequency': 'high-frequency-small-interval',
            'time-double': 'double-transaction'
        }