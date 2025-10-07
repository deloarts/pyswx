"""
swCreateExplodeStepError_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateExplodeStepError_e.html

Status: 🟢
"""

from enum import IntEnum


class SWCreateExplodeStepErrorE(IntEnum):
    """Defines return codes when creating an explode step in SolidWorks."""

    SW_CREATE_EXPLODE_STEP_ERROR_SUCCESSFUL = 0  # Step created successfully
    SW_CREATE_EXPLODE_STEP_ERROR_GENERIC = 1  # Explode step creation failed
    SW_CREATE_EXPLODE_STEP_ERROR_NO_EXPLODE_VIEW = 2  # No explode view active
    SW_CREATE_EXPLODE_STEP_ERROR_NO_COMPONENTS = 3  # No components selected
    SW_CREATE_EXPLODE_STEP_ERROR_INVALID_RADIAL_AXIS = 4  # Invalid radial explode axis
    SW_CREATE_EXPLODE_STEP_ERROR_OPEN_EXPLODE_PMP = 5  # Explode PropertyManager is open
    SW_CREATE_EXPLODE_STEP_ERROR_EDITING_COMPONENT_IN_CONTEXT = 6  # Editing a component in context is blocking creation
