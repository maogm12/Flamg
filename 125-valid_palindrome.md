# 125-Valid Palindrome

## Problem

> Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

> For example,

> `"A man, a plan, a canal: Panama"` is a palindrome.

> `"race a car"` is not a palindrome.

> Note:

> Have you consider that the string might be empty? This is a good question to ask during an interview.

> For the purpose of this problem, we define empty string as valid palindrome.

## Solution

- 相向搜索法

    用两个指针从头和尾同时向中间搜索，发现不同的就可以判断为 false，遇到不是字母或数字的字符就丢弃

    Remember, the check is case-insensitice!

## Code

### Python

```python
class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        low, high = 0, len(s) - 1
        s = s.lower()
        while low <= high:
            if not s[low].isalnum():
                low += 1
            elif not s[high].isalnum():
                high -= 1
            else:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
        return True
```

### C++

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        int low = 0, high = s.size() - 1;
        while (low <= high) {
            if (!isalnum(s[low])) {
                low++;
            } else if (!isalnum(s[high])) {
                high--;
            } else {
                if (tolower(s[low]) != tolower(s[high])) {
                    return false;
                }
                low++;
                high--;
            }
        }

        return true;
    }
};
```
