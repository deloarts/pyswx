"""
IComponent2 Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html

Status: 🔴
"""

from pathlib import Path
from typing import TYPE_CHECKING
from typing import List

from pythoncom import VT_ARRAY
from pythoncom import VT_BOOL
from pythoncom import VT_BSTR
from pythoncom import VT_I4
from pythoncom import VT_NULL
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.swconst.enumerations import SWComponentSuppressionStateE
from pyswx.api.swconst.enumerations import SWDocumentTypesE
from pyswx.api.swconst.enumerations import SWInConfigurationOptsE

if TYPE_CHECKING:
    from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2


class IComponent2(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IComponent2({self.com_object})"

    @property
    def name2(self) -> str:
        """
        Gets the name of this component.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2.html
        """
        return self.com_object.Name2

    @name2.setter
    def name2(self, value: str):
        self.com_object.Name2 = value

    def get_children(self) -> List["IComponent2"]:
        """
        Gets all of the children components of this component.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetChildren.html
        """
        com_object = self.com_object.GetChildren
        return [IComponent2(i) for i in com_object]

    @property
    def referenced_configuration(self) -> str:
        """
        Gets or sets the active configuration used by this component.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ReferencedConfiguration.html
        """
        return self.com_object.ReferencedConfiguration

    @referenced_configuration.setter
    def referenced_configuration(self, value: str) -> None:
        self.com_object.referenced_configuration = value

    def get_exclude_from_bom2(self, config_opt: SWInConfigurationOptsE, config_names: List[str] | None) -> List[bool]:
        """
        Gets whether this component is excluded from the bills of materials (BOMs) in the specified configurations.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetExcludeFromBOM2.html
        """
        in_config_opt = VARIANT(VT_I4, config_opt.value)
        in_config_names = (
            VARIANT(VT_BSTR | VT_ARRAY, [str(i) for i in config_names]) if config_names else VARIANT(VT_NULL, None)
        )

        com_object = self.com_object.GetExcludeFromBOM2(in_config_opt, in_config_names)
        return [bool(i) for i in com_object]

    def get_id(self) -> int:
        """
        Gets the component ID for this component.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetID.html
        """
        return int(self.com_object.GetID)

    def get_model_doc2(self) -> "IModelDoc2 | None":
        """
        Gets the model document for this component.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetModelDoc2.html
        """
        from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2

        com_object = self.com_object.GetModelDoc2
        return IModelDoc2(com_object) if com_object else None

    def get_parent(self) -> "IComponent2":
        """
        Gets the parent component.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetParent.html
        """
        com_object = self.com_object.GetParent
        return IComponent2(com_object)

    def get_path_name(self) -> Path:
        """
        Gets the full path name for this component.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetPathName.html
        """
        return Path(self.com_object.GetPathName)

    def get_suppression2(self) -> SWComponentSuppressionStateE:
        """
        Gets the suppression state of this component.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSuppression2.html
        """
        return SWComponentSuppressionStateE(self.com_object.GetSuppression2)

    def get_type(self) -> SWDocumentTypesE:
        """
        Gets this lightweight assembly component's document type.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetType.html
        """
        return SWDocumentTypesE(self.com_object.GetType)

    def is_envelope(self) -> bool:
        """
        Gets whether this component is an envelope.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.icomponent2~isenvelope.html
        """
        return bool(self.com_object.IsEnvelope)

    def is_hidden(self, consider_suppressed: bool) -> bool:
        """
        Gets whether this component is hidden or suppressed.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/solidworks.interop.sldworks~solidworks.interop.sldworks.icomponent2~ishidden.html
        """
        in_consider_suppressed = VARIANT(VT_BOOL, consider_suppressed)

        return bool(self.com_object.IsHidden(in_consider_suppressed))
