#!/usr/bin/python
# encoding: utf-8

import os
import os.path
import re
import json

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

def genHtml(ids):
    if len(ids) == 0:
        return
    marks = '\n'
    links = '\n'
    linkId = 1
    with open('problems.json') as problems_file:
        problems = json.load(problems_file)
        problems.sort(key = lambda problem: problem.get('id'))
        for problem in problems:
            pid = problem.get('id')
            title = str(pid) + '. ' + problem.get('title')
            href = problem.get('href')
            checked = 'red.gif' if pid in ids else 'ddd.gif'
            marks += '[![%s][%d]][%d]\n' % (title, linkId, linkId + 1)
            links += '  [%d]: ./images/%s (%s)\n'%(linkId, checked, title)
            links += '  [%d]: %s\n'%(linkId + 1, href)
            linkId += 2
        links += '\n'
        return marks + links

def updateReadme():
    if os.path.exists('./README.md'):
        with open('./README.md', 'r', encoding="utf8") as readme:
            content = readme.read()
            marks = '## Achievement' + genHtml(getAllProblemId())
            r = re.compile(r'## Achievement.*',re.DOTALL)
            content = r.sub(marks, content)

        with open('./README.md', 'w', encoding="utf8") as readme:
            readme.write(content)

if __name__ == '__main__':
    updateReadme()
