"""
IExplodeStep Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html?id=286529deb1df4c659253bd5be2bbea5d#Pg0
Status: 🔴
"""

from pyswx.api.base_interface import BaseInterface


class IExplodeStep(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IExplodeStep ({self.com_object})"
