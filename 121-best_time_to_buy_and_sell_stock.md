# 121-Best Time to Buy and Sell Stock

## Problem

> Say you have an array for which the i<sup>th</sup> element is the price of a given stock on day i.

> If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

## Solution

- Direct解法：股票自然是要低价进，高价出。于是问题转化为在某个时间点，购买该时间点之前的最低价格的股票，在该时间点之后的最高价格时卖出。
- 贪心优化：在程序实现时，保存当前时间点的最低价，并不需要如Direct解法那样求出该时间以后的最高价格，而是继续向后遍历，若之后并没有比当前时间点更低的价格，那么最小值一直保持在该时间点，而最高值也会被遍历得到。所以不会遗漏最优解。

## Code

### Python Greedy

```python
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        len_n = len(prices)
        if len_n <= 1:
            return 0
        low_price = prices[0]
        max_profit = 0
        for j in range(1, len_n):
            max_profit = max(max_profit, prices[j] - low_price)
            low_price  = min(low_price,  prices[j])
        return max_profit
```

### C++ Directly  

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n <= 1) {
            return 0;
        }
        vector<int> max_to_end(n, 0);
        vector<int> min_to_begin(n, 0);
        max_to_end[n-1] = prices[n-1];
        min_to_begin[0] = prices[0];
        for(int j = n-2; j >= 0; j--) {
            max_to_end[j] = max(prices[j], max_to_end[j+1]);
        }
        for(int j = 1; j < n; j++) {
            min_to_begin[j] = min(prices[j], min_to_begin[j-1]);
        }
        int max_profit = 0;
        for(int j = 0; j < n-1; j++) {
            if (max_to_end[j+1] - min_to_begin[j] > max_profit) {
                max_profit = max_to_end[j+1] - min_to_begin[j];
            }
        }
        return max_profit;
    }
};
```

### C++ Greedy

```cpp
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n <= 1) {
            return 0;
        }
        int max_profit = 0;
        int low_price = prices[0];
        for(int j = 1; j < n; j++) {
            max_profit = max(max_profit, prices[j] - low_price);
            low_price  = min(low_price,  prices[j]);
        }
        return max_profit;
    }
};
```