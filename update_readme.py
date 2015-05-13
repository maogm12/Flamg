#!/usr/bin/python
# encoding: utf-8

import os
import os.path
import re

def getAllProblemId():
    ids = []
    for f in os.listdir('.'):
        if not f.endswith('.md') and not f.endswith('.markdown'):
            continue

        try:
            id = int(f[:3])
            ids.append(id)
        except:
            pass
    ids.sort()
    return ids

def genMarks(ids):
    if len(ids) == 0:
        return
    marks = '\n'
    for i in xrange(201):
        checked = 'red.gif' if i + 1 in ids else 'ddd.gif'
        marks += '![%d](./images/%s)\n' % (i + 1, checked)
    marks += '\n'
    return marks

def updateReadme():
    if os.path.exists('./README.md'):
        with open('./README.md', 'r') as readme:
            content = readme.read()
            marks = '## Achievement' + genMarks(getAllProblemId())
            r = re.compile(r'## Achievement.*',re.DOTALL)
            content = r.sub(marks, content)

        with open('./README.md', 'w') as readme:
            readme.write(content)

if __name__ == '__main__':
    updateReadme()
