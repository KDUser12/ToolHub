from datetime import datetime
import calendar
from core.developer_mode.managements import CommandManagements


class DeveloperMode:
    current_time = datetime.now()
    special_time = {
        'year': current_time.year,
        'month': calendar.month_abbr[current_time.month],
        'day': current_time.day,
        'hour': current_time.hour,
        'minute': current_time.minute,
        'second': current_time.second
    }

    def __init__(self, version, system):
        self.version = version
        self.system = system
        self.prompt = None

        print(f"ToolHub {self.version} ({self.special_time['month']} {self.special_time['day']} {self.special_time['year']}, {self.special_time['hour']}:{self.special_time['minute']}:{self.special_time['second']}) [Developer Mode] on {self.system}")
        print('Type "help", "about", "credits" or "license" for more information.')
        CommandManagements(self.version)
