#!/usr/bin/python3
class Error(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooFar(Error):
    """Raised when the input value is too large"""
    pass


def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except ValueTooFar:
            result = b + a
            break
    return (result)
