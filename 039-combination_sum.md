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
```
[7]
[2, 2, 3]
```

## Solution

- 回溯：每个数都可以出现多次，为了遍历所有的情况，需要在回溯过程中保存一个指示器，标明只能选择该指示器位置及以后的数。
	
	初始状态下指示器为0，代表可以选择数组中任何位置的数，此时，
	- 选择位置为0的数，代表下一次选择还可以从位置为0上选，这就意味着涵盖了位置0上的数可以在结果中出现无数次。
	- 选择位置为i(i>0)的数，代表下一次选择只能从i及以后的位置上选，此时涵盖了所有位置0上的数在不出现的结果。
	- 以此类推

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