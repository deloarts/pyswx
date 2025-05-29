"""
PART TOOLS // EXPORT STEP
"""

from pathlib import Path
from typing import Literal

from pyswx.api.sldworks.interfaces.i_document_specification import (
    IDocumentSpecification,
)
from pyswx.api.sldworks.interfaces.i_sldworks import ISldWorks
from pyswx.api.swconst.enumerations import SWSaveAsOptionsE
from pyswx.api.swconst.enumerations import SWSaveAsVersionE
from pyswx.tools.part_tools.open_part import open_part


def export_part(
    swx: ISldWorks,
    part_path: Path,
    export_type: Literal["step"],
    export_path: Path | None = None,
    close_document: bool = False,
    save_document: bool = True,
    document_specification: IDocumentSpecification | None = None,
) -> None:
    """
    Export a SolidWorks part to STEP format.

    Args:
        swx (ISldWorks): The SolidWorks application instance.
        part_path (Path): The path to the SolidWorks part file to be exported.
        export_type (Literal[&quot;step&quot;]): The file type of the exported data.
        export_path (Path | None, optional): The path to the step file. Same location if None. Defaults to None.
        close_document (bool, optional): Whether to close the document after export. Defaults to False.
        save_document (bool, optional): Whether to save the document before closing. Defaults to True.
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
        ValueError: Raised if the active document is not a part.
        FileNotFoundError: Raised if the export fails and the step file does not exist.
    """

    part_model, _ = open_part(
        swx=swx, part_path=part_path, document_specification=document_specification
    )

    if export_path is None:
        export_path = part_model.get_path_name().with_suffix(f".{export_type}")

    part_model.extension.save_as_3(
        name=export_path,
        version=SWSaveAsVersionE.SW_SAVE_AS_CURRENT_VERSION,
        options=SWSaveAsOptionsE.SW_SAVE_AS_OPTIONS_SILENT,
        export_data=None,
        advanced_save_as_options=None,
    )

    if save_document:
        part_model.save_3(options=SWSaveAsOptionsE.SW_SAVE_AS_OPTIONS_SILENT)

    if close_document:
        swx.quit_doc(name=part_model.get_path_name())

    if not export_path.exists():
        raise FileNotFoundError(f"Failed to export STEP file: {export_path}")
