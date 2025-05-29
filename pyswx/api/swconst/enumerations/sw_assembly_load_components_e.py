"""
swAssemblyLoadComponents_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyLoadComponents_e.html

Status: 🟢
"""

from enum import IntEnum


class SWAssemblyLoadComponentsE(IntEnum):
    """Assembly loading options in Tools > System Options > Performance."""

    SW_ASSEMBLY_LOAD_COMPONENTS_AUTO_LOAD = 0  # Auto load components
    SW_ASSEMBLY_LOAD_COMPONENTS_MANUAL_LOAD = 1  # Manual load components
