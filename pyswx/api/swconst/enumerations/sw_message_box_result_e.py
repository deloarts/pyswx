"""
swMessageBoxResult_e Enumeration

Defines the possible results returned from SolidWorks message boxes.

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMessageBoxResult_e.html

Status: 🟢
"""

from enum import IntEnum


class SWMessageBoxResultE(IntEnum):
    """Results of user interaction with a message box."""

    SW_MB_HIT_ABORT = 1  # Abort was clicked
    SW_MB_HIT_CANCEL = 7  # Cancel was clicked
    SW_MB_HIT_IGNORE = 2  # Ignore was clicked
    SW_MB_HIT_NO = 3  # No was clicked
    SW_MB_HIT_OK = 4  # OK was clicked
    SW_MB_HIT_RETRY = 5  # Retry was clicked
    SW_MB_HIT_YES = 6  # Yes was clicked
