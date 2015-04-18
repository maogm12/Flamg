#!/bin/python

import json
import sys
from os import path

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
pid = 0
if (len(sys.argv) < 2):
    pid = input("Generate template for which problem[id]: ")
else:
    pid = sys.argv[1]

try:
    pid = int(pid)
except:
    print("Error pid")
    sys.exit()

with open("problems.json") as problems_file:
    problems = json.load(problems_file)
    for i in range(len(problems)):
        problem = problems[i]
        _pid = problem.get("id", None)
        _title = problem.get("title", None)
        if not _pid or not _title:
            continue
        if _pid == pid:
            filename = gen_filename(_pid, _title)
            if path.exists(filename):
                print("The target file: {} already exists".format(filename))
                sys.exit()
            fill_content(filename, _pid, _title)
            print("Template generated: {}".format(filename))
            break
    else:
        print("Error pid")
