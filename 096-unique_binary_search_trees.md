# 096-Unique Binary Search Trees

## Problem

> Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

> For example,
Given n = 3, there are a total of 5 unique BST's.

>
```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

## Solution

- 假设函数为f，f(n)返回n个节点时的BST的数目。那么，有：
	- f(0) = 1
	- f(1) = 1
	- f(2) = f(0)×f(1) + f(1)×f(0)
	- f(3) = f(0)×f(2) + f(1)×f(1) + f(2)×f(0)
	- ...

以n=3为例，首先，选取一个数做根节点，那么剩下的就分三种情况，一种是左子树有2个节点，右子树有0个节点；一种是左子树有一个节点，右子树有一个节点；一种是左子树有0个节点，右子树有2个节点。此时，问题就切分成了子问题。

## Code

### Python

```python
class Solution:
    # @return an integer
    def numTrees(self, n):
		results = [0 for i in range(n+1)]
		results[0] = 1
		for i in range(1, n+1):
		    for j in range(0, i):
		        results[i] += results[j] * results[i-j-1]
		return results[n]
```

### C++

```cpp
class Solution {
public:
    int numTrees(int n) {
        vector<int> nums(n+1, 0);
        nums[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                nums[i] += nums[j] * nums[i-j-1];
            }
        }
        return nums[n];
    }
};
```