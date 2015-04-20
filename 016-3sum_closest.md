# 016-3Sum Closest

## Problem
> Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

> ```
> For example, given array S = {-1 2 1 -4}, and target = 1.
> The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
> ```

由于是计算最接近 target 的和，hash 貌似都不管用了。

## Solution

- Brute Force

    不多说，时间复杂度 O(n^3)，空间复杂度 O(1)

- Binary Search

    枚举前两个数(设为 first 和 second)，若要和最接近，可以假设第三个数为 target - first - second，去二分查找。

    这样时间复杂度为 O(n^2 logn)，空间复杂度为 O(1)

- Search

    依然可以用 3sum 里面那个从两边向中间搜索的方法。

	比如 `[-2,-1,-1,1,1,2]`

	我们枚举 `[-2,-1,-1,1]`，当第一个数选 `-2` 时，我们在右边 `[-1,-1,1,1,2]` 里面从两边往中间搜索。起始位置第二个数即 `-1`，第三个数即 `2`，第二个数往右边取，可以使得结果变大，第三个数往左边来，可以使得结果变小。这样，如果相加结果比大于 target，我们可以让第三个数往左边去一点，反之，我们让第二个书往右边来一点。

	时间复杂度降低到了 O(n^2)，空间复杂度为 O(1)

## Code

### Python

```python
# wait a minute
```

### C++ 相向搜索版

```cpp
class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
        if (num.size() < 3) {
            return -1;
        }

        sort(num.begin(), num.end());
        int maxDiff = INT_MAX;
        int total = num[0] + num[1] + num[2];
        for (auto first = num.begin(); first < num.end() - 2; ++first) {
            auto second = first + 1;
            auto third = num.end() - 1;
            while (second < third) {
                // 不用考虑重复的情况，反而比 3sum 简单多了
                int curTotal = *first + *second + *third;
                int diff = abs(curTotal - target);
                if (diff < maxDiff) {
                    maxDiff = diff;
                    total = curTotal;
                }

                if (curTotal < target) {
                    ++second;
                } else {
                    --third;
                }
            }
        }

        return total;
    }
};
```

### C++ 二分搜索版

**待review！！！！**

```cpp
class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) {
        if (num.size() < 3) {
            return -1;
        }

        sort(num.begin(), num.end());
        int maxDiff = INT_MAX;
        int total = num[0] + num[1] + num[2];
        for (auto first = num.begin(); first < num.end() - 2; ++first) {
            for (auto second = first + 1; second < num.end() - 1; ++second) {
                int perfectThird = target - *first - *second;

                // 二分搜索
                auto third = lower_bound(second + 1, num.end() - 1, perfectThird);
                if (third - 1 > second && perfectThird - *(third - 1) < *third - perfectThird) {
                    --third;
                }

                int curTotal = *first + *second + *third;
                int diff = abs(curTotal - target);
                if (diff < maxDiff) {
                    maxDiff = diff;
                    total = curTotal;
                }
            }
        }

        return total;
    }
};
```
