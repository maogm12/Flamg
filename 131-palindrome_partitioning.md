# 131-Palindrome Partitioning

## Problem

> Given a string s, partition s such that every substring of the partition is a palindrome.

> Return all possible palindrome partitioning of s.

> For example, given s = "aab",
> Return
> 
```
  [
    ["aa","b"],
    ["a","a","b"]
  ]
```

## Solution

- 由底向上的拼接法，对于一个字符串来说，比如上面的`"aab"`，那么每个字符单放出来一定是一种结果，即`["a", "a", "b"]`, 然后，对于`（a[i], a[i+1]）`的情况，如果`a[i] == a[i+1]`，那么可以拼起来形成一个新结果，对于`（a[i-1], a[i], a[i+1]）`的情况，如果`a[i-1] == a[i+1]`，那么也可以拼接起来形成一个新结果。

- 回溯法， 对于一个字符串来说，假如它长度为n，那么有n-1个地方可以切分，遍历这2<sup>n-1</sup>种情况，将不是回文串的情况剪枝，得到最终结果




## Code

### Python for down-to-up

```python
class Solution:
    # @param s, a string
    # @return a list of lists of string
	def partition(self, s):
		self.results = []
		if len(s) == 0:
			return self.results
		init = [c for c in s]
		self.results.append(init)
		self.combine(init)
		return self.results
	
	def combine(self, result):
		len_result = len(result)
		for i in range(1, len_result):
			if result[i] == result[i-1]:
				new_word = result[i-1] + result[i]
				new_result = result[0:i-1] + [new_word] + result[i+1:]
				if not new_result in self.results:
					self.results.append(new_result)
					self.combine(new_result)
		for i in range(1, len_result-1):
			if result[i-1] == result[i+1]:
				new_word = result[i-1] + result[i] + result[i+1]
				new_result = result[0:i-1] + [new_word] + result[i+2:]
				if not new_result in self.results:
					self.results.append(new_result)
					self.combine(new_result)

```

### python for backtracing

```
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.results = []
        self.split(s, 0, 1, [])
        return self.results
    
    def split(self, s, start, end, result):
        if end == len(s):
            if self.is_pali(s[start:end]):
                self.results.append(result + [s[start:end]])
            return
        if self.is_pali(s[start:end]):
            self.split(s, end, end+1, result + [s[start:end]])
        self.split(s, start, end+1, result)
            
    def is_pali(self, s):
        len_s = len(s)
        begin_i = 0
        end_i = len_s - 1
        while begin_i < end_i:
            if s[begin_i] != s[end_i]:
                return False
            begin_i += 1
            end_i -= 1
        return True
```

### C++ for backtracing

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<string> result;
        split(s, 0, 1, result);
        return results;
    }
    void split(string &s, int start, int end, vector<string> &result) {
        if (end == s.length()) {
            if (is_pal(s, start, end-1)) {
                result.push_back(s.substr(start, end - start));
                results.push_back(result);
                result.pop_back();
            }
            return;
        }
        if (is_pal(s, start, end-1)) {
            result.push_back(s.substr(start, end - start));
            split(s, end, end+1, result);
            result.pop_back();
        }
        split(s, start, end+1, result);
    }
    
    bool is_pal(string &s, int start, int end) {
        while (start < end) {
            if (s[start] != s[end]) {
                return false;
            }
            start++;
            end--;
        }
        return true;
    }
private:
    vector<vector<string>> results;
};
```