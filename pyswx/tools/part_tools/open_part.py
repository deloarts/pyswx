"""
PART TOOLS // OPEN PART
"""

from pathlib import Path
from typing import Tuple

from pyswx.api.sldworks.interfaces.i_document_specification import (
    IDocumentSpecification,
)
from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2
from pyswx.api.sldworks.interfaces.i_part_doc import IPartDoc
from pyswx.api.sldworks.interfaces.i_sldworks import ISldWorks
from pyswx.api.swconst.enumerations import SWDocumentTypesE
from pyswx.api.swconst.enumerations import SWRebuildOnActivationOptionsE


def open_part(
    swx: ISldWorks,
    part_path: Path,
    document_specification: IDocumentSpecification | None = None,
) -> Tuple[IModelDoc2, IPartDoc]:
    """
    Open a SolidWorks part document.

    Args:
        swx (ISldWorks): The SolidWorks application instance.
        part_path (Path): The path to the SolidWorks part file to be exported.
        document_specification (IDocumentSpecification | None, optional): The document specification to use. Defaults to None.

    Returns:
        Tuple[IModelDoc2, IPartDoc]: A tuple containing the model document and part document.

    Remarks:
        The following document specification options are set:
        - document_type: SWDocumentTypesE.SW_DOC_PART
        - use_light_weight_default: True
        - light_weight: True
        - silent: True
        - ignore_hidden_components: True

    Raises:
        Exception: Raised if there is an error opening the document.
        ValueError: Raised if no active document is found.
        ValueError: Raised if the active document is not a part.
    """
    part_open_spec = swx.get_open_doc_spec(file_name=part_path)
    part_open_spec.document_type = SWDocumentTypesE.SW_DOC_PART
    part_open_spec.use_light_weight_default = True
    part_open_spec.light_weight = True
    part_open_spec.silent = True
    part_open_spec.ignore_hidden_components = True
    part_model = swx.open_doc7(specification=document_specification or part_open_spec)

    if part_open_spec.warning is not None:
        swx.logger.warning(part_open_spec.warning.name)

    if part_open_spec.error is not None:
        swx.logger.error(part_open_spec.error.name)
        raise Exception(part_open_spec.error.name)

    if part_model is None:
        raise ValueError("No active document found")

    model_type = part_model.get_type()
    if model_type != SWDocumentTypesE.SW_DOC_PART:
        raise ValueError(f"Active document is not a part: {model_type.name}")

    part_model = swx.activate_doc_3(
        name=part_model.get_path_name(),
        use_user_preferences=False,
        option=SWRebuildOnActivationOptionsE.SW_REBUILD_ACTIVE_DOC,
    )

    return part_model, IPartDoc(part_model.com_object)
