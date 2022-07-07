import hashlib
import json
import os

from grep import GrepShellCommand


class CachedGrepShellCommand:
    _temp_dir = "/tmp/log-spam-analyze"

    def __init__(self, target_file, pattern, limit=5):
        self._grep_command = GrepShellCommand(target_file, pattern, limit)
        self._cache_base_key = hashlib.md5(target_file + pattern + str(limit)).hexdigest()

    def execute(self):
        return self._from_cache(
            "execute",
            lambda: self._grep_command.execute()
        )

    def statistic(self, replace_from_pattern, replace_to_pattern):
        params_key = hashlib.md5(replace_from_pattern + replace_to_pattern).hexdigest()
        result = self._from_cache(
            "statistic" + params_key,
            lambda: self._grep_command.statistic(replace_from_pattern, replace_to_pattern)
        )
        return result

    def _from_cache(self, prefix, value_supplier):
        cache_key = prefix + self._cache_base_key

        if not os.path.exists(self._temp_dir):
            os.makedirs(self._temp_dir)

        cache_file_name = "%s/%s" % (self._temp_dir, cache_key)
        if os.path.exists(cache_file_name):
            cache_file = open(cache_file_name, "r")
            result = json.loads(cache_file.read())
            cache_file.close()
        else:
            cache_file = open(cache_file_name, "w")
            result = value_supplier()
            cache_file.write(json.dumps(result))
            cache_file.close()

        return result



