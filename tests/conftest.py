"""
PYSWX TESTS // CONFTEST
"""

import pytest


def pytest_sessionstart():
    from pyswx import PySWX

    swx = PySWX().application
    swx.visible = True
    swx.user_control = False
    assert (
        swx.get_document_count() == 0
    ), "\n\n\n\nClose all documents before running tests!\n\n\n"


def pytest_sessionfinish():
    from pyswx import PySWX

    swx = PySWX().application
    swx.user_control = True
