# 210-Course Schedule II

## Problem

> There are a total of n courses you have to take, labeled from 0 to n - 1.

> Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

> Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

> There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

> For example:
>
	2, [[1,0]]

> There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]
>
	4, [[1,0],[2,0],[3,1],[3,2]]

> There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3]. Another correct ordering is[0,2,1,3].

## Solution

拓扑排序

- 对每一个课程，都计算其前置课程的数目
- 维护一个队列，将所有前置课程数目为0的课程先添加进来
- 对队列中得每个元素，将所有后置课程的前置课程数目减一，然后如果该后置课程的前置数目为0，添加进队列，直到队列中所有元素已遍历完。
- 查看访问过得课程数目是否等于课程总数，如果是，返回结果，否，返回空。

## Code

### Python

```python
class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        pre_count = [0 for i in range(numCourses)]
        graph = [[] for i in range(numCourses)]
        for item in prerequisites:
            graph[item[1]].append(item[0])
            pre_count[item[0]] += 1
        result = []
        for i in range(numCourses):
            if pre_count[i] == 0:
                result.append(i)
        begin = 0
        while begin < len(result):
            course_i = result[begin]
            for post_course in graph[course_i]:
                pre_count[post_course] -= 1
                if pre_count[post_course] == 0:
                    result.append(post_course)
            begin += 1
        if len(result) == numCourses:
            return result
        return []
        
```

### C++

```cpp
class Solution {
public:
    vector<int> findOrder(int numCourses, vector<pair<int, int>>& prerequisites) {
        vector<int> pre_count(numCourses, 0);
        vector<vector<int>> graph(numCourses);
        for (auto it : prerequisites) {
            graph[it.second].push_back(it.first);
            pre_count[it.first]++;
        }
        vector<int> result;
        for (int i = 0; i < numCourses; i++) {
            if (pre_count[i] == 0) {
                result.push_back(i);
            }
        }
        int begin = 0;
        while (begin < result.size()) {
            int course_id = result[begin];
            for (int post_course : graph[course_id]) {
                pre_count[post_course]--;
                if (pre_count[post_course] == 0) {
                    result.push_back(post_course);
                }
            }
            begin++;
        }
        if (result.size() == numCourses) {
            return result;
        }
        result.clear();
        return result;
    }
};
```