import os
import importlib

# Get the path to the modules folder
modules_folder = os.path.join(os.path.dirname(__file__), 'modules')

# Iterate over the files in the modules folder
for file_name in os.listdir(modules_folder):
    # Check if the file is a Python module
    if file_name.endswith('.py') and not file_name.startswith("!"):
        # Remove the file extension to get the module name
        module_name = file_name[:-3]
        
        # Import the module
        module = importlib.import_module(f'modules.{module_name}')
        
        # Check if the module has an on_load function
        if hasattr(module, 'on_load') and callable(module.on_load):
            # Call the on_load function
            module.on_load()