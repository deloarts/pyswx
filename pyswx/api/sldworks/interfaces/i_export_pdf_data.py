"""
IExportPdfData Interface Members

Reference:
https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData_members.html

Status: 🔴
"""

from typing import List

from pythoncom import VT_ARRAY
from pythoncom import VT_BSTR
from pythoncom import VT_I4
from win32com.client import VARIANT

from pyswx.api.base_interface import BaseInterface
from pyswx.api.swconst.enumerations import SWExportDataSheetsToExportE


class IExportPdfData(BaseInterface):
    def __init__(self, com_object):
        super().__init__()
        self.com_object = com_object

    def __repr__(self) -> str:
        return f"IExportPdfData({self.com_object})"

    @property
    def export_as_3d(self) -> bool:
        """
        Gets or sets whether to export this part or drawing document to 3D PDF.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~ExportAs3D.html
        """
        return bool(self.com_object.ExportAs3D)

    @export_as_3d.setter
    def export_as_3d(self, value: bool) -> None:
        """True to export this part or drawing document to 3D PDF, false to not"""
        self.com_object.ExportAs3D = value

    @property
    def view_pdf_after_saving(self) -> bool:
        """
        Gets or sets whether to view the PDF file to which a part or drawing is saved.

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~ViewPdfAfterSaving.html
        """
        return bool(self.com_object.ViewPdfAfterSaving)

    @view_pdf_after_saving.setter
    def view_pdf_after_saving(self, value: bool) -> None:
        """True to view the PDF file, false to not"""
        self.com_object.ViewPdfAfterSaving = value

    def get_sheets(self) -> List[str]:
        """
        Gets the names of the sheets to export.

        Remarks:
        Call IModelDocExtension::SaveAs after calling this method.

        Returns:
        Array of the names of the sheets to export

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetSheets.html
        """
        com_object = self.com_object.GetSheets
        return [sheet for sheet in com_object] if com_object else []

    def get_which_sheets(self) -> SWExportDataSheetsToExportE:
        """
        Gets the drawing sheets to export to PDF.

        Returns:
        Drawing sheets to export to PDF as defined in swExportDataSheetsToExport_e

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~GetWhichSheets.html
        """
        com_object = self.com_object.GetWhichSheets
        return SWExportDataSheetsToExportE(com_object)

    def set_sheets(self, which: SWExportDataSheetsToExportE, sheets: List[str]) -> bool:
        """
        Sets the drawing sheets to export.

        Args:
            which (SWExportDataSheetsToExportE): Drawing sheets to export to PDF as defined in swExportDataSheetsToExport_e
            sheets (List[str]): Array of the names of the drawing sheets to export

        Returns:
            True if the drawings sheets are set to export to PDF, false if not

        Reference:
        https://help.solidworks.com/2024/english/api/sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExportPdfData~SetSheets.html
        """
        in_which = VARIANT(VT_I4, which.value)
        in_sheets = VARIANT(VT_BSTR | VT_ARRAY, [str(sheet) for sheet in sheets])

        com_object = self.com_object.SetSheets(in_which, in_sheets)

        return bool(com_object)
