# 090-Subsets II

## Problem

> Given a collection of integers that might contain duplicates, S, return all possible subsets.

> Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,2], a solution is:
>
```
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

## Solution

- 回溯法，与078相似，每一个元素都有可能出现或者不出现，但是本题目需要去重。
  - 比如当结果为[1]时，需要添加后面的[2]形成一个新结果，但数组中有两个重复的2，
所以，2只需要加一次即可，那么在添加元素时需要判断是否已经添加过。
  - 上述判断是在本回合中是否已经被添加过，之所以要强调在本回合中，
就是要考虑在结果中，还有[2,2]这样的集合,这点在下面的代码中会有说明

## Code

### Python

```python
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        self.results = []
        self.gen_subset([], S, 0)
        return self.results

    def gen_subset(self, result, S, reached_index):
        self.results.append(result)
        for i in range(reached_index, len(S)):
            // 此处不能用0来代替reached_index，因为那样[2,2]这样的结果就没有了
            if i == reached_index or (i>reached_index and S[i] != S[i-1]):
                self.gen_subset(result + [S[i]], S, i+1)
```

### C++

```cpp
class Solution {
public:
    vector<vector<int> > subsetsWithDup(vector<int> &S) {
        sort(S.begin(), S.end());
        results.clear();
        vector<int> result;
        gen_subset(result, S, 0);
        return results;
    }
    void gen_subset(vector<int> result, vector<int> &S, int reached_index) {
        results.push_back(result);
        for (int i = reached_index; i < S.size(); i++) {
            if (i == reached_index || (i > reached_index && S[i] != S[i-1])) {
                result.push_back(S[i]);
                gen_subset(result, S, i+1);
                result.pop_back();
            }
        }
    }

private:
    vector<vector<int> > results;
};

```
