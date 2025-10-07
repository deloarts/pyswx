"""
PYSWX LOGGER
"""

import logging
import sys


class Log:
    def __init__(self) -> None:
        """
        Create and configure a logger for PYSWX.
        """
        default_handler = logging.StreamHandler(sys.stderr)
        default_handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s"))

        self._logger = logging.getLogger("pyswx")
        self._logger.setLevel(logging.INFO)
        self._logger.handlers.clear()
        self._logger.addHandler(default_handler)

    @property
    def logger(self) -> logging.Logger:
        """The pyswx logging handler"""
        return self._logger

    def set_level_debug(self) -> None:
        """Sets the level of the log handler to 'DEBUG'"""
        self._logger.setLevel(logging.DEBUG)

    def set_level_info(self) -> None:
        """Sets the level of the log handler to 'INFO'"""
        self._logger.setLevel(logging.INFO)


log = Log()
