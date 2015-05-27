# 123-Best Time to Buy and Sell Stock III

## Problem

> Say you have an array for which the ith element is the price of a given stock on day i.

> Design an algorithm to find the maximum profit. You may complete at most two transactions.

> **Note**:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

## Solution

- 将数组拆成两部分，分别对两个部分求最大利润。
- 为了优化，两个部分可以分别用递推算法求得

## Code

### Python

```python
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        len_p = len(prices)
        if len_p <= 1:
            return 0
        max_change = [0 for i in range(len_p)]
        max_change_reverse = [0 for i in range(len_p)]
        min_price = prices[0]
        i = 1
        while i < len_p:
            profit = prices[i] - min_price
            max_change[i] = max(0, max_change[i-1], profit)
            min_price = min(min_price, prices[i])
            i += 1
        max_price = prices[len_p - 1]
        i = len_p - 2
        while i > 0:
            profit = max_price - prices[i]
            max_change_reverse[i] = max(0, max_change_reverse[i+1], profit)
            max_price = max(max_price, prices[i])
            i-= 1
        max_profit = 0
        for i in range(len_p):
            max_profit = max(max_profit, max_change[i] + max_change_reverse[i])
        return max_profit
        
```

### C++

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int len_p = prices.size();
        if (len_p <= 1) {
            return 0;
        }
        vector<int> max_exchange(len_p, 0);
        vector<int> reverse_max_exchange(len_p, 0);
        int min_price = prices[0];
        for (int i = 1; i < len_p; i++) {
            max_exchange[i] = max(max_exchange[i-1], prices[i] - min_price);
            min_price = min(prices[i], min_price);
        }
        int max_price = prices[len_p-1];
        for (int i = len_p - 2; i >= 0; i--) {
            reverse_max_exchange[i] = max(reverse_max_exchange[i+1], max_price - prices[i]);
            max_price = max(prices[i], max_price);
        }
        int max_profit = 0;
        for (int i = 0; i < len_p; i++) {
            max_profit = max(max_profit, max_exchange[i] + reverse_max_exchange[i]);
        }
        return max_profit;
    }
};
```