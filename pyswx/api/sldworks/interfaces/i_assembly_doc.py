"""
IAssemblyDoc Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html

Status: 🔴
"""

from typing import List

from pythoncom import VT_BOOL
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.sldworks.interfaces.i_component_2 import IComponent2


class IAssemblyDoc(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IAssemblyDoc({self.com_object})"

    def get_components(self, top_level_only: bool) -> List[IComponent2]:
        """
        Gets all of the components in the active configuration of this assembly.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.iassemblydoc~getcomponents.html
        """
        in_top_level_only = VARIANT(VT_BOOL, top_level_only)

        com_object = self.com_object.GetComponents(in_top_level_only)
        return [IComponent2(i) for i in com_object]
