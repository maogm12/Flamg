# 040-Combination Sum II

## Problem

> Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

> Each number in C may only be used once in the combination.

> **Note**:
> 
> All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
>
```
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
```

## Solution

- 回溯：每个数都有出现和不出现两种情况，为了遍历所有的情况，需要在回溯过程中保存一个指示器，只能从指示器及之后的数字中选择。指示器初始化为0，此时：
	- 选择位置为0的数，指示器+1。这样包含了所有有位置0的结果。
	- 不选择位置为0的数，指示器+1。这样包含了所有没有位置0上数的结果。

> 与039极为相似，只不过039中描述的指示器在数字被选择后可以不变，而本题必须加1.

> 数组中可能有重复的数字，那么就可能出现重复的结果。比如[2,2,2], target=4，这样，结果中就会有多个[2,2]出现，重复的根源就在于如果第一个2出现了，那么就覆盖了出现1个2的情况，而第一个2没出现，第二个2出现了，那么也是结果中只出现1个2的情况，解决的办法是在选择下一个数时，如果该数的位置大于当前指示器位置，且与前一个数相等，那就忽略它，因为这种情况与前一个数出现而当前数不出现重合了。

> 当然，你也可以去结果中判断，不过这样显得很low，哦不，简直low爆了，虽然我之前就是去结果中检查的。

## Code

### Python

```python
class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        candidates.sort()
        self.results = []
        result = []
        self.combination(result, 0, candidates, 0, target)
        return self.results
    
    def combination(self, result, current_sum, candidates, pre_index, target):
        len_cand = len(candidates)
        for i in range(pre_index, len_cand):
            if i > pre_index and candidates[i] == candidates[i-1]:
                continue
            current_sum += candidates[i]
            if current_sum > target:
                break
            if current_sum == target:
                self.results.append(result + [candidates[i]])
                break
            self.combination(result + [candidates[i]], current_sum, candidates, i+1, target)
            current_sum -= candidates[i]
```

### C++

```cpp
class Solution {
public:
    vector<vector<int> > combinationSum2(vector<int> &candidates, int target) {
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
            if (i > pre_index && num == candidates[i-1]) {
                continue;
            }
            current.push_back(num);
            current_sum += num;
            if (current_sum > target) {
                break;
            }
            if (current_sum == target) {
                results.push_back(current);
                break;
            }
            combination(current, candidates, target, current_sum, i+1);
            current.pop_back();
            current_sum -= num;
        }
    }
private:
    vector<vector<int> > results;
};
```