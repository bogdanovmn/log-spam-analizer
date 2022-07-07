from shellcmd import ShellCommand


class GrepShellCommand:
    def __init__(self, target_file, pattern, limit):
        self._file = target_file
        self._pattern = pattern.replace("'", "")
        self._limit = limit

    def execute(self):
        return ShellCommand("%s -m%d" % (self._base_command(), self._limit)).execute().output()

    def statistic(self, replace_from_pattern, replace_to_pattern):
        result = ShellCommand(
            "%s | sed -r 's,%s,%s,' | sort | uniq -c | sort" % (
                self._base_command(),
                replace_from_pattern,
                replace_to_pattern
            )
        ).execute()
        raw_data = {}
        for raw_stat in result.output():
            components = raw_stat.lstrip().split(" ", 1)
            value = int(components[0])
            key = components[1]
            raw_data[key] = value
        return raw_data

    def _result_count(self):
        return ShellCommand("%s -c" % (self._base_command()))

    def _base_command(self):
        return "grep '%s' %s" % (self._pattern, self._file)
