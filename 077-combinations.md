# 077-Combinations

## Problem

> Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

> For example,
If n = 4 and k = 2, a solution is:

>
```
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

## Solution

- 递归，本题需要从1,2,...,n中选择k个数。为了保证选的没有重复性，需要这样考虑，即当第a个数被选择后，剩下的数只能从a+1,...,n中选择。具体过程详细如下：
	- 首先，选第一个数，比如i。
	- 从i+1,...,n中选择剩下的k-1个数。

## Code

### Python

```python
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        self.results = []
        self.combine_nk([], 1, n, k)
        return self.results
    
    def combine_nk(self, result, start, n, k):
        if n - start + 1 < k:
            return
        if k == 0:
            self.results.append(result)
            return
        for i in range(start, n-k+2):
            self.combine_nk(result + [i], i+1, n, k-1)
```

### C++

```cpp

class Solution {
public:
    vector<vector<int> > combine(int n, int k) {
        results.clear();
        vector<int> result;
        combine_nk(result, 1, n, k);
        return results;
    }
    void combine_nk(vector<int> &result, int start, int n, int k) {
        if (n - start + 1 < k) {
            return;
        }
        if (k == 0) {
            results.push_back(result);
            return;
        }
        for (int i = start; i <= n - k + 1; i++) {
            result.push_back(i);
            combine_nk(result, i+1, n, k-1);
            result.pop_back();
        }
    }
private:
    vector<vector<int> > results;
};
```