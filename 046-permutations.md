# 046-Permutations

## Problem

> Given a collection of numbers, return all possible permutations.

> For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

    无重复数字的全排列问题

## Solution

- 回溯法。 先确定第一个数字（每一个数字都有可能是排列在第一个位置），
然后是剩下数字的全排列。即本问题，确定第一个数字后，变换成剩下数字的子问题。
具体做法就是，使用一个访问标志数组，来标示当前结果中已经有的数字，
然后对剩下未访问的数组全排列。

## Code

### Python

```python
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        self.results = []
        visited = [0 for i in range(len(num))]
        self.sub_permute(num, visited, [])
        return self.results

    def sub_permute(self, num, visited, result):
        if len(num) == len(result):
            self.results.append(result)
            return
        for i in range(len(num)):
            if visited[i] == 0:
                visited[i] = 1
                self.sub_permute(num, visited, result + [num[i]])
                visited[i] = 0
```

### C++

```cpp
class Solution {
public:
    vector<vector<int> > permute(vector<int> &num) {
        vector<int> visited(num.size(), 0);
        results.clear();
        vector<int> result;
        sub_permute(num, visited, result);
        return results;
    }
    void sub_permute(const vector<int> &num, vector<int> &visited, vector<int> result) {
        if (num.size() == result.size()) {
            results.push_back(result);
        }
        for (int i = 0; i < num.size(); i++) {
            if (visited[i] == 0) {
                visited[i] = 1;
                result.push_back(num[i]);
                sub_permute(num, visited, result);
                result.pop_back();
                visited[i] = 0;
            }
        }
    }
private:
    vector<vector<int> > results;
};
```
