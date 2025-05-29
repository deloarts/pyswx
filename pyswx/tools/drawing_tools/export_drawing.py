"""
DRAWING TOOLS // EXPORT DRAWING
"""

from pathlib import Path
from typing import Literal

from pyswx.api.sldworks.interfaces.i_document_specification import (
    IDocumentSpecification,
)
from pyswx.api.sldworks.interfaces.i_sldworks import ISldWorks
from pyswx.api.swconst.enumerations import SWExportDataFileType_e
from pyswx.api.swconst.enumerations import SWSaveAsOptionsE
from pyswx.api.swconst.enumerations import SWSaveAsVersionE
from pyswx.tools.drawing_tools.open_drawing import open_drawing


def export_drawing(
    swx: ISldWorks,
    drawing_path: Path,
    export_type: Literal["pdf", "dxf", "dwg"],
    export_path: Path | None = None,
    close_document: bool = False,
    save_document: bool = True,
    view_pdf_afterwards: bool = False,
    document_specification: IDocumentSpecification | None = None,
) -> None:
    """
    Export a SolidWorks drawing to PDF, DXF or DWG.

    Args:
        swx (ISldWorks): The SolidWorks application instance.
        drawing_path (Path): The path to the SolidWorks drawing file to be exported.
        export_type (Literal[&quot;pdf&quot;, &quot;dxf&quot;, &quot;dwg&quot;]): The file type of the exported data.
        export_path (Path | None, optional): The path for the exported file. Same location if None. Defaults to None.
        close_document (bool, optional): Whether to close the document after export. Defaults to False.
        save_document (bool, optional): Whether to save the document before closing. Defaults to True.
        view_pdf_afterwards (bool, optional): Whether to open the PDF after the export. Only relevant for export_type 'pdf'.
        document_specification (IDocumentSpecification | None, optional): The document specification to use. Defaults to None.

    Remarks:
        The following document specification options are set:
        - document_type: SWDocumentTypesE.SW_DOC_PART
        - use_light_weight_default: True
        - light_weight: True
        - silent: True
        - ignore_hidden_components: True

        Document is saved silently.

    Raises:
        ValueError: Raised if no active document is found.
        ValueError: Raised if the active document is not a drawing.
        FileNotFoundError: Raised if the export fails and the exported file does not exist.
    """

    drawing_model, _ = open_drawing(
        swx=swx,
        drawing_path=drawing_path,
        document_specification=document_specification,
    )

    if export_path is None:
        export_path = drawing_model.get_path_name().with_suffix(f".{export_type}")

    export_data = swx.get_export_file_data(
        file_type=SWExportDataFileType_e.SW_EXPORT_PDF_DATA
    )

    if view_pdf_afterwards:
        export_data.view_pdf_after_saving = True

    drawing_model.extension.save_as_3(
        name=Path(export_path),
        version=SWSaveAsVersionE.SW_SAVE_AS_CURRENT_VERSION,
        options=SWSaveAsOptionsE.SW_SAVE_AS_OPTIONS_SILENT,
        export_data=export_data,
        advanced_save_as_options=None,
    )

    if save_document:
        drawing_model.save_3(options=SWSaveAsOptionsE.SW_SAVE_AS_OPTIONS_SILENT)

    if close_document:
        swx.quit_doc(name=drawing_model.get_path_name())

    if not export_path.exists():
        raise FileNotFoundError(f"Failed to export STEP file: {export_path}")
