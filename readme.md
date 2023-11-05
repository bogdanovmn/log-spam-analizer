# About

This is a python wrapper for unix pipe commands: grep, cut, sort, etc for java log statistics.
In case of growing logs you want to know and analyze the reason. This tool is one of the methods to discover a problem.

It was written using Python 2.x for more compatibility and use on old as well as new servers.

# Usage

## Installation 

1. Clone the repo
2. Make an alias 
`loganalyze='/path/to/src/com/github/bogdanovmn/loganalyze/App.py'`
3. Run `loganalyze -h` for usage info

## How it works
* By default, it processes logs in format like `... SomeClassName.java:123 ...` and builds statistics by class name and line number (generally it should be identifier).
* It also uses the `/tmp/log-spam-com.github.bogdanovmn.loganalyze.analyze` directory for the grep result cache (this speeds up similar requests).

## Examples
### Get statistic by all records
```bash
$ loganalyze -f api.log
Top 14/154 findings with occurrence >= 5% (82% total):
----------------------
[ 21%] SomeService.java:44 => 1092453
[ 21%] AnotherService.java:92 => 1085371
[  9%] BlaBlaService.java:144 => 484742
[  6%] FooService.java:30 => 328705
[  5%] BarService.java:141 => 268042
```
### Get statistic by ERROR records only
```bash
$ loganalyze -f api.log -g ERROR
Top 2/21 findings with occurrence >= 5% (98% total):
----------------------
[ 73%] BazService.java:191 => 129771
[ 25%] FooService.java:39 => 44308 
```
Note:
1. `Top 2/21 findings` means that there are 19 more unique ERROR "sources" with a frequency of less than 5%. If you are interested in those as well, there is a special option `-l`.
2. `(98% total)` means that these 2 unique sources (BazService.java:191 & FooService.java:39) make up 98% of all ERROR records.

### Get examples of sources
In some cases, you may want to know more details about these records.
```bash
$ loganalyze -f api-node1.txt -g ERROR -e
Top 2/21 findings with occurrence >= 5% (98% total):
----------------------
[ 73%] DefaultTokenProducer.java:191 => 129771
---
Examples:
2023-11-01 08:00:00.795 ERROR [http-nio-8443-exec-121] BazService.java:191 Unsupported JWT token: The parsed JWT indicates it was signed with the RS256 signature algorithm, but <...>
2023-11-01 08:00:00.799 ERROR [http-nio-8443-exec-100] BazService.java:191 Unsupported JWT token: The parsed JWT indicates it was signed with the RS256 signature algorithm, but <...>
2023-11-01 08:00:00.807 ERROR [http-nio-8443-exec-99] BazService.java:191 Unsupported JWT token: The parsed JWT indicates it was signed with the RS256 signature algorithm, but <...>
---

[ 25%] SimpleAsyncUncaughtExceptionHandler.java:39 => 44308
---
Examples:
2023-11-01 08:00:01.126 ERROR [longRunningAsyncOperations-53] FooService.java:39 Unexpected exception occurred invoking async method: public void foo.blabla.Klass.method1
2023-11-01 08:00:01.150 ERROR [longRunningAsyncOperations-39] FooService.java:39 Unexpected exception occurred invoking async method: public void foo.blabla.Klass.method2
2023-11-01 08:00:01.201 ERROR [longRunningAsyncOperations-42] FooService.java:39 Unexpected exception occurred invoking async method: public void foo.blabla.Klass.method3

```
