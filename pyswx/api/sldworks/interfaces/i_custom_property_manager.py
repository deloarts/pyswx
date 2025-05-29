"""
ICustomPropertyManager Interface Members

Reference:
https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.html

Status: 🔴
"""

from typing import List
from typing import Tuple

from pythoncom import VT_BOOL
from pythoncom import VT_BSTR
from pythoncom import VT_BYREF
from pythoncom import VT_I4
from pythoncom import VT_VARIANT
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.swconst.enumerations import SWCustomInfoAddResultE
from pyswx.api.swconst.enumerations import SWCustomInfoDeleteResultE
from pyswx.api.swconst.enumerations import SWCustomInfoGetResultE
from pyswx.api.swconst.enumerations import SWCustomInfoSetResultE
from pyswx.api.swconst.enumerations import SWCustomInfoTypeE
from pyswx.api.swconst.enumerations import SWCustomLinkSetResultE
from pyswx.api.swconst.enumerations import SWCustomPropertyAddOptionE

type ValueOut = str
type ResolvedValueOut = str
type WasResolvedOut = bool
type LinkToPropertyOut = bool

type NumberOfProperties = int
type PropNames = List[str]
type PropTypes = List[SWCustomInfoTypeE]
type PropValues = List[str]
type Resolved = List[SWCustomInfoGetResultE]
type PropLink = List[int]


class ICustomPropertyManager(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"ICustomPropertyManager({self.com_object})"

    @property
    def count(self) -> int:
        """
        Gets the number of custom properties.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Count.html
        """
        return int(self.com_object.Count)

    @property
    def link_all(self) -> bool:
        """
        Gets or sets whether to link or unlink all custom properties to or from their parent part.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~LinkAll.html
        """
        return bool(self.com_object.LinkAll)

    @link_all.setter
    def link_all(self, value: bool):
        self.com_object.LinkAll = value

    @property
    def owner(self) -> str:
        """
                Gets the owner of this custom property.

                Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Owner.html
        """
        return str(self.com_object.Owner)

    def add3(
        self,
        field_name: str,
        field_type: SWCustomInfoTypeE,
        field_value: str,
        overwrite_existing: SWCustomPropertyAddOptionE,
    ) -> SWCustomInfoAddResultE:
        """
        Adds a custom property to a configuration or model document.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add3.html
        """
        return SWCustomInfoAddResultE(
            self.com_object.Add3(
                field_name, field_type.value, field_value, overwrite_existing.value
            )
        )

    def delete2(self, field_name: str) -> SWCustomInfoDeleteResultE:
        """
        Deletes the specified custom property.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Delete2.html
        """
        return SWCustomInfoDeleteResultE(self.com_object.Delete2(field_name))

    def get6(
        self,
        field_name: str,
        use_cached: bool,
    ) -> Tuple[
        SWCustomInfoGetResultE,
        ValueOut,
        ResolvedValueOut,
        WasResolvedOut,
        LinkToPropertyOut,
    ]:
        """
        Gets the value and the evaluated value of the specified custom property.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get6.html
        """

        in_field_name = VARIANT(VT_BSTR, field_name)
        in_use_cached = VARIANT(VT_I4, int(use_cached))

        out_val_out = VARIANT(VT_BYREF | VT_BSTR, None)
        out_resolved_val_out = VARIANT(VT_BYREF | VT_BSTR, None)
        out_was_resolved = VARIANT(VT_BYREF | VT_BOOL, None)
        out_link_to_property = VARIANT(VT_BYREF | VT_BOOL, None)

        com_object = self.com_object.Get6(
            in_field_name,
            in_use_cached,
            out_val_out,
            out_resolved_val_out,
            out_was_resolved,
            out_link_to_property,
        )

        return (
            SWCustomInfoGetResultE(com_object),
            str(out_val_out.value),
            str(out_resolved_val_out.value),
            bool(out_was_resolved.value),
            bool(out_link_to_property.value),
        )

    def get_all3(
        self,
    ) -> Tuple[
        NumberOfProperties, PropNames, PropTypes, PropValues, Resolved, PropLink
    ]:
        """
        Gets all of the custom properties for this configuration.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll3.html
        """
        out_prop_names = VARIANT(VT_VARIANT | VT_BYREF, [])
        out_prop_types = VARIANT(VT_VARIANT | VT_BYREF, [])
        out_prop_values = VARIANT(VT_VARIANT | VT_BYREF, [])
        out_prop_resolved = VARIANT(VT_VARIANT | VT_BYREF, [])
        out_prop_link = VARIANT(VT_VARIANT | VT_BYREF, [])

        com_object = self.com_object.GetAll3(
            out_prop_names,
            out_prop_types,
            out_prop_values,
            out_prop_resolved,
            out_prop_link,
        )

        return (
            int(com_object),
            [str(i) for i in out_prop_names.value],
            [SWCustomInfoTypeE(i) for i in out_prop_types.value],
            [str(i) for i in out_prop_values.value],
            [SWCustomInfoGetResultE(i) for i in out_prop_resolved.value],
            [int(i) for i in out_prop_link.value],
        )

    def get_names(self) -> List[str]:
        """
        Gets the names of the custom properties.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetNames.html
        """
        com_object = self.com_object.GetNames
        return [str(i) for i in com_object] if com_object else []

    def get_type2(self, field_name: str) -> SWCustomInfoTypeE:
        """
        Gets the type of the specified custom property for a configuration or model document.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetType2.html
        """
        return SWCustomInfoTypeE(self.com_object.GetType2(field_name))

    def link_property(
        self, field_name: str, field_link: bool
    ) -> SWCustomLinkSetResultE:
        """
        Sets whether to link or unlink the specified custom property to or from its parent part.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~LinkProperty.html
        """
        return SWCustomLinkSetResultE(
            self.com_object.LinkProperty(field_name, field_link)
        )

    def set2(self, field_name: str, field_value: str) -> SWCustomInfoSetResultE:
        """
        Sets the value of the specified custom property.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set2.html
        """
        return SWCustomInfoSetResultE(self.com_object.Set2(field_name, field_value))
