import platform

__version__ = "0.1.2"

if platform.system() != "Windows":
    raise OSError

from main import CWInput, Key, Keys
