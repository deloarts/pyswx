"""
swCADFamilyCfgOptions_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCADFamilyCfgOptions_e.html

Status: 🟢
"""

from enum import IntFlag


class SWCADFamilyCfgOptionsE(IntFlag):
    """SOLIDWORKS CONNECTED family configuration options. Bitmask."""

    SW_CAD_FAMILY_CFG_OPTION_SUPPRESS_NEW_FEATURES = 1  # Suppress new features
    SW_CAD_FAMILY_CFG_OPTION_SUPPRESS_NEW_COMPONENTS = 2  # Suppress new components
    SW_CAD_FAMILY_CFG_OPTION_DONT_ACTIVATE = 4  # Do not activate
