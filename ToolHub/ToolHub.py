from utils.version import get_version
from app import ToolHubApp

__version__ = (0, 1, 0, "alpha", 0)
tool_version = get_version(__version__)

if __name__ == '__main__':
    ToolHubApp(tool_version)
