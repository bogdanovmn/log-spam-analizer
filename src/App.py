#!/usr/bin/env python

import argparse

from analyze.logfile import LogFile

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
argsParser.add_argument(
    '-e', '--show-examples',
    help="show example instances for each finding",
    required=False,
    default=False,
    action='store_true'
)
argsParser.add_argument(
    '-r', '--rewrite-cache',
    help="rewrite cache for the run",
    required=False,
    default=False,
    action='store_true'
)
args = argsParser.parse_args()


log_file = LogFile(args.log_file, " INFO ", use_cache=not args.rewrite_cache)
statistic = log_file.map_and_reduce(
    replace_from_pattern=".*\\s(\\S+\\.java:[0-9]+).*",
    replace_to_pattern="\\1",
)
statistic.print_top(
    int(args.freq_limit),
    args.show_examples
)
