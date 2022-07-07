from grep import GrepShellCommand
from statistic import Statistic


class LogFile:
    def __init__(self, file_name, base_filter_pattern="^\\S"):
        self._file_name = file_name
        self._grep_command = GrepShellCommand(file_name, base_filter_pattern)

    def map_and_reduce(self, replace_from_pattern, replace_to_pattern):
        return Statistic(
            self._file_name,
            self._grep_command.statistic(
                replace_from_pattern,
                replace_to_pattern
            )
        )
