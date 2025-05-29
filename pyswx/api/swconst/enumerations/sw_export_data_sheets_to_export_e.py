"""
swExportDataSheetsToExport_e Enumeration

Reference:
https://help.solidworks.com/2024/english/api/swconst/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swExportDataSheetsToExport_e.html

Status: 🟢
"""

from enum import IntEnum


class SWExportDataSheetsToExportE(IntEnum):
    """Export data sheets to export options."""

    SW_EXPORT_DATA_EXPORT_ALL_SHEETS = 1  # Export all sheets
    SW_EXPORT_DATA_EXPORT_CURRENT_SHEET = 2  # Export only the current sheet
    SW_EXPORT_DATA_EXPORT_SPECIFIED_SHEETS = 3  # Export specified sheets
