# 219-Contains Duplicate II

## Problem

> Given an array of integers and an integer k, find out whether there there are two distinct indices i and j in the array such that nums[i] = nums[j] and the difference between i and j is at most k.

## Solution

- Hash

    Iterate the array, use hash to store the last index of some number, if the difference is at most k, then the result is true

## Code

### Python

```python

```

### C++

```cpp
bool containsNearbyDuplicate(vector<int>& nums, int k) {
    unordered_map<int, int> indice;
    for (int i = 0; i < nums.size(); ++i) {
        if (indice.find(nums[i]) != indice.end()) {
            if (i - indice[nums[i]] <= k) {
                return true;
            }
        }
        indice[nums[i]] = i;
    }

    return false;
}
```
