# 029-Divide Two Integers

## Problem

> Divide two integers without using multiplication, division and mod operator.

> If it is overflow, return `MAX_INT`.

这个是一个很多细节的题，要仔细检查边界

## Solution

这个题需要考虑很多细节，比如小明就踩了好多坑，某天，小明（M）来面试，面试官（Z)。

Z: 我们来做个 a/b 的题吧  
M: 好

```cpp
int divide(int divident, int dividor) {
    return divident / dividor;
}
```

Z: 汗！滚犊子！容我说完，不用乘法，除法和求模  
M: 哦

> **首先弄清楚题目各个坑**

M: 那我们就只能用加减法来模拟了  
Z: 恩，可以  
M: 数字都是整数还是浮点数，结果要求是整数还是浮点数
Z: 都是整数  
M: 我们来举几个例子，比如 `1/0`，恩，除 0 异常要处理，比如 `5 / -3`，我们需要处理负数么？  
Z: 需要  
M: 还要处理边界条件，`INT_MAX/INT_MIN` 会不会溢出  
Z: 恩，除 0 和溢出都返回 INT_MAX  
M: 负数处理如果直接使用 abs 求绝对值的话，INT_MIN 会溢出，所以我们需要根据结果符号的不同，来决定是相加还是相减

```cpp
int divide(int dividend, int dividor) {
	if (dividor == 0) return INT_MAX;
	if (dividend == 0) return 0;
	int result = 0;
	int sign = checkSign(dividend, dividor);
    // have not same sign, then we use + or - otherwise
	int next = sign > 0 ? dividend - dividor : dividend + dividor;
	while (next == 0 || checkSign(dividend, next) == 1) {
	    dividend = next;
        // check overflow
	    if (result == INT_MAX || result == INT_MIN) return result;
	    result += sign;
	    if (dividend == 0) return result;
	    next = sign > 0 ? dividend - dividor : dividend + dividor;
	}
	return result;
}

// check if the two numbers have same sign or not
int checkSign(int lh, int rh) {
    return lh > 0 && rh > 0 || lh < 0 && rh < 0 ? 1 : -1;
}
```

> 关键要搞清楚的问题
> 1. 数字范围：整数还是浮点数，结果是整数还是浮点数
> 2. 除以 0 怎么处理
> 3. 负数需要处理么
> 4. 溢出怎么处理

Z: 恩，你这样处理符号很麻烦，有没有方法可以直接去绝对值算呢？关键是那个东西能装下 -INT_MIN，你可能需要一些宽一点的类型  
M: 面试管英明！！我们可以用 unsigned int/long long/double 来存，这样就可以只考虑正数了    
Z: 恩。回到刚刚你的解法，这个解法看起来是可行的，但是有点慢了，对于一个 `INT_MAX / 1` 要循环几十亿次，有什么方法优化么  
M: 关键是我们每次都减一个 dividor，我们可以每次多减去一些 dividor，我们每次减去两个 dividor，我们的结果每次就可以增加 2  
Z: 那你怎么得到每次减多少 dividor 呢？
M: 我们可以维护一个表，记录 n 个 dividor 的结果 dividor * n  
Z: 不能用乘法哦  
M: 那我们就只能用位运算，取 n 为 2 的幂，比如 25 / 3，我们保存维护数组 `[3, 6, 12, 24]`，这样我们 25 - 24 = 1，就可以直接加 2^3 = 8  

## Code

### Python

```python

```

### C++

```cpp
int divide(int divident, int dividor) {
	if (dividor == 0) return INT_MAX;
	// 使用 unsigned int，防止 INT_MIN 这个怪胎溢出
	unsigned int udivident = divident >= 0 ? divident : -divident;
	unsigned int udividor = dividor >= 0 ? dividor : -dividor;

	// 我们可以只维护上面所说数组最大的那个数，后面的数可以通过 /2 得到
	int dtime = 0;
	unsigned int timesDividor = udividor;
	while (timesDividor <= udivident >> 1) {
		dtime += 1;
		timesDividor <<= 1;
	}

	unsigned int result = 0;
	while (dtime >= 0) {
		while (udivident >= timesDividor) {
			udivident -= timesDividor;
			result += 1 << dtime;
		}
		dtime -= 1;
		timesDividor >>= 1;
	}

	// 还要处理溢出: INT_MIN / -1
	return ((divident ^ dividor) >> 31) ? -result : (result > INT_MAX ? INT_MAX : result);
}
```
