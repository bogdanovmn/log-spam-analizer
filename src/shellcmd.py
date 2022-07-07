import logging
from subprocess import Popen, PIPE, STDOUT


class ShellCommand:
    _retcode = None
    _output = None

    def __init__(self, command):
        self._command = command

    def execute(self):
        # print "\nRUNNING: %s\n" % self._command
        process = Popen(self._command, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
        self._output = process.stdout.read()
        self._retcode = process.returncode
        return self

    def output(self):
        lines = filter(lambda l: len(l) > 0, self._output.split("\n"))
        return lines
