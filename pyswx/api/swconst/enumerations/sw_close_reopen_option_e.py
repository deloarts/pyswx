"""
swCloseReopenOption_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCloseReopenOption_e.html

Status: 🟢
"""

from enum import IntEnum


class SWCloseReopenOptionE(IntEnum):
    """File close and reopen options. Bitmask."""

    SW_CLOSE_REOPEN_OPTION_READ_ONLY = 1  # Open the document in read-only mode
    SW_CLOSE_REOPEN_OPTION_DISCARD_CHANGES = 2  # Discard changes before reopening
    SW_CLOSE_REOPEN_OPTION_MATCH_SHEET = 4  # Reopen with the same active sheet
    SW_CLOSE_REOPEN_OPTION_EXIT_DETAILING_MODE = 8  # Reopen model drawings as resolved
