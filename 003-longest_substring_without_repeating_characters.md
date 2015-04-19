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