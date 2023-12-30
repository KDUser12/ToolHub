import platform
import os
import sys
import time
import select
from core.developer_mode import DeveloperMode


class ToolHubApp:
    operating_system = platform.system()

    def __init__(self, app_version):
        self.app_version = app_version
        self.run_developer_mode()

    def run_developer_mode(self):
        self.clear_screen()

        for countdown in reversed(range(1, 6)):
            sys.stdout.write(f"Press enter to enter developer mode. ({countdown})")
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write('\r')

            try:
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    sys.stdin.readline()
                    self.clear_screen()
                    DeveloperMode(self.app_version, self.operating_system)
                    break
            except select.error:
                pass

        sys.stdout.write('\033[K')
        sys.stdout.flush()

    def clear_screen(self):
        os.system('cls' if self.operating_system == 'Windows' else 'clear')
