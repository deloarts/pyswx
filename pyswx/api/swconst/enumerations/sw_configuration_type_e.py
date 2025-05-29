"""
swConfigurationType_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swConfigurationType_e.html

Status: 🟢
"""

from enum import IntEnum


class SWConfigurationTypeE(IntEnum):
    """Types of configurations."""

    SW_CONFIGURATION_STANDARD = 0  # Standard configuration
    SW_CONFIGURATION_ASMACHINED = 1  # As Machined configuration
    SW_CONFIGURATION_ASWELDED = 2  # As Welded configuration
    SW_CONFIGURATION_SHEETMETAL = 3  # Sheet Metal configuration
    SW_CONFIGURATION_SPEEDPAK = 4  # SpeedPak configuration
