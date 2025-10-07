"""
swMessageBoxIcon_e Enumeration

Defines message box icons used in SolidWorks.

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMessageBoxIcon_e.html

Status: 🟢
"""

from enum import IntEnum


class SWMessageBoxIconE(IntEnum):
    """Message box icon types."""

    SW_MB_WARNING = 1  # Exclamation-point (!) icon
    SW_MB_INFORMATION = 2  # Information (i) icon
    SW_MB_QUESTION = 3  # Question-mark (?) icon
    SW_MB_STOP = 4  # Stop-sign icon
