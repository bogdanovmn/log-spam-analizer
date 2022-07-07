#!/usr/bin/env python

import argparse

from logfile import LogFile

argsParser = argparse.ArgumentParser()
argsParser.add_argument(
    '-f', '--log-file',
    help="target log file",
    required=True
)
argsParser.add_argument(
    '-l', '--freq-limit',
    help="frequency occurrence in percent limit",
    required=False,
    default=5
)
args = argsParser.parse_args()


log_file = LogFile(args.log_file)
statistic = log_file.map_and_reduce(
    replace_from_pattern=".*\\s(\\S+\\.java:[0-9]+).*",
    replace_to_pattern="\\1",
)
statistic.print_top(int(args.freq_limit))
