# 080-Remove Duplicates from Sorted Array II

## Problem

> Follow up for "Remove Duplicates":
> What if duplicates are allowed at most twice?
> 
> For example,
> 
> Given sorted array A = [1,1,1,2,2,3], 
> 
> Your function should return length = 5, and A is now [1,1,2,2,3]. 

和 [Remove Duplicates from Sorted Array](./026-remove_duplicates_from_sorted_array.md) 很像，不过这次得到的结果里面允许出现重复元素，不过最多两次。

## Solution

- Loop

    既然语序出现重复元素，我们就需要再前看一个元素，如果填进去造成连续3个元素相等，那么就不行。

## Code

### C++

```cpp
class Solution {
public:
    int removeDuplicates(int A[], int n) {
        if (n <= 2) {
            return n;
        }
        
        int pre = 0, cur = 1;
        for (int i = 2; i < n; ++i) {
            // 不能造成连续三个数一样的情况
            if (A[pre] != A[cur] || A[cur] != A[i]) {
                A[++cur] = A[i];
                pre++;
            }
        }
        
        return cur + 1;
    }
};

```