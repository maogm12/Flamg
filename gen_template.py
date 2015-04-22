#!/usr/bin/env python
# encoding: utf-8

import json
import sys
from os import path
import argparse

def gen_filename(pid, title):
    return "{:0>3}-{}.md".format(pid, "_".join(map(lambda x: x.lower(), filter(lambda x: x, title.split(" ")))))

def fill_content(filename, pid, title):
    with open(filename, 'w') as template:
        template.write("# {:0>3}-{}\n\n".format(pid, title))
        template.write("## Problem\n\n")
        template.write("## Solution\n\n")
        template.write("## Code\n\n")
        template.write("### Python\n\n")
        template.write("```python\n\n```\n\n")
        template.write("### C++\n\n")
        template.write("```cpp\n\n```")

# get problem id
parser = argparse.ArgumentParser(description='Generate markdown template for leetcode')
parser.add_argument("pid", metavar="id", nargs="?", type=int,
                    help="id of problem to deal with")
parser.add_argument("-s", "--search", dest="word", help="word to search")
args = parser.parse_args()
if args.pid is None and args.word is None:
    parser.print_help()
    exit()

if args.word:
    args.word = args.word.lower()

with open("problems.json") as problems_file:
    problems = json.load(problems_file)
    if not args.pid:
        problems = filter(lambda item: item.get("title") and \
                          item["title"].lower().find(args.word) != -1, problems)
        problems = list(problems)
        if not problems:
            print("No such problem whose title containing {}".format(args.word))
        else:
            for problem in problems:
                _pid = problem.get("id", None)
                _title = problem.get("title", None)
                if not _pid or not _title:
                    continue
                print("{:0>3}-{}".format(problem["id"], problem["title"]))
    else:
        for i in range(len(problems)):
            problem = problems[i]
            _pid = problem.get("id", None)
            _title = problem.get("title", None)
            if not _pid or not _title:
                continue
            if _pid == args.pid:
                filename = gen_filename(_pid, _title)
                if path.exists(filename):
                    print("The target file: {} already exists".format(filename))
                    sys.exit()
                fill_content(filename, _pid, _title)
                print("Template generated: {}".format(filename))
                break
        else:
            print("No such problem having id {}".format(args.pid))
