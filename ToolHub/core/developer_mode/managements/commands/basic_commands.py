import sys
from core.developer_mode.managements.base import BasicCommand

class HelpCommand(BasicCommand):
    help = ""

    def __str__(self):
        return f"""Basic commands
- about: {AboutCommand.help}
- credits: {CreditsCommand.help}
- license: {LicenseCommand.help}
- exit: {ExitCommand.help}"""


class AboutCommand(BasicCommand):
    help = "Displays the developer mode information."

    def __init__(self, version):
        self.version = version

    def __str__(self):
        return f"ToolHub [DEVELOPER MODE] - {self.version}\n" \
               f"Developer mode allows users to create tools to integrate into the ToolHub application. If you want to" \
               f" create a tool for ToolHub, we invite you to look in the developer mode documentation on GitHub."


class CreditsCommand(BasicCommand):
    help = "Displays the credits of the application."

    def __str__(self):
        return "Made by KDUser12 on GitHub."


class LicenseCommand(BasicCommand):
    help = "Displays the license belonging to the program."

    def __str__(self):
        return "This application belongs to the MIT License"


class ExitCommand(BasicCommand):
    help = "Exits the program."

    def __init__(self):
        sys.exit(0)
