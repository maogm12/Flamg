# 204-Count Primes

## Problem

> Description:

> Count the number of prime numbers less than a non-negative number, n.

## Solution

使用一个指示数组，访问当前值时，将其倍数索引处都置为false。没有被置为false的就是质数

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int countPrimes(int n) {
        vector<bool> flags(n, true);
        int counter = 0;
        for (int i = 2; i < n; i++) {
            if (flags[i]) {
                counter++;
                for (int j = i+i; j < n; j += i) {
                    flags[j] = false;
                }
            }
        }
        return counter;
    }
};
```