# 172-Factorial Trailing Zeroes

## Problem

> Given an integer n, return the number of trailing zeroes in n!.

> **Note**: Your solution should be in logarithmic time complexity.

## Solution

计算5的个数

## Code

### Python

```python

class Solution:
    # @return an integer
    def trailingZeroes(self, n):
		if n == 0:
			return 0
		result = 0
		while n != 0:
			n = n / 5
			result += n
		return result

```

### C++

```cpp

```