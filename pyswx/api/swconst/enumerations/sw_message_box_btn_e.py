"""
swMessageBoxBtn_e Enumeration

Defines the control button sets available for SolidWorks message boxes.

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMessageBoxBtn_e.html
"""

from enum import IntEnum


class SWMessageBoxBtnE(IntEnum):
    """Message box control button configurations."""

    SW_MB_ABORT_RETRY_IGNORE = 1  # Buttons: Abort, Retry, Ignore
    SW_MB_OK = 2  # Button: OK
    SW_MB_OK_CANCEL = 3  # Buttons: OK, Cancel
    SW_MB_RETRY_CANCEL = 4  # Buttons: Retry, Cancel
    SW_MB_YES_NO = 5  # Buttons: Yes, No
    SW_MB_YES_NO_CANCEL = 6  # Buttons: Yes, No, Cancel
