# 140-Word Break II

## Problem

> Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

> Return all such possible sentences.

> For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

> A solution is ["cats and dog", "cat sand dog"].

## Solution

- DFS, 同139题类似。DFS+末尾判断

## Code

### Python for DFS

```python
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        self.max_len = -1
        self.min_len = -1
        for word in wordDict:
            len_w = len(word)
            if self.min_len == -1 or len_w < self.min_len:
                self.min_len = len_w
            if self.max_len == -1 or len_w > self.max_len:
                self.max_len = len_w
        
        self.results = []
        if not self.end_judge(s, wordDict):
            return self.results
        self.sub_wordbreak(s, 0, wordDict, '')
        return self.results
        
    def sub_wordbreak(self, s, i_start, wordDict, result):
        if i_start == len(s):
            self.results.append(result.strip(' '))
        for i in range(self.min_len, self.max_len+1):
            if i + i_start > len(s):
                break
            word_tmp = s[i_start: i_start+i]
            if word_tmp in wordDict:
                self.sub_wordbreak(s, i_start+i, wordDict, result + ' ' + word_tmp)
    
    def end_judge(self, s, wordDict):
        len_s = len(s)
        for i in range(self.min_len, self.max_len+1):
            if s[len_s - i:] in wordDict:
                return True
        return False
```

### C++

```cpp

```