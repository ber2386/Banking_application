"""This custom exception is used when you try to access an
entity via a non-existent Record"""


class RecordNotFound(Exception):
    pass