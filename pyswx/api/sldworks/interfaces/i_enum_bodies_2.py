"""
IEnumBodies2 Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumBodies2_members.html

Status: 🔴
"""

from pyswx.api.base_interface import BaseInterface


class IEnumBodies2(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IEnumBodies2({self.com_object})"
