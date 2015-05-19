# 151-Reverse Words in a String

## Problem

> Given an input string, reverse the string word by word.

> For example,
> 
> Given s = `"the sky is blue"`,

> return `"blue is sky the"`.

> **Update (2015-02-12)**:
> 
> For C programmers: Try to solve it in-place in O(1) space.

## Solution

- Solution 1	
	- 把多余的空格去掉；
	- 把整个字符串反转；
	- 以单词为单位再反转
- Solution 2
	- 把所有单词存储起来，成为数组
	- 反转单词数组
	- 拼接

## Code

### Python

```python
class Solution:
    # @param s, a string
    # @return a string
	def reverseWords(self, s):
		words = []
		i = 0
		pre_index = 0
		while i <= len(s):
			if i == len(s) or s[i] == ' ':
				word = s[pre_index:i]
				if word != '':
					words.append(word)
				pre_index = i + 1
			i += 1
		words.reverse()
		new_s = ' '.join(words)
		return new_s

```

### C++

```cpp
class Solution {
public:
    void reverseWords(string &s) {
        string new_s = "";
        int length = s.length();
		int start_i = 0;
		int end_i = 0;
		while (end_i < length) {
			if (s[end_i] == ' ') {
				if (start_i == 0 || s[start_i - 1] == ' ') {
					end_i++;
					continue;
				} 
			}
			s[start_i++] = s[end_i++];
		}
        s = s[start_i-1] == ' ' ? s.substr(0, start_i-1): s.substr(0, start_i);
		length = s.length();

        reverse_word(s, 0, length-1);
        int start = 0;
        int end = 0;
        while (end <= length) {
            if (end == length || s[end] == ' ') {
                reverse_word(s, start, end-1);
                start = end+1;
            }
            end++;
        }
    }
    void reverse_word(string &s, int start, int end) {
        while (start < end) {
            char t = s[start];
            s[start++] = s[end];
            s[end--] = t;
        }
    }
};

```