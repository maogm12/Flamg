# 202-Happy Number

## Problem

> Write an algorithm to determine if a number is "happy".

> A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

> Example: 19 is a happy number

> 1<sup>2</sup> + 9<sup>2</sup> = 82
> 
> 8<sup>2</sup> + 2<sup>2</sup> = 68
> 
> 6<sup>2</sup> + 8<sup>2</sup> = 100
> 
> 1<sup>2</sup> + 0<sup>2</sup> + 0<sup>2</sup> = 1


## Solution


## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> prev_set;
        while (n != 1) {
            if (prev_set.find(n) == prev_set.end()) {
                prev_set.insert(n);
                n = square_digits(n);
            } else {
                return false;
            }
        }
        return true;
        
    }
    int square_digits(int n) {
        int result = 0;
        while (n) {
            int mod = n % 10;
            n = n / 10;
            result += mod * mod; 
        }
        return result;
    }
};
```