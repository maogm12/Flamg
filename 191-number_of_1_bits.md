# 191-Number of 1 Bits

## Problem

> Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

> For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.

## Solution

位操作

## Code

### Python

```python
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
		result = 0
		i = 0
		while i < 32:
			value = (n >> i) & 1
			if value == 1:
				result += 1
			i += 1
		return result

```

### C++

```cpp

```