"""
swInConfigurationOpts_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html
"""

from enum import IntEnum


class SWInConfigurationOptsE(IntEnum):
    SW_CONFIG_PROPERTY_SUPPRESS_FEATURES = 0  # Suppress features
    SW_THIS_CONFIGURATION = 1  # This configuration only
    SW_ALL_CONFIGURATION = 2  # All configurations
    SW_SPECIFY_CONFIGURATION = 3  # Specify a configuration
    SW_LINKED_TO_PARENT = 4  # Linked to parent (valid only for derived configurations)
    SW_SPEEDPAK_CONFIGURATION = 5  # SpeedPak configuration
