"""This is to raised when a customer trys to create an account with either a First name or an Last name that is over
the 20-character limit."""


class InputLength(Exception):
    pass