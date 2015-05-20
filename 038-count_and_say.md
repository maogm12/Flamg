# 038-Count and Say

## Problem

> The count-and-say sequence is the sequence of integers beginning as follows:
`1`, `11`, `21`, `1211`, `111221`, ...

> `1` is read off as `"one 1"` or `11`.  
> `11` is read off as `"two 1s"` or `21`.  
> `21` is read off as `"one 2, then one 1"` or `1211`.  
> Given an integer `n`, generate the nth sequence.

> Note: The sequence of integers will be represented as a string.

## Solution

- 递归

    1. 如果 n 等于 1，直接返回 1
    2. 如果 n 大于 1，先求出 n-1 对应的字符串，然后遍历这个字符串统计生成新字符串返回

    这个很容易改成迭代版本


## Code

### Python

```python

```

### C++

```cpp
string countAndSay(int n) {
    if (n == 1) {
        return "1";
    }
    string n_1 = countAndSay(n - 1);
    string res = "";
    int counter = 1;
    for (int i = 1; i < n_1.size(); ++i) {
        if (n_1[i - 1] == n_1[i]) {
            ++counter;
        } else {
            res += to_string(counter) + n_1[i - 1];
            counter = 1;
        }
    }
    res += to_string(counter) + n_1[n_1.size() - 1];
    return res;
}
```
