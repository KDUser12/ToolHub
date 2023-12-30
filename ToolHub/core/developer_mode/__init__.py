from datetime import datetime
import calendar
from core.developer_mode.managements import CommandManagements


class DeveloperMode:
    current_time = datetime.now()
    formatted_time = {
        'year': current_time.year,
        'month': calendar.month_abbr[current_time.month],
        'day': current_time.day,
        'hour': current_time.hour,
        'minute': current_time.minute,
        'second': current_time.second
    }

    def __init__(self, app_version, operating_system):
        self.app_version = app_version
        self.operating_system = operating_system
        self.prompt = None

        print(f"ToolHub {self.app_version} ({self.formatted_time['month']} {self.formatted_time['day']} {self.formatted_time['year']}, {self.formatted_time['hour']}:{self.formatted_time['minute']}:{self.formatted_time['second']}) [Developer Mode] on {self.operating_system}")
        print('Type "help", "about", "credits" or "license" for more information.')
        CommandManagements(self.app_version)
