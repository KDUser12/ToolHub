from utils.version import get_version
from app import ToolHub

__version__ = (0, 1, 0, "alpha", 0)
version = get_version(__version__)

if __name__ == '__main__':
    ToolHub(version)
