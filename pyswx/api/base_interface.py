"""
Base interface for all API interfaces.
"""

import logging

from pyswx.logger import create_logger


class BaseInterface:
    """
    Base interface for all api interfaces.
    This class provides a logger property that can be used by derived classes.
    Logs to 'pyswx'.
    """

    def __init__(self) -> None:
        pass

    @property
    def logger(self) -> logging.Logger:
        return create_logger()
