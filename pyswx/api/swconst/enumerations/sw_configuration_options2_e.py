"""
swConfigurationOptions2_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigurationOptions2_e.html

Status: 🟢
"""

from enum import IntEnum


class SWConfigurationOptions2E(IntEnum):
    """Option bits used when setting configuration options. Bitmask."""

    SW_CONFIG_OPTION_USE_ALTERNATE_NAME = 1  # Use an alternate configuration name
    SW_CONFIG_OPTION_DONT_SHOW_PARTS_IN_BOM = (
        2  # Show sub-assemblies instead of child components in BOM
    )
    SW_CONFIG_OPTION_SUPPRESS_BY_DEFAULT = 4  # Suppress newly added features and mates
    SW_CONFIG_OPTION_HIDE_BY_DEFAULT = 8  # Hide newly added components
    SW_CONFIG_OPTION_MIN_FEATURE_MANAGER = 16  # Suppress new components
    SW_CONFIG_OPTION_LINK_TO_PARENT = 64  # Link component to parent configuration
    SW_CONFIG_OPTION_DONT_ACTIVATE = 128  # Do not activate the configuration
    SW_CONFIG_OPTION_DO_DISSOLVE_IN_BOM = (
        256  # Dissolve configuration in BOM and promote child components
    )
    SW_CONFIG_OPTION_USE_DESCRIPTION_IN_BOM = 512  # Use description in BOM
