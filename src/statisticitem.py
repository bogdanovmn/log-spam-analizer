from common.cached_grep import CachedGrepShellCommand


class StatisticItem:
    def __init__(self, key, count, freq_percent, log_file, use_cache):
        self._use_cache = use_cache
        self._log_file = log_file
        self.key = key
        self.count = count
        self.freq_percent = freq_percent

    def examples(self, count):
        return CachedGrepShellCommand(self._log_file, self.key, count, rewrite=not self._use_cache).execute()
