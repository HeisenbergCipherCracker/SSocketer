from enum import Enum
import platform

class Platforms(Enum):
    LINUX : bool = platform.system().lower() == "linux"
    WINDOWS : bool = platform.system().lower() == "windows"
    MAC : bool = platform.system().lower() == "darwin"

