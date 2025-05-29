"""
PART TOOLS // OPEN DRAWING
"""

from pathlib import Path
from typing import Tuple

from pyswx.api.sldworks.interfaces.i_document_specification import (
    IDocumentSpecification,
)
from pyswx.api.sldworks.interfaces.i_drawing_doc import IDrawingDoc
from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2
from pyswx.api.sldworks.interfaces.i_sldworks import ISldWorks
from pyswx.api.swconst.enumerations import SWDocumentTypesE
from pyswx.api.swconst.enumerations import SWRebuildOnActivationOptionsE
from pyswx.api.swconst.enumerations import SWSaveAsOptionsE
from pyswx.tools.part_tools.open_part import open_part


def open_associated_drawing(
    swx: ISldWorks,
    part_path: Path,
    close_document: bool = False,
    save_document: bool = True,
    document_specification: IDocumentSpecification | None = None,
) -> Tuple[IModelDoc2, IDrawingDoc]:
    """
    Open the drawing associated with a SolidWorks part file.
    Uses the same name in the same folder as the part file with a .SLDDRW extension.

    Args:
        swx (ISldWorks): The SolidWorks application instance.
        part_path (Path): The path to the SolidWorks part file.
        close_document (bool, optional): Whether to close the part document after export. Defaults to False.
        save_document (bool, optional): Whether to save the part document before closing. Defaults to True.
        document_specification (IDocumentSpecification | None, optional): The document specification to use. Defaults to None.

    Returns:
        Tuple[IModelDoc2, IDrawingDoc]: A tuple containing the model document and drawing document.

    Raises:
        ValueError: Raised if no active document is found.
        ValueError: Raised if the active document is not a part.
        FileNotFoundError: Raised if the drawing file does not exist.
        ValueError: Raised if the active document is not a drawing.
    """

    part_model, _ = open_part(
        swx=swx, part_path=part_path, document_specification=document_specification
    )

    drawing_path = part_model.get_path_name().with_suffix(".SLDDRW")
    if not drawing_path.exists():
        raise FileNotFoundError(f"Drawing file does not exist: {drawing_path}")

    drawing_model = swx.open_doc6(
        file_name=drawing_path, file_type=SWDocumentTypesE.SW_DOC_DRAWING
    )
    drawing_model = swx.activate_doc_3(
        name=drawing_path,
        use_user_preferences=False,
        option=SWRebuildOnActivationOptionsE.SW_REBUILD_ACTIVE_DOC,
    )

    model_type = drawing_model.get_type()
    if model_type != SWDocumentTypesE.SW_DOC_DRAWING:
        raise ValueError(f"Active document is not a drawing: {model_type.name}")

    if save_document:
        part_model.save_3(options=SWSaveAsOptionsE.SW_SAVE_AS_OPTIONS_SILENT)

    if close_document:
        swx.quit_doc(name=part_model.get_path_name())

    return drawing_model, IDrawingDoc(drawing_model.com_object)
