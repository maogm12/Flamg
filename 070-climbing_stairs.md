# 070-Climbing Stairs

## Problem

> You are climbing a stair case. It takes n steps to reach to the top.

> Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

## Solution

- 递归

    要爬上第 n 级台阶，要么从第 n - 1 级台阶上去，要么从 n - 2 级台阶上去，递归有木有！
    我们可以保存中间状态的值，大大提高效率。。。

- 循环

    避免了递归的函数调用代价，什么？没有递归直观？忍着！

    时间复杂度为 O(n)，空间复杂度 O(n)

    恩，其实还可以改进的！！！就用两个数记录 n - 1 和 n - 2 记录即可，空间复杂度降为 O(1)

## Code

### Python

```python
# python 发来贺电
```

### C++

递归版本（该版本装逼用的，请看后面的循环版本）

> lambda 大法好！
>
> 碎碎念：`function<int(int)>` 如果能用 `auto` 自动推导类型就好了，不过 `calcWays` 在 auto 推导类型前使用了，所以就只能这么长了

```cpp
class Solution {
public:
    int climbStairs(int n) {
        vector<int> ways(n + 1, -1);
        ways[0] = 1;
        ways[1] = 1;
        function<int(int)> calcWays = [&](int n) -> int {
            if (ways[n] == -1) {
                ways[n] = calcWays(n - 1) + calcWays(n - 2);
            }
            return ways[n];
        };

        return calcWays(n);
    }
};
```

循环版本（代码短多了，妈蛋）

```cpp
class Solution {
public:
    int climbStairs(int n) {
        vector<int> ways(n + 1, -1);
        ways[0] = 1;
        ways[1] = 1;
        for (int i = 2; i < n + 1; ++i) {
            ways[i] = ways[i - 1] + ways[i - 2];
        }
        return ways[n];
    }
};
```

循环版本改进版

```cpp
class Solution {
public:
    int climbStairs(int n) {
        int n_2 = 1;
        int n_1 = 1;
        for (int i = 1; i < n; ++i) {
            int temp = n_2;
            n_2 = n_1;
            n_1 = temp + n_1;
        }
        return n_1;
    }
};
```
