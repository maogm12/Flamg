# 122-Best Time to Buy and Sell Stock II

## Problem

> Say you have an array for which the i<sup>th</sup> element is the price of a given stock on day i.

> Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

## Solution

- Direct求解：可以无限次的低价进高价出，则需要找出每一个递增序列，然后用该递增序列的最高值减去最低值，加入到收益中。
- 贪心优化：由于递增序列都是连续的，因而也可以看做每次都卖出再买进。以此性质可以简化程序

## Code

### Python Greedy

```python
class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        max_profit = 0
        n = len(prices)
        for i in range(1,n):
            max_profit += max(0, prices[i] - prices[i-1]);
        return max_profit
```

### C++ Direct

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
        
        int j = 1;
        while (j < n) {
            if (prices[j] > low_price) {
                while (j+1 < n && prices[j+1] >= prices[j]) {
                    j++;
                }
                max_profit += prices[j] - low_price;
            } 
            low_price = prices[j];
            j++;
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
        int max_profit = 0;
        int j = 1;
        while (j < n) {
            max_profit += max(0, prices[j] - prices[j-1]);
            j++;
        }
        return max_profit;
    }
};
```