# 065-Valid Number

## Problem

> Validate if a given string is numeric.

> Some examples:
> ```
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
> ```

> Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

## Solution

多和面试官沟通，这题里面边界条件超级多，多沟通才能确定哪些条件是需要考虑的，基本上有

1. 前置空格，后置空格
2. 符号，符号后面的空格是否需要考虑
3. 是否一定整数位/小数位，是否可以出现这种的数字 `'.1'` / `'1.'`
4. 科学记数法
5. 科学记数法的符号
6. 考虑各种边界条件，比如：
    1. '.'
    2. 'e'
    3. '1e'
    4. 'e1'

## Code

### Python

```python

```

### C++

```cpp
bool isNumber(string s) {
    if (s.empty()) return false;

    int size = s.size();
    while (size > 0 && isspace(s[size - 1])) --size; // tailing whitespaces
    int i = 0;
    bool hasInt = false;
    bool hasFrac = false;

    // skip whitespaces
    while (i < size && isspace(s[i])) ++i;
    if (i == size) return false;  // ' '

    // sign
    if (s[i] == '+' || s[i] == '-') ++i;
    if (i == size) return false; // '+' / '-'

    // integer
    while (i < size && isdigit(s[i])) {
        hasInt = true;
        ++i;
    }
    if (i == size) return hasInt;

    // dot
    if (s[i] != '.' && s[i] != 'E' && s[i] != 'e') return false;
    if (s[i] == '.') {
        ++i;
        // if (i == size) return false;  // '1.'

        // fraction
        while (i < size && isdigit(s[i])){
            hasFrac = true;
            ++i;
        }
        if (i == size) return hasInt || hasFrac;
    }

    // e/E
    if (s[i] != 'e' && s[i] != 'E') return false;
    ++i;
    if (!hasInt && !hasFrac || i == size) return false;

    // sign
    if (s[i] == '+' || s[i] == '-') ++i;
    if (i == size || !isdigit(s[i])) return false;  // '1e-' / '1e+' / '1e'

    // numbers
    while (i < size && isdigit(s[i])) ++i;
    return i == size;
}
```
