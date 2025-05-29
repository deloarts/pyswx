"""
IModelDocExtension Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html

Status: 🔴
"""

from pathlib import Path

from pythoncom import VT_BSTR
from pythoncom import VT_BYREF
from pythoncom import VT_DISPATCH
from pythoncom import VT_I4
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.sldworks.interfaces.i_advanced_save_as_options import (
    IAdvancedSaveAsOptions,
)
from pyswx.api.sldworks.interfaces.i_custom_property_manager import (
    ICustomPropertyManager,
)
from pyswx.api.sldworks.interfaces.i_export_pdf_data import IExportPdfData
from pyswx.api.swconst.enumerations import SWFileSaveErrorE
from pyswx.api.swconst.enumerations import SWFileSaveWarningE
from pyswx.api.swconst.enumerations import SWSaveAsOptionsE
from pyswx.api.swconst.enumerations import SWSaveAsVersionE


class IModelDocExtension(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IModelDocExtension({self.com_object})"

    def custom_property_manager(self, config_name: str) -> ICustomPropertyManager:
        """
        Gets the custom property information for this configuration.

        Reference:
        https://help.solidworks.com/2018/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.html

        Note:
        In the api definition this is a property, but in the python implementation it is a method, because python
        does not support properties with parameters. The parameter is the configuration name.
        """
        return ICustomPropertyManager(
            self.com_object.CustomPropertyManager(config_name)
        )

    def save_as_3(
        self,
        name: Path,
        version: SWSaveAsVersionE,
        options: SWSaveAsOptionsE | None,
        export_data: IExportPdfData | None,
        advanced_save_as_options: IAdvancedSaveAsOptions | None,
    ) -> bool:
        """
        Saves the active document to the specified name with advanced options.

        Args:
            name (Path): Full pathname of the document to save; the file extension indicates any conversion that should be performed (for example, Part1.igs to save in IGES format) (see Remarks)
            version (SWSaveAsVersionE): Format in which to save this document as defined in swSaveAsVersion_e (see Remarks)
            options (SWSaveAsOptionsE): Option indicating how to save the document as defined in swSaveAsOptions_e (see Remarks)
            export_data (IExportPdfData): IExportPdfData object for exporting drawing sheets to PDF (see Remarks)
            advanced_save_as_options (IAdvancedSaveAsOptions): IAdvancedSaveAsOptions (see Remarks)

        Returns:
        True if the save is successful, false if not

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.html
        """

        in_name = VARIANT(VT_BSTR, str(name))
        in_version = VARIANT(VT_I4, version.value)
        in_options = VARIANT(VT_I4, options.value) if options else VARIANT(VT_I4, 0)
        in_export_data = (
            VARIANT(VT_DISPATCH, export_data.com_object)
            if export_data
            else VARIANT(VT_DISPATCH, None)
        )
        in_advanced_save_as_options = (
            VARIANT(VT_DISPATCH, advanced_save_as_options.com_object)
            if advanced_save_as_options
            else VARIANT(VT_DISPATCH, None)
        )

        out_errors = VARIANT(VT_BYREF | VT_I4, None)
        out_warnings = VARIANT(VT_BYREF | VT_I4, None)

        com_object = self.com_object.SaveAs3(
            in_name,
            in_version,
            in_options,
            in_export_data,
            in_advanced_save_as_options,
            out_errors,
            out_warnings,
        )

        if out_warnings.value != 0:
            out_warnings = SWFileSaveWarningE(value=out_warnings.value)
            self.logger.warning(out_warnings.name)

        if out_errors.value != 0:
            out_errors = SWFileSaveErrorE(value=out_errors.value)
            self.logger.error(out_errors)
            raise Exception(out_errors)

        return com_object
