import platform
import os
import sys
import time
import select
from core.developer_mode import DeveloperMode


class ToolHub:
    system = platform.system()

    def __init__(self):
        self.run_developer_mode()

    def run_developer_mode(self):
        self.clear_all()

        for i in range(5, 0, -1):
            sys.stdout.write(f"Press enter to enter developer mode. ({i})")
            sys.stdout.flush()
            time.sleep(1)
            sys.stdout.write('\r')

            try:
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    sys.stdin.readline()
                    self.clear_all()
                    DeveloperMode()
                    break
            except select.error:
                pass
        sys.stdout.write('\033[K')
        sys.stdout.flush()
        return None

    def clear_all(self):
        if self.system == 'Windows':
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('clear')
        return None
