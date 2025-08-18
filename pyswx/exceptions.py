"""
PYSWX EXCEPTIONS
"""

import sys
import traceback

from pyswx.logger import log


class BaseError(Exception):
    """Base class for all app exceptions. Logs to pyswx logger."""

    def __init__(self, msg: str) -> None:

        super().__init__(msg)
        if traceback.extract_tb(sys.exc_info()[2]):
            log.logger.exception(msg)
        else:
            log.logger.error(msg)


class DocumentError(BaseError): ...
