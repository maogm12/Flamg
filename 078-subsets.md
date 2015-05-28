# 078-Subsets

## Problem

> Given a set of distinct integers, S, return all possible subsets.

> Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If S = [1,2,3], a solution is:


>
```
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

## Solution

- 回溯法，每一种元素都有两种可能，出现或不出现。因而，可以使用递归函数，每次划分两种情况。

- 二进制法

    一个有 `n` 个数字的数组，有 2^n 个子集，因为每个元素有出现/不出现两种情况，所以可以用二进制模拟，
    从 0 - (2^n - 1)，每一个代表一种情况

## Code

### Python

```python
class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        self.results = []
        S.sort()
        self.gen_subset([], S, 0)
        return self.results

    def gen_subset(self, result, S, reached_index):
        self.results.append(result)
        for i in range(reached_index, len(S)):
            self.gen_subset(result + [S[i]], S, i+1)

```

### C++

```cpp

class Solution {
public:
    vector<vector<int> > subsets(vector<int> &S) {
        sort(S.begin(), S.end());
        results.clear();
        vector<int> result;
        gen_subset(result, S, 0);
        return results;
    }
    void gen_subset(vector<int> result, vector<int> &S, int reached_index) {
        results.push_back(result);
        for (int i = reached_index; i < S.size(); i++) {
            result.push_back(S[i]);
            gen_subset(result, S, i+1);
            result.pop_back();
        }
    }
private:
    vector<vector<int> > results;
};

```

Binary
```cpp
vector<vector<int>> subsets(vector<int>& nums) {
    vector<vector<int>> result;
    if (nums.empty()) {
        return result;
    }

    sort(nums.begin(), nums.end());
    int size = nums.size();
    for (int i = 0; i < pow(2, size); ++i) {
        result.push_back(number2set(nums, i));
    }
    return result;
}

vector<int> number2set(vector<int>& nums, int n) {
    int mask = 1;
    vector<int> result;
    for (int i = 0; i < nums.size(); ++i, mask <<= 1) {
        if ((n & mask) != 0) {
            result.push_back(nums[i]);
        }
    }
    return result;
}
```
