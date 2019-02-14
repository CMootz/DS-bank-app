from .bank import Bank
from .data_preproc import DataWrapper


def check_greater_zero(value):
    if isinstance(value, int):
        return value > 0
    elif isinstance(value, float):
        return value > 0.0


__all__ = ['Bank', 'DataWrapper']
