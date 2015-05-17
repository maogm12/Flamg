# 020-Valid Parentheses

## Problem

> Given a string containing just the characters `'(', ')', '{', '}', '[' `and `']'`, determine if the input string is valid.

> The brackets must close in the correct order, `"()"` and `"()[]{}"` are all valid but `"(]" `and `"([)]"` are not.

## Solution

不解释，直接看代码。

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    bool isValid(string s) {
        stack<char> char_stack;
        for(int i = 0; i < s.length(); i++) {
            if (s[i] == ')') {
                if (!char_stack.empty() && char_stack.top() == '(') {
                    char_stack.pop();
                } else {
                    return false;
                }
            } else if (s[i] == '}') {
                if (!char_stack.empty() && char_stack.top() == '{') {
                    char_stack.pop();
                } else {
                    return false;
                }
            } else if (s[i] == ']') {
                if (!char_stack.empty() && char_stack.top() == '[') {
                    char_stack.pop();
                } else {
                    return false;
                }
            } else {
                char_stack.push(s[i]);
            }
        }
        return char_stack.empty();

    }
};
```

maybe we can create some helper function

```cpp
bool isValid(string s) {
    stack<char> prth;
    for (auto ch : s) {
        switch (ch) {
            case '(':
            case '[':
            case '{':
                prth.push(ch);
                break;
            case ')':
            case ']':
            case '}':
                if (prth.empty() || prth.top() != findPair(ch)) {
                    return false;
                } else {
                    prth.pop();
                }
                break;
            default:
                break;
        }
    }

    return prth.empty();
}

char findPair(char half) {
    switch (half) {
        case ')':
            return '(';
        case ']':
            return '[';
        case '}':
            return '{';
        default:
            return ' ';
    }
}
```
