# 066-Plus One

## Problem

> Given a non-negative number represented as an array of digits, plus one to the number.

> The digits are stored such that the most significant digit is at the head of the list.

## Solution

- 模拟竖式

    模拟竖式，从低位往高位加，然后把结果放到一个数组里，这样的话得到的结果
    是逆序的，结果的时候反过来就可以了

    时间复杂度是 O(n)，目测先分配足够的空间然后往里面填数比翻转要快

## Code

### Python

```python
# 赞 C++ ->_->
```

### C++

```cpp
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> reverseResult;
        int remain = 1;
        for (auto rit = digits.rbegin(); rit != digits.rend(); ++rit) {
            remain = remain + *rit;
            reverseResult.push_back(remain % 10);
            remain /= 10;
        }
        if (remain != 0) {
            reverseResult.push_back(remain);
        }
        reverse(reverseResult.begin(), reverseResult.end());
        return reverseResult;
    }
};
```
