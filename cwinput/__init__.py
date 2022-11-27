import platform

__version__ = "0.1"

if platform.system() != "Windows":
    raise OSError

from . import __main__
