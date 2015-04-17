# 026-Remove Duplicates from Sorted Array

## Problem

> Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
>
> Do not allocate extra space for another array, you must do this in place with constant memory. 
> 
> For example,
>  Given input array A = [1,1,2], 
>  
> Your function should return length = 2, and A is now [1,2]. 

去除有序数组里面的重复的元素，原地修改，返回新长度。

## Solution

- Loop

	数组已经是有序的了，直接从前往后遍历，保留一个不含重复元素的数组尾部指针，每遇到不同的数就更新这个尾部指针。
	
	一句话：遍历，把不同的数填到前面去。

## Code

### Python

```python
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0
        
        newSize = 0
        for i in xrange(1, len(A)):
            if A[newSize] != A[i]:
                newSize += 1
                A[newSize] = A[i]
        return newSize + 1
```

### C++

```cpp
class Solution {
public:
    int removeDuplicates(int A[], int n) {
        int newSize = 0;
        for (int i = 1; i < n; ++i) {
            if (A[newSize] != A[i]) {
                A[++newSize] = A[i];
            }
        }
        
        // 注意这个空数组的情况 ==
        return n == 0 ? 0 : newSize + 1;
    }
};
```