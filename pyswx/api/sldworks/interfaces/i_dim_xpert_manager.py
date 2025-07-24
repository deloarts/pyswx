"""
IDimXpertManager Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimXpertManager_members.html

Status: 🔴
"""

from pyswx.api.base_interface import BaseInterface


class IDimXpertManager(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IDimXpertManager ({self.com_object})"
