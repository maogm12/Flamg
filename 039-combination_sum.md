# 039-Combination Sum

## Problem

> Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

> The same repeated number may be chosen from C unlimited number of times.

> Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 

> A solution set is:
> 
`[7]` 
>
`[2, 2, 3]` 

## Solution

- 回溯：每个数都有出现和不出现两种情况，为了遍历所有的情况，需要在回溯过程中保存一个状态，即前m个数中选了c个，其中选中的第c个数就是数组中得第m个数。此时，遍历m个数以后的数组，选择一个，比如选择了第k个，那么状态更新为前k个数中选择了c+1个数。

## Code

### Python

```python
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.results = []
        result = []
        self.combination(result, 0, candidates, 0, target)
        return self.results
    
    def combination(self, result, current_sum, candidates, pre_index, target):
        len_cand = len(candidates)
        for i in range(pre_index, len_cand):
            current_sum += candidates[i]
            if current_sum > target:
                break
            if current_sum == target:
                self.results.append(result + [candidates[i]])
                break
            self.combination(result + [candidates[i]], current_sum, candidates, i, target)
            current_sum -= candidates[i]
      
```

### C++

```cpp

class Solution {
public:
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        sort(candidates.begin(), candidates.end());
        results.clear();
        vector<int> result;
        combination(result, candidates, target, 0, 0);
        return results;
    }
    void combination(vector<int> current, vector<int> &candidates, int target, int current_sum, size_t pre_index) {
        size_t len_candidates = candidates.size();
        for (size_t i = pre_index; i < len_candidates; i++) {
            int num = candidates[i];
            current.push_back(num);
            current_sum += num;
            if (current_sum > target) {
                break;
            }
            if (current_sum == target) {
                results.push_back(current);
                break;
            }
            combination(current, candidates, target, current_sum, i);
            current.pop_back();
            current_sum -= num;
        }
    }
private:
    vector<vector<int> > results;
};

```