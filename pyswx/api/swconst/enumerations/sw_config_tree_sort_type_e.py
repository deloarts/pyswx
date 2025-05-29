"""
swConfigTreeSortType_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConfigTreeSortType_e.html
"""

from enum import IntEnum


class SWConfigTreeSortTypeE(IntEnum):
    """Order in which configurations are listed in the ConfigurationManager."""

    SW_SORT_TYPE_HISTORY = 0  # Sorted by creation date (earliest to latest)
    SW_SORT_TYPE_NUMERIC = 1  # Sorted by ascending numeric or alphanumeric value
    SW_SORT_TYPE_LITERAL = 2  # Sorted alphabetically
    SW_SORT_TYPE_DESIGN_TABLE = 3  # Sorted by order in the design table
