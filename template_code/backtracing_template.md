## 模板

```
void helper(vector<vector<int>> &results, vector<int> &nums, vector<int> cur, int index) {
		// 一些终止条件，包括何时将当前结果加入最后结果中
		if (index == nums.size()) {
				results.push_back(cur);
				return;
		}
		
		// 一些遍历循环，每一次循环形成一个新状态，然后递归调用
		for (int i = index; i < nums.size(); i++) {
				cur.push_back(nums[i]);
				helper(results, nums, cur, i+1);
				cur.pop_back();
		}
}
```

## 子集

```
class Solution {
public:
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    vector<vector<int> > subsets(vector<int> &nums) {
    	// write your code here
        vector<vector<int>> results;
        vector<int> result;
        generate(results, nums, result, 0);
        return results;
    }
    void generate(vector<vector<int>> &results, vector<int> &nums, vector<int> &cur, int index) {
    		// 后面的元素通通都不要的情况
        results.push_back(cur);
        
        if (index == nums.size()) {
            return;
        }
        
        // 后面的元素取某个位置的情况
        for (int i = index; i < nums.size(); i++) {
            cur.push_back(nums[i]);
            generate(results, nums, cur, i+1);
            cur.pop_back();
        }
        
    }

};
```

## 带重复的子集

```
class Solution {
public:
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    vector<vector<int> > subsetsWithDup(const vector<int> &S) {
        // write your code here
        vector<int> nums(S.begin(), S.end());
        sort(nums.begin(), nums.end());
        vector<vector<int>> results;
        vector<int> result;
        generate(results, nums, result, 0);
        return results;
    }
    void generate(vector<vector<int>> &results, vector<int> &S, vector<int> &cur, int pos) {
    
    		// 后面的情况通通都不要的情况
        results.push_back(cur);
        if (pos == S.size()) {
            return;
        }
        
        // 后面的情况得要，但是得排除重复情况
        for (int i = pos; i < S.size(); i++) {
            if (i > pos && S[i] == S[i-1]) {
                continue;
            }
            cur.push_back(S[i]);
            generate(results, S, cur, i+1);
            cur.pop_back();
        }
    }
};

```

## 数字组合

```
class Solution {
public:
    /**
     * @param candidates: A list of integers
     * @param target:An integer
     * @return: A list of lists of integers
     */
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) {
        // write your code here
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> results;
        vector<int> result;
        helper(results, candidates, result, 0, 0, target);
        return results;
    }
    void helper(vector<vector<int>> &results, vector<int> &candidates, vector<int> cur, int index, int cur_sum, const int &target) {
    		// 如果等于当前和等于目标值，就将当前数组加入最后结果
        if (cur_sum == target) {
            results.push_back(cur);
            return;
        } 
        
        // 越过了最后一个元素，停止
        if (index >= candidates.size()) {
            return;
        }
        
        // 将当前元素的各种情况考虑进去，不考虑当前元素，考虑加入1个、2个、3个等等
        while (cur_sum <= target) {
            helper(results, candidates, cur, index+1, cur_sum, target);
            cur_sum += candidates[index];
            cur.push_back(candidates[index]);
        }
    }
};

```

## 数字组合2

```
class Solution {
public:
	/**
	 * @param num: Given the candidate numbers
	 * @param target: Given the target number
	 * @return: All the combinations that sum to target
	 */
    vector<vector<int> > combinationSum2(vector<int> &num, int target) {
        // write your code here
        sort(num.begin(), num.end());
        vector<vector<int>> results;
        vector<int> result;
        helper(results, num, result, 0, 0, target);
        return results;
    }
    
    void helper(vector<vector<int>> &results, vector<int> &num, vector<int> &cur, int pos, int cur_sum, const int target) {
        if (cur_sum == target) {
            results.push_back(cur);
            return;
        }
        if (pos >= num.size()) {
            return;
        }
        
        for (int i = pos; i < num.size() && cur_sum + num[i] <= target; i++) {
            if (i > pos && num[i] == num[i-1]) {
                continue;
            }
            cur.push_back(num[i]);
            helper(results, num, cur, i+1, cur_sum+num[i], target);
            cur.pop_back();
        }
    }
};

```

## 组合

```
class Solution {
public:
    /**
     * @param n: Given the range of numbers
     * @param k: Given the numbers of combinations
     * @return: All the combinations of k numbers out of 1..n
     */
    vector<vector<int> > combine(int n, int k) {
        // write your code here
        vector<vector<int>> results;
        vector<int> result;
        helper(results, result, 1, n, k);
        return results;
    }
    
    void helper(vector<vector<int>> &results, vector<int> &cur, int pos, int n, int k) {
        if (cur.size() == k) {
            results.push_back(cur);
            return;
        }
        if (pos > n) {
            return;
        }
        helper(results, cur, pos+1, n, k);
        cur.push_back(pos);
        helper(results, cur, pos+1, n, k);
        cur.pop_back();
    }
};
```

