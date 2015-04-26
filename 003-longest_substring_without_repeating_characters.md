# 003-Longest Substring Without Repeating Characters

## Problem

> Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

## Solution

- 暴力算法，O(n<sup>2</sup>)的时间复杂度，不解释，因为更优的解也十分直观

- 双指示器法

	遍历字符串的每个字符ch，计算以ch为结尾的最长非重复子串。

	那么，这个子串以ch所在位置索引为结尾，以字符串中出现ch的上一个位置的索引+1为开始。
	如`abcad`，当以第二个a为结尾时，那么以第2个a为结尾的最长非重复子串以b为开始。

	此时，就需要两个指示器begin和end，end用来遍历字符串，begin用来指出end位置上的字符的上一个位置。此时，非重复子串长度为end-begin+1.


> 注意：双指示器法是leetcode中比较常用的方法


## Code

### Python

```python
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        len_s = len(s)
        begin = 0
        end = 0
        max_len = 0
        pre_dict = {}
        while end < len_s:
            if s[end] in pre_dict:
                begin = max(begin, pre_dict[s[end]] + 1)
            pre_dict[s[end]] = end
            end += 1
            max_len = max(end-begin, max_len)
        return max_len
```

My name is mgm, <s>I am the fa...</s> 我觉得祥爷的代码可以改进

1. `max_len` 可以不用每次都求值，只有 `begin` 发生变化时求即可
2. 目测祥爷很喜欢用 `while`，感觉这里用 `for` 更方便，因为这里 `end` 在循环里做的唯一修改是自增
3. to be more Pythonic，赋值可以不用写这么多行的
4. 对，我就是来凑 challenge 的 TT

mgm版本

```python
class Solution:
	# @param {string} s
	# @return {integer}
	def lengthOfLongestSubstring(self, s):
		maxLen, begin = 0, 0
		preIndex = {}
		for i in xrange(len(s)):
			if s[i] in preIndex and preIndex[s[i]] >= begin:
				maxLen = max(maxLen, i - begin)
				begin = preIndex[s[i]] + 1
			preIndex[s[i]] = i
		# 注意最后一节，比如 aaabcde
		return max(maxLen, len(s) - begin)
```

### C++

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> pre_index;
        unordered_map<char, int>::iterator find_it;
        int begin = 0, end = 0, max_len = 0;
        int len_s = s.length();
        while (end < len_s) {
            find_it = pre_index.find(s[end]);
            if (find_it != pre_index.end()) {
                begin = max(find_it->second+1, begin);
            }
            pre_index[s[end]] = end;
            end++;
            max_len = max(max_len, end-begin);
        }
        return max_len;
    }
};
```

mgm 版本

```cpp
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int begin = 0, maxLen = 0;
        unordered_map<char, int> preIndex;
        for (int i = 0; i < s.size(); ++i) {
            if (preIndex.find(s[i]) != preIndex.end() && preIndex[s[i]] >= begin) {
                maxLen = max(maxLen, i - begin);
                begin = preIndex[s[i]] + 1;
            }
            preIndex[s[i]] = i;
        }
        return max(maxLen, (int)s.size() - begin);
    }
};
```

> **Tips**

> 其实我们可以问面试官，如果这个字符串里面是否都是 ASCII 字符，如果是我们可以直接开一个 256 大小的数组，如果不能用哈希表的话可以这么做。或者只有字母，可以只需 26 大小的数组，如果是 unicode 字符，shut up，我想静静...
