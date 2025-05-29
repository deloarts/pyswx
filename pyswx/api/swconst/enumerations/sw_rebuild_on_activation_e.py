"""
swRebuildOnActivation_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swRebuildOnActivation_e.html
"""

from enum import IntEnum


class SWRebuildOnActivationOptionsE(IntEnum):
    SW_USER_DECISION = 0  # Prompt the user whether to rebuild the activated document
    SW_DONT_REBUILD_ACTIVE_DOC = 1  # Do not rebuild the activated document
    SW_REBUILD_ACTIVE_DOC = 2  # Rebuild the activated document
