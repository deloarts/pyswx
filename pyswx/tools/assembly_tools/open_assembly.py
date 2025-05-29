"""
ASSEMBLY TOOLS // OPEN ASSEMBLY
"""

from pathlib import Path
from typing import Tuple

from pyswx.api.sldworks.interfaces.i_assembly_doc import IAssemblyDoc
from pyswx.api.sldworks.interfaces.i_document_specification import (
    IDocumentSpecification,
)
from pyswx.api.sldworks.interfaces.i_model_doc_2 import IModelDoc2
from pyswx.api.sldworks.interfaces.i_sldworks import ISldWorks
from pyswx.api.swconst.enumerations import SWDocumentTypesE
from pyswx.api.swconst.enumerations import SWRebuildOnActivationOptionsE


def open_assembly(
    swx: ISldWorks,
    assembly_path: Path,
    document_specification: IDocumentSpecification | None = None,
) -> Tuple[IModelDoc2, IAssemblyDoc]:
    """
    Open a SolidWorks assembly model.

    Args:
        swx (ISldWorks): The SolidWorks application instance.
        assembly_path (Path): The path to the SolidWorks assembly file to be exported.
        document_specification (IDocumentSpecification | None): The document specification to use. Defaults to None.

    Returns:
        Tuple[IModelDoc2, IPartDoc]: A tuple containing the model document and assembly document.

    Remarks:
        The following document specification options are set:
        - document_type: SWDocumentTypesE.SW_DOC_ASSEMBLY
        - use_light_weight_default: True
        - light_weight: True
        - silent: True
        - ignore_hidden_components: True
        - view_only: False

    Raises:
        Exception: Raised if there is an error opening the document.
        ValueError: Raised if no active document is found.
        ValueError: Raised if the active document is not an assembly.
    """
    assembly_open_spec = swx.get_open_doc_spec(file_name=assembly_path)
    assembly_open_spec.document_type = SWDocumentTypesE.SW_DOC_ASSEMBLY
    assembly_open_spec.use_light_weight_default = True
    assembly_open_spec.light_weight = True
    assembly_open_spec.silent = True
    assembly_open_spec.ignore_hidden_components = True
    assembly_open_spec.view_only = False
    assembly_model = swx.open_doc7(
        specification=document_specification or assembly_open_spec
    )

    if assembly_open_spec.warning is not None:
        swx.logger.warning(assembly_open_spec.warning.name)

    if assembly_open_spec.error is not None:
        swx.logger.error(assembly_open_spec.error.name)
        raise Exception(assembly_open_spec.error.name)

    if assembly_model is None:
        raise ValueError("No active document found")

    model_type = assembly_model.get_type()
    if model_type != SWDocumentTypesE.SW_DOC_ASSEMBLY:
        raise ValueError(f"Active document is not an assembly: {model_type.name}")

    assembly_model = swx.activate_doc_3(
        name=assembly_model.get_path_name(),
        use_user_preferences=False,
        option=SWRebuildOnActivationOptionsE.SW_REBUILD_ACTIVE_DOC,
    )

    return assembly_model, IAssemblyDoc(assembly_model.com_object)
