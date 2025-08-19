"""
PYSWX TESTS // CONFTEST
"""

import os
from pathlib import Path

import pytest

from tests.scripts import create_test_drawing_01
from tests.scripts import create_test_part_01
from tests.scripts import create_test_part_02

TEST_ROOT = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tests")
TEST_OBJECTS = Path(TEST_ROOT, "objects")
TEST_PART_01 = Path(TEST_OBJECTS, "test_01.sldprt")
TEST_PART_01_EXPORT_STEP = Path(TEST_OBJECTS, "test_01.step")
TEST_PART_02 = Path(TEST_OBJECTS, "test_02.sldprt")
TEST_DRAWING_01 = Path(TEST_OBJECTS, "test_01.slddrw")


def pytest_sessionstart():
    from pyswx import PySWX
    from pyswx.api.swconst.enumerations import SWMessageBoxBtnE
    from pyswx.api.swconst.enumerations import SWMessageBoxIconE

    swx = PySWX().application
    swx.visible = True
    swx.user_control = False

    doc_count = swx.get_document_count()

    if doc_count > 0:
        swx.send_msg_to_user2(
            message="PYSWX: Close all documents before running tests.",
            icon=SWMessageBoxIconE.SW_MB_WARNING,
            buttons=SWMessageBoxBtnE.SW_MB_OK,
        )
    assert doc_count == 0, "\n\n\n\nClose all documents before running tests!\n\n\n"

    # Ensure test object folder has all required files
    os.makedirs(TEST_OBJECTS, exist_ok=True)
    if not TEST_PART_01.exists():
        create_test_part_01.run(file_location=TEST_PART_01)
    if not TEST_PART_02.exists():
        create_test_part_02.run(file_location=TEST_PART_02)
    if not TEST_DRAWING_01.exists():
        create_test_drawing_01.run(part_file_location=TEST_PART_01, drawing_file_location=TEST_DRAWING_01)

    # Remove generic files
    if os.path.exists(TEST_PART_01_EXPORT_STEP):
        os.remove(TEST_PART_01_EXPORT_STEP)


def pytest_sessionfinish():
    from pyswx import PySWX

    swx = PySWX().application
    swx.user_control = True
