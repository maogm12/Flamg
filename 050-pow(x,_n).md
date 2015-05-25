# 050-Pow(x, n)

## Problem

> Implement pow(x, n).

## Solution

- 暴力算法：一个一个逐步去乘到一起，不过狗都知道这样会超限
- 由底向上的分治：每个n都可以分为2的若干不同幂次之和，比如12=2<sup>2</sup>+2<sup>3</sup>
- 由顶向下的分治：递归的方式将每个n二分，二分之后再二分，直到n=1为止。得到n/2的结果，就可以组合成n的结果了。

## Code

### Python down-to-up

```python
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.my_pow(-n, x)
        else:
            return self.my_pow(n, x)

    def my_pow(self, n, x):
        pows_v = []
        v = x
        pows = 1
        while pows <= n:
            pows_v.append(v)
            v = v*v
            pows += pows
        pows /= 2

        result = 1
        index = len(pows_v) - 1
        while n > 0:
            if pows <= n:
                result *= pows_v[index]
                n -= pows
            pows /= 2
            index -= 1

        return result

```

### python up-to-down

```python
class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.my_pow(-n, x)
        else:
            return self.my_pow(n, x)

    def my_pow(self, n, x):
        if n == 0:
            return 1
        v = self.my_pow(n/2, x)
        if n % 2 == 1:
            return v*x*v
        else:
            return v*v
```

### C++ up-to-down

```cpp
class Solution {
public:
    double myPow(double x, int n) {
        if (n < 0) {
            return 1 / my_pow(x, -n);
        } else {
            return my_pow(x, n);
        }
    }
    double my_pow(double x, int n) {
        if (n == 0) {
            return 1;
        }
        double v = my_pow(x, n/2);
        if (n % 2 == 1) {
            return v * x * v;
        } else {
            return v * v;
        }
    }
};
```

down-to-up

里面有坑

```cpp
double myPow(double x, int n) {
    if (n < 0) {
        return 1/myPow2(x, -n);  // 转成 unsigned int，防止 INT_MIN 溢出！！！
    }
    return myPow2(x, n);
}

double myPow2(double x, unsigned int n) {
    if (n == 0) {
        return 1;
    }

    if (n == 1) {
        return x;
    }

    vector<double> median;
    int i = 1;
    double temp = x;
    median.push_back(x);
    while (i <= n / 2) {  // i < n 的话， i *= 2 可能溢出！！！
        i *= 2;
        temp *= temp;
        median.push_back(temp);
    }

    double result = 1;
    for (int j = median.size() - 1; j >= 0; --j, i /= 2) {
        if (n < i) {
            continue;
        }

        result *= median[j];
        n -= i;

        if (n == 0) {
            break;
        }
    }

    return result;
}
```
