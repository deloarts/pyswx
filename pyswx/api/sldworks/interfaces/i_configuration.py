"""
IConfiguration Interface Members

Reference:
https://help.solidworks.com/2018/english/api/sldworksapi/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html

Status: 🔴
"""

from pyswx.api.base_interface import BaseInterface
from pyswx.api.sldworks.interfaces.i_component_2 import IComponent2
from pyswx.api.sldworks.interfaces.i_custom_property_manager import (
    ICustomPropertyManager,
)
from pyswx.api.swconst.enumerations import SWChildComponentInBOMOptionE


class IConfiguration(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IConfiguration({self.com_object})"

    @property
    def child_component_display_in_bom(self) -> SWChildComponentInBOMOptionE:
        """
        Gets or sets the child component display option of a configuration in a Bill of Materials (BOM) for an assembly document.

        Reference:
        https://help.solidworks.com/2024/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~ChildComponentDisplayInBOM.html
        """
        return SWChildComponentInBOMOptionE(self.com_object.ChildComponentDisplayInBOM)

    @child_component_display_in_bom.setter
    def child_component_display_in_bom(self, value: SWChildComponentInBOMOptionE) -> None:
        self.com_object.ChildComponentDisplayInBOM = value.value

    @property
    def custom_property_manager(self) -> ICustomPropertyManager:
        """
        Gets the custom property information for this configuration.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.html
        """
        return ICustomPropertyManager(self.com_object.CustomPropertyManager)

    @property
    def name(self) -> str:
        """
        Gets or sets the configuration name.

        Reference:
        https://help.solidworks.com/2021/English/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Name.html
        """
        return str(self.com_object.Name)

    @name.setter
    def name(self, value: str) -> None:
        self.com_object.Name = value

    def get_root_component3(self, resolve: bool) -> IComponent2 | None:
        """
        Gets the root component for this assembly configuration.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.html
        """
        com_object = self.com_object.GetRootComponent3(resolve)
        return IComponent2(com_object) if com_object else None
