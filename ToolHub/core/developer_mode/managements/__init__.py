from core.developer_mode.managements.commands.basic_commands import (
    HelpCommand,
    AboutCommand,
    CreditsCommand,
    LicenseCommand,
    ExitCommand
)
from core.developer_mode.managements.commands.create import CreatePackageCommand
from core.developer_mode.managements.manager import commands, package_optional_value


class CommandManagements:
    def __init__(self, app_version):
        self.package_directory = 'packages'
        self.app_version = app_version
        self.prompt = None
        self.run_command_loop()

    def run_command_loop(self):
        while True:
            prompt_prefix = f"[~/ToolHub/{self.package_directory}/]" if self.package_directory == 'packages' else f"[{self.package_directory}/]"
            self.prompt = input(f"\n{prompt_prefix} : ")
            self.process_command()

    def process_command(self):
        basic_commands = {
            "help": lambda: print(HelpCommand()),
            "about": lambda: print(AboutCommand(self.app_version)),
            "credits": lambda: print(CreditsCommand()),
            "license": lambda: print(LicenseCommand()),
            "exit": lambda: ExitCommand()
        }

        category, command = self.find_command()

        if category == 'basic.commands' and command in basic_commands:
            basic_commands[command]()
        elif category == 'base.commands' and command == 'package':
            optional_values = set(self.prompt.split()).intersection(package_optional_value)
            if "-c" in optional_values:
                CreatePackageCommand()

    def find_command(self):
        for entry in commands:
            category = next((cat for cat, cmd_set in entry.items() if self.prompt in cmd_set), None)
            if category:
                return category, self.prompt

        prompt_parts = self.prompt.split()
        if "package" in prompt_parts:
            prompt_parts = prompt_parts[1:]
            return "base.commands", "package"

        return None, None
