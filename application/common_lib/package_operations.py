import importlib
import pkgutil

PYTHON_MODULES_EXTENSIONS = ('.py')


def list_package_modules(package_name):
    package = importlib.import_module(package_name)
    prefix = package.__name__ + "."

    return [modname.split for importer, modname, ispkg in pkgutil.iter_modules(package.__path__, prefix) if not ispkg]
