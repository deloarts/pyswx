"""
PYSWX TESTS
"""

from pyswx.const import VERSION


def test_version():
    assert VERSION == "0.0.1"


def test_pyswx():
    from pyswx import PySWX

    swx = PySWX().application

    while not swx.startup_process_completed:
        pass

    assert swx.visible  # This is set in conftest.py
    assert swx.startup_process_completed
    assert swx.user_control == False
