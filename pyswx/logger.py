"""
PYSWX Logger Module
"""

import logging
import sys


def create_logger() -> logging.Logger:
    """
    Create and configure a logger for PYSWX.

    Returns:
        logging.Logger: The configured logger instance.
    """
    default_handler = logging.StreamHandler(sys.stderr)
    default_handler.setFormatter(
        logging.Formatter("[%(asctime)s] %(levelname)s in %(module)s: %(message)s")
    )

    logger = logging.getLogger("pyswx")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    logger.addHandler(default_handler)

    return logger
