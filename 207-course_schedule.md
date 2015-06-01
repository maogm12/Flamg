# 207-Course Schedule

## Problem

> There are a total of n courses you have to take, labeled from 0 to n - 1.

> Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

> Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

> For example:
>
	2, [[1,0]]
>	
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
>
	2, [[1,0],[0,1]]
	
> There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

## Solution

拓扑排序之有向图环查找，如果有环则返回False。
可以使用深搜来查找环。

## Code

### Python

```python
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if numCourses == 0:
            return True
        graph = [[] for i in range(numCourses)]
        for item in prerequisites:
            graph[item[1]].append(item[0])
        visited = [False for i in range(numCourses)]
        for i in range(numCourses):
            if not visited[i]:
                visited[i] = True
                if self.circle(graph, i, visited, [i]):
                    return False
        return True
    
    def circle(self, graph, i, visited, cur):
        next_courses = graph[i]
        for next_course in next_courses:
            if next_course in cur:
                return True
            if not visited[next_course]:
                visited[next_course] = True
                if self.circle(graph, next_course, visited, cur + [next_course]):
                    return True
        return False
```

### C++

```cpp

```