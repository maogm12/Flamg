# 047-Permutations II

## Problem

> Given a collection of numbers that might contain duplicates, return all possible unique permutations.

> For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].

    有重复数字的全排列问题

## Solution

- 回溯法。046问题的加强版，因为有重复数字的出现，所以，在本回合`（就是一次递归调用）`中，
重复的数字就可以不用考虑了。
注意，这里指的重复的数字不是说只要在数组中重复出现过的数字，而是添加到结果中时重复的数字。
如`1,2,3,3,4`, 当前结果为`1,2`,那么下一个产生的结果为`1,2,3`,`1,2,3`和`1,2,4`.
这样的重复才算是当前回合的重复。

## Code

### Python

```python
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        map_num = {}
        for number in num:
            map_num.setdefault(number, 0)
            map_num[number] += 1
        self.results = []
        self.sub_permute(map_num, [], len(num))
        return self.results

    def sub_permute(self, map_num, result, len_num):
        if len(result) == len_num:
            self.results.append(result)
        for key in map_num:
            if map_num[key] > 0:
                map_num[key] -= 1
                self.sub_permute(map_num, result + [key], len_num)
                map_num[key] += 1
```

### C++

```cpp
class Solution {
public:
    vector<vector<int> > permuteUnique(vector<int> &num) {
		map<int, int> *map_num = new map<int, int>();
		for(vector<int>::iterator iter = num.begin(); iter != num.end(); iter++) {
			if (map_num->find(*iter) == map_num->end()) {
				(*map_num)[*iter] = 1;
			} else {
				(*map_num)[*iter]++;
			}
		}
		vector<int> result;
		sub_permute(map_num, result, num.size());
		delete map_num;
		return results;
    }

	void sub_permute(map<int, int> *map_num, vector<int> &result, size_t len_num) {
		if (result.size() == len_num) {
			results.push_back(result);
		}
		for(map<int, int>::iterator iter = map_num->begin(); iter != map_num->end(); iter++) {
			if (iter->second > 0) {
				iter->second--;
				result.push_back(iter->first);
				sub_permute(map_num, result, len_num);
				result.pop_back();
				iter->second++;
			}
		}

	}
private:
	vector<vector<int> > results;
};

```

A little improvement, we can use a bool array as a hash table

```cpp
vector<vector<int>> results;

vector<vector<int>> permuteUnique(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int size = nums.size();
    if (size == 0) {
        return results;
    }

    bool used[size];  // hash table
    memset(used, false, size);

    vector<int> prefix;
    gen(nums, used, prefix);
    return results;
}

void gen(vector<int> &nums, bool used[], vector<int>& prefix) {
    if (prefix.size() == nums.size()) {
        results.push_back(prefix);
        return;
    }

    int before = -1;
    for (int i = 0; i < nums.size(); ++i) {
        if (used[i] || before != -1 && nums[i] == nums[before]) continue;
        before = i;
        prefix.push_back(nums[i]);
        used[i] = true;
        gen(nums, used, prefix);
        prefix.pop_back();
        used[i] = false;
    }
}
```
