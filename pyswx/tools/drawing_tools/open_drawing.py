"""
DRAWING TOOLS // OPEN DRAWING
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


def open_drawing(
    swx: ISldWorks,
    drawing_path: Path,
    document_specification: IDocumentSpecification | None = None,
) -> Tuple[IModelDoc2, IDrawingDoc]:
    """
    Open a SolidWorks drawing document.

    Args:
        swx (ISldWorks): The SolidWorks application instance.
        part_path (Path): The path to the SolidWorks drawing file to be exported.
        document_specification (IDocumentSpecification | None): The document specification to use. Defaults to None.

    Returns:
        Tuple[IModelDoc2, IDrawingDoc]: A tuple containing the model document and drawing document.

    Remarks:
        The following document specification options are set:
        - document_type: SWDocumentTypesE.SW_DOC_DRAWING
        - use_light_weight_default: True
        - light_weight: True
        - silent: True
        - ignore_hidden_components: True

    Raises:
        Exception: Raised if there is an error opening the document.
        ValueError: Raised if no active document is found.
        ValueError: Raised if the active document is not a drawing.
    """
    drawing_open_spec = swx.get_open_doc_spec(file_name=drawing_path)
    drawing_open_spec.document_type = SWDocumentTypesE.SW_DOC_DRAWING
    drawing_open_spec.use_light_weight_default = True
    drawing_open_spec.light_weight = True
    drawing_open_spec.silent = True
    drawing_open_spec.ignore_hidden_components = True
    drawing_model = swx.open_doc7(
        specification=document_specification or drawing_open_spec
    )

    if drawing_open_spec.warning is not None:
        swx.logger.warning(drawing_open_spec.warning.name)

    if drawing_open_spec.error is not None:
        swx.logger.error(drawing_open_spec.error.name)
        raise Exception(drawing_open_spec.error.name)

    if drawing_model is None:
        raise ValueError("No active document found")

    model_type = drawing_model.get_type()
    if model_type != SWDocumentTypesE.SW_DOC_DRAWING:
        raise ValueError(f"Active document is not a drawing: {model_type.name}")

    drawing_model = swx.activate_doc_3(
        name=drawing_model.get_path_name(),
        use_user_preferences=False,
        option=SWRebuildOnActivationOptionsE.SW_REBUILD_ACTIVE_DOC,
    )

    return drawing_model, IDrawingDoc(drawing_model.com_object)
