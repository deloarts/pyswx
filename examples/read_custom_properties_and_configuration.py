"""
PYSWX EXAMPLES // READ CUSTOM PROPERTIES AND CONFIGURATION

This example demonstrates how to read custom properties and configuration parameters from a SolidWorks
model document using the PYSWX library.

Prerequisites:
    - An open SolidWorks session with a model document loaded (part or assembly)
    - The model should contain custom properties and configurations
"""

from pyswx import PySWX
from pyswx.api.swconst.enumerations import SWRebuildOnActivationOptionsE

swx = PySWX().application
model = swx.active_doc
assert model is not None, "No active document found"

model = swx.activate_doc_3(
    name=model.get_path_name(),
    use_user_preferences=False,
    option=SWRebuildOnActivationOptionsE.SW_REBUILD_ACTIVE_DOC,
)
active_configuration_name = swx.get_active_configuration_name(model.get_path_name())

custom_property_manager = model.extension.custom_property_manager("")
active_configuration_params = model.configuration_manager.get_configuration_params(
    config_name=active_configuration_name
)
all_configuration_names = model.get_configuration_names()

print(f"Active Document: {model.get_path_name()}")
print(f"Active Configuration: {active_configuration_name}")

print("Custom Properties:")
for prop_name in custom_property_manager.get_names():
    prop = custom_property_manager.get6(prop_name, use_cached=False)
    print(f"    {prop_name}: {prop[2]}")

print("Active Configuration Parameters:")
for config_index, config_param in enumerate(active_configuration_params[1]):
    print(f"    {config_param}: {active_configuration_params[2][config_index]}")

print(f"All Configuration Names:\n    {'\n    '.join(all_configuration_names)}")
