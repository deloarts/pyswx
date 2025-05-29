"""
IDrawingDoc Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html

Status: 🔴
"""

from pyswx.api.base_interface import BaseInterface


class IDrawingDoc(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IDrawingDoc({self.com_object})"
