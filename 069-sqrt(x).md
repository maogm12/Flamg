# 069-Sqrt(x)

## Problem

> Implement int sqrt(int x).

> Compute and return the square root of x.

## Solution

自己实现开方，不过只要实现整数域内的就行，即2的开放为1.4，那么结果就是1。

二分查找，不详述了。不过需要注意的地方在于在判断当前数a是否比b的开方大还是小时，不能用`a×a`与`b`比较，那样会超限。需要用`a`和`b/a`比较。

## Code

### Python

```python
not neccessary for python code. i need to hurry up.
```

### C++

```cpp
class Solution {
public:
    int mySqrt(int x) {
        if (x <= 1) {
            return x;
        }
        return binary_search(0, x/2, x);
    }
    int binary_search(int low, int high, int x) {
        if (high - low <= 1) {
            if ( x / high >= high) {
                return high;
            }
            return low;
        }
        int mid = (high + low) / 2;
        if (mid == x / mid) {
            return mid;
        } else if (mid > x / mid) {
            return binary_search(low, mid - 1, x);
        } else if (mid < x / mid) {
            return binary_search(mid, high, x);
        }
    }
};
```