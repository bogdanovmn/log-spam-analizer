from grep import GrepShellCommand


class StatisticItem:
    def __init__(self, key, count, freq_percent, log_file):
        self._log_file = log_file
        self.key = key
        self.count = count
        self.freq_percent = freq_percent

    def examples(self, count):
        return GrepShellCommand(self._log_file, self.key, count).execute().output()
