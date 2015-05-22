# 076-Minimum Window Substring

## Problem

> Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

> For example,
> 
> S = `"ADOBECODEBANC"`

> T = `"ABC"`
> 
Minimum window is `"BANC"`.

> Note:
>
> If there is no such window in S that covers all characters in T, return the emtpy string `""`.

> If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

## Solution

滑动窗口法：

- 保存两个指示器，left和right，均初始化为0
- right端添加元素，直到s[left...right]符合条件
- left端删除元素，直到再删一个元素就s[left...right]就不符合条件
- 使用（left, right）更新结果
- left++
- 继续执行第二步

## Code

### Python

```python
class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
	def minWindow(self, s, t):
		char_dict = {}
		for c in t:
			char_dict.setdefault(c, 0)
			char_dict[c] += 1
		begin_i = 0
		end_i = 0
		result = (-1, -1)
		while end_i < len(s):
			if s[end_i] in char_dict:
				char_dict[s[end_i]] -= 1
				if self.check_dict(char_dict):
					while begin_i <= end_i:
						if s[begin_i] in char_dict:
							if char_dict[s[begin_i]] == 0:
								break
							char_dict[s[begin_i]] += 1
						begin_i += 1
					if result == (-1, -1) or result[1] - result[0] > end_i - begin_i:
						result = (begin_i, end_i)
					char_dict[s[begin_i]] += 1
					begin_i += 1
			end_i += 1
		if result == (-1, -1):
			return ''
		return s[result[0]: result[1] + 1]
	
	def check_dict(self, char_dict):
		for c in char_dict:
			if char_dict[c] > 0:
				return False
		return True
```

### C++

```cpp

```