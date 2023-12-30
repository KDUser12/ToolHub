from core.developer_mode.managements.base import BaseCommand


class CreatePackageCommand(BaseCommand):
    help = "Command allowing the user to create his own package."

    def __init__(self):
        super().__init__()

        # Collect STR data :
        self.package_name = input("[*] Package name : ")
        self.version = input("[*] Version : ")
        self.author = input("[*] Author : ")

        # Collect BOOL data :
        self.python_version_required = input("\n[-] Python tool version required : ")
        self.system_required = self.input_list("[-] Type of system required : ")
        self.command_line = self.input_boolean("[-] Called from command line : ")
        self.program_console = self.input_boolean("[-] Called from the program console : ")

        self.python_versions_allowed = self.python_version_check()
        self.system_allowed = self.system_check()

        print(self.package_name, self.version, self.author)
        print(self.python_version_required)
        print(self.system_required)
        print(self.command_line, self.program_console)

        print(self.python_versions_allowed, self.system_allowed)

    @staticmethod
    def input_boolean(prompt):
        response = input(prompt)
        return response.lower() == 'true' if response.lower() in {'true', 'false'} else None

    @staticmethod
    def input_list(prompt):
        response = input(prompt)
        return response.split() if response else None

    def python_version_check(self):
        if self.python_version_required:
            self.python_version_required = self.python_version_required.split()

            python_versions = [36, 37, 38, 39, 310, 311, 312]
            unofficial_versions = [int(version) for version in self.python_version_required]
            official_versions = []

            for version in unofficial_versions:
                for python_version in python_versions:
                    if version == python_version:
                        official_versions.append(version)

            occurrences = {}
            value_without_duplicate = []

            for element in official_versions:
                occurrences[element] = occurrences.get(element, 0) + 1
                if occurrences[element] == 1:
                    value_without_duplicate.append(element)

            return value_without_duplicate
        return None

    def system_check(self):
        if self.system_required:
            systems = {'Windows', 'Linux', 'Darwin'}
            return list(systems.intersection(self.system_required))
        return None
