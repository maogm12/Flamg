# 150-Evaluate Reverse Polish Notation

## Problem

> Evaluate the value of an arithmetic expression in [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).

> Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression.

> Some examples:
> ```
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
> ```

## Solution

逆波兰式解析使用栈解析

## Code

### Python

```python

```

### C++

```cpp
int evalRPN(vector<string>& tokens) {
    stack<int> s;
    for (auto token: tokens) {
        if (token == "+") {
            int rh = s.top(); s.pop();
            int lh = s.top(); s.pop();
            s.push(lh + rh);
        } else if (token == "-") {
            int rh = s.top(); s.pop();
            int lh = s.top(); s.pop();
            s.push(lh - rh);
        } else if (token == "*") {
            int rh = s.top(); s.pop();
            int lh = s.top(); s.pop();
            s.push(lh * rh);
        } else if (token == "/") {
            int rh = s.top(); s.pop();
            int lh = s.top(); s.pop();
            s.push(lh / rh);
        } else {
            s.push(atoi(token.c_str()));
        }
    }
    return s.top();
}
```
