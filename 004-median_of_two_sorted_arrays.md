# 004-Median of Two Sorted Arrays

## Question

> There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

找两个有序数组的中位数，中位数好求，就是排好序后最中间的那个数（偶数个数的话，中间两个数的平均）。

## Solution

- Brout-Force

	得到排序后的数组，这两个数组已经是有序的，所以使用归并排序即可。归并排序的复杂度是 O(m + n)，空间复杂度 O(m + n)。不展开了。这个算法用来找第 `k` 大的元素也可以，上天给了暴力算法超长的执行时间，大部分时候也会给他比较 nb 的适用范围。

- Search
	
	但是其实我们是不需要去排序的，我们可以直接搜索，就是找第 `(m + n) / 2` 大的元素嘛，我们使用两个指针分别只想两个数组的头部，哪个小就往后移动哪个，直到移动 `(m + n) / 2`个为止，注意偶数情况下要两个数。这个算法用来找第 `k` 大的元素也可以。时间复杂度是 O((m + n) / 2))，没有大的改善，空间复杂度倒是降到了 O(1)。

- Binary Search

	既然都可以搜索了，并且是有序的，那就用二分查找吧。首先中位数右边的数肯定比左边大。我们把数组切成两截，让左边的两截最大值比右边两截最小值小，如果还能保证左边和右边的元素总数相等，那么中位数肯定就在这切口的4个数里面产生。
	
	```	
	A: ***leftA**(a1) | (a2)**rightA***
	B: ***leftB**(b1) | (b2)**rightB***
	```

	然后就看代码吧！我们可以二分查找短的那个数组，时间复杂度降到了 O(min(m, n))

## Code

### Python

wait a minute...

### C++
```cpp
class Solution {
public:
    double findMedianSortedArrays(int A[], int m, int B[], int n) {
        if (m > n) {
            return findMedianSortedArrays(B, n, A, m);
        }
        
        int low = 0, high = m + 1, half = (m + n) / 2;
        bool odd = (m + n) % 2 != 0;
        while (low < high) {
            int midA = (low + high) / 2;
            int midB = half - midA;
            
            if (midA - 1 >= 0 && midB < n && A[midA - 1] > B[midB]) {
                high = midA;
                continue;
            } else if (midB - 1 >= 0 && midA < m && B[midB - 1] > A[midA]) {
                low = midA;
                continue;
            }
            
            int leftMax, rightMin;
            // calc leftMax
            if (midA - 1 >= 0) {
                leftMax = A[midA - 1];
                if (midB - 1 >= 0 && B[midB - 1] > leftMax) {
                    leftMax = B[midB - 1];
                }
            } else {
                if (midB - 1 >= 0) {
                    leftMax = B[midB - 1];
                } else {
                    return n > 0 ? B[0] : 0;
                }
            }
            // calc rightMin
            if (midA < m) {
                rightMin = A[midA];
                if (midB < n && B[midB] < rightMin) {
                    rightMin = B[midB];
                }
            } else {
                if (midB < n) {
                    rightMin = B[midB];
                }
            }
            return odd ? rightMin : (leftMax + rightMin) / 2.0;
        }
    }
};
```
