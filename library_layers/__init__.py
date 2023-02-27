import sys
import importlib
from .loaders import LayersLoader


loader = LayersLoader(filename=__file__)
sys.path.append(loader.layers_path)
modules = importlib.import_module('libraries', package="library_layers.{module_name}".format(module_name=loader.module_name))
sys.modules['library_layers.libraries'] = modules


import library_layers.libraries

