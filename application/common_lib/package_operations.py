import imp
import os

MODULE_EXTENSIONS = ('.py')


def package_contents(package_name):
    file, pathname, description = imp.find_module(package_name)

    if (file):
        raise ImportError('Not a package: %r', package_name)

    return set([os.path.splitext(module)[0]
                for module in os.listdir(pathname)
                if module.endswith(MODULE_EXTENSIONS)])
