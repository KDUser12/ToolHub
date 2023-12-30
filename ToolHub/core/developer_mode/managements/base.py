import platform
from utils.version import (
    PY36,
    PY37,
    PY38,
    PY39,
    PY310,
    PY311,
    PY312
)


class BasicCommand:
    # Metadata about this command.
    help = ""


class BaseCommand:
    # Metadata about this command.
    help = ""

    # Configuration shortcuts that alter various logic.
    require_system_check = False
    require_python_version_check = True

    def __init__(self):
        self.check_system()
        self.check_python_version()

    def check_system(self):
        if self.require_system_check:
            return platform.system()

    def check_python_version(self):
        if self.require_python_version_check:
            supported_versions = [PY36, PY37, PY38, PY39, PY310, PY311, PY312]

            for version in supported_versions:
                if not version:
                    return version
