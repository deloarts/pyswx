"""
swComponentSolvingOption_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSolvingOption_e.html

Status: 🟢
"""

from enum import IntEnum


class SWComponentSolvingOptionE(IntEnum):
    """Specifies options for resolving components in assemblies."""

    SW_COMPONENT_RIGID_SOLVING = 0  # Component is solved as rigid (default)
    SW_COMPONENT_FLEXIBLE_SOLVING = 1  # Component is solved as flexible
