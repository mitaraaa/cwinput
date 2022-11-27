import platform

if platform.system() != "Windows":
    raise OSError

from . import __main__
