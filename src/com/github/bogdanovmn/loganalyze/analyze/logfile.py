from common.cached_grep import CachedGrepShellCommand
from statistic import Statistic


class LogFile:
    def __init__(self, file_name, base_filter_pattern="^\\S", use_cache=True):
        self._use_cache = use_cache
        self._file_name = file_name
        self._grep_command = CachedGrepShellCommand(file_name, base_filter_pattern, rewrite=not use_cache)

    def map_and_reduce(self, replace_from_pattern, replace_to_pattern):
        return Statistic(
            self._file_name,
            self._grep_command.statistic(
                replace_from_pattern,
                replace_to_pattern
            ),
            use_cache=self._use_cache
        )
