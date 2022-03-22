"""
    File contain all custom errors
"""
class NotSupportedCity(Exception):
    """Raised when the city value is not supported"""
    pass

class NotSupportedMonth(Exception):
    """Raised when the month value is not supported"""
    pass

class NotSupportedDay(Exception):
    """Raised when the day value is not supported"""
    pass