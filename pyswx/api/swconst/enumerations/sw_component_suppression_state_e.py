"""
swComponentSuppressionState_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html

Status: 🟢
"""

from enum import IntEnum


class SWComponentSuppressionStateE(IntEnum):
    """States for component suppression."""

    SW_COMPONENT_SUPPRESSED = 0  # Fully suppressed (recursive)
    SW_COMPONENT_LIGHTWEIGHT = 1  # Lightweight (only the component)
    SW_COMPONENT_FULLY_RESOLVED = 2  # Fully resolved (recursive)
    SW_COMPONENT_RESOLVED = 3  # Resolved (only the component)
    SW_COMPONENT_FULLY_LIGHTWEIGHT = 4  # Fully lightweight (recursive)
    SW_COMPONENT_INTERNAL_ID_MISMATCH = 5  # Internal ID mismatch
