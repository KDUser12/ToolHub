from core.developer_mode.managements.commands.basic_commands import (
    HelpCommand,
    AboutCommand,
    CreditsCommand,
    LicenseCommand,
    ExitCommand
)

commands = [
            {
                "basic.commands": {
                    "help",
                    "about",
                    "credits",
                    "license",
                    "exit"
                }
            }
        ]


class CommandManagements:
    def __init__(self, version):
        self.version = version
        self.prompt = None
        self.call_command()

    def call_command(self):
        package_directory = '~/ToolHub/packages/'

        while True:
            self.prompt = input(f"\n[{package_directory}] : ")
            self.process_command()

    def process_command(self):
        command, category = self.find_command()
        if category == 'basic.commands':
            basic_commands = [
                {
                    "help": lambda: print(HelpCommand()),
                    "about": lambda: print(AboutCommand(self.version)),
                    "credits": lambda: print(CreditsCommand()),
                    "license": lambda: print(LicenseCommand()),
                    "exit": lambda: ExitCommand()
                }
            ]

            for command_factory in basic_commands:
                for command_name, command_function in command_factory.items():
                    if command_name == self.prompt:
                        command_function()

    def find_command(self):
        for entry in commands:
            for category, command_set in entry.items():
                if self.prompt in command_set:
                    return self.prompt, category

