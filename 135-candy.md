# 135-Candy

## Problem
> There are N children standing in a line. Each child is assigned a rating value.

> You are giving candies to these children subjected to the following requirements:
> - Each child must have at least one candy.
> - Children with a higher rating get more candies than their neighbors.

> What is the minimum candies you must give?

## Solution

- 两遍搜索法

    因为每个人至少一个糖，我们初始化给每人一个糖。然后：

    1. 从右向左扫描，保证比相邻的左边分数高的人得到的糖果比左边那个人多一个
    2. 从左往边扫描，保证比相邻的右边分数高的人得到的糖果比右边那个人多

    这样就保证了一个小盆友如果比相邻的小盆友分数高，得到的糖果多

    时间复杂度 O(n)，空间复杂度 O(n)

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int candy(vector<int> &ratings) {
        int size = ratings.size();

        // 初始化每人一个
        vector<int> candies(size, 1);

        for (int i = 1; i < size; ++i) {
            if (ratings[i] > ratings[i - 1] && candies[i] <= candies[i - 1]) {
                candies[i] = candies[i - 1] + 1;
            }
        }

        for (int i = size - 2; i >= 0; --i) {
            if (ratings[i] > ratings[i + 1]  && candies[i] <= candies[i + 1]) {
                candies[i] = candies[i + 1] + 1;
            }
        }

        // 计算总糖数
        return accumulate(candies.begin(), candies.end(), 0);
    }
};
```
