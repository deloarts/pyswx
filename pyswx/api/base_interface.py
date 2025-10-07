"""
Base interface for all API interfaces.
"""

from logging import Logger

from pyswx.logger import log


class BaseInterface:
    """
    Base interface for all api interfaces.
    This class provides a logger property that can be used by derived classes.
    Logs to 'pyswx'.
    """

    def __init__(self) -> None:
        pass

    @property
    def logger(self) -> Logger:
        return log.logger
