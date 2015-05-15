# 012-Integer to Roman

## Problem

> Given an integer, convert it to a roman numeral.

> Input is guaranteed to be within the range from 1 to 3999.

数字转罗马数字

## Solution

罗马数字有一些基础字母，然后通过加减运算来组成数字，具体请查看 [Wikipedia](http://en.wikipedia.org/wiki/Roman_numerals)。当时的人怎么发明了这么蛋疼的计数方法。。。

字母对应十进制数字有

| 字母 | 十进制数字 |
| :--- | :------- |
| I    | 1        |
| V    | 5        |
| X    | 10       |
| L    | 50       |
| C    | 100      |
| D    | 500      |
| M    | 1000     |

比如 `2014` 就是 `MMXIV`，就是 1000 + 1000 + 10 + (5 - 1)

计算的时候我们按上面的表格按贪心算法减，不过有一点要注意就是 4 和 9 比较坑爹，我们可以在查找表里面加上 4 和 9

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    string intToRoman(int num) {
        // 加上 4、9 方便处理
        unordered_map<int, string> lut({
		{1, "I"},
		{4, "IV"},
		{5, "V"},
		{9, "IX"},
		{10, "X"},
		{40, "XL"},
		{50, "L"},
		{90, "XC"},
		{100, "C"},
		{400, "CD"},
		{500, "D"},
		{900, "CM"},
		{1000, "M"}
	});
	vector<int> base({1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1});

	string roman;
	while (num > 0) {
		int i = 0;
		while (i < base.size() && base[i] > num) {
			++i;
		}
		roman += lut[base[i]];
		num -= base[i];
	}
	return roman;
    }
};
```
