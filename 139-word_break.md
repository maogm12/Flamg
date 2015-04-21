# 139-Word Break

## Problem

> Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

> For example, given
s = "leetcode",
dict = ["leet", "code"].

> Return true because "leetcode" can be segmented as "leet code".

## Solution

- 深度优先遍历(DFS)，也是一种回溯算法，即找到一个匹配A之后，继续向后匹配，如果继续的那个匹配没有成功，再回到当前，寻找另一个匹配B，继续向后匹配，如此下去。但是，在本题中，使用DFS是要超时的，因为当最后不匹配的时候，需要将所有的深度都遍历完才能判断出来。所以，作为一种比较trick的方法，先对最后的部分做一个判断，如果最后的部分可以匹配的上，则再用DFS；反之，直接判否。
- 动态规划(DP)，设字典中最长的词语长度为max_len，最短的词语长度为min_len，设dp为长度为字符串长度的标志数组，dp[i]表示s[0:i]可以由词典中的词组成，dp数组的值只有0和1，0表示不能，1表示能。那么，存在如下关系：
	```dp[i] = max(dp[i-j:i]) j∈[min_len, max_len] 且 s[i-j:i] in Dict```
	
- DP和DFS的关系，为毛DFS超时，DP不超时呢？
	比如对于aaaaaaaab， Dict中有'a','aa','aaa','aaaa'。那么，如果是DFS，要判否，就需要将前面一串a的所有组合全都找出来，最终每一个都不能匹配才行。如果是DP，就不需要找出所有组合，因为dp[i]标示为1只需要有一种情况到位置i时能匹配上就可以了，没有考虑那些乱七八糟的组合了。

## Code

### Python for DFS

```python
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        self.max_len = -1
        self.min_len = -1
        for word in wordDict:
            len_w = len(word)
            if self.min_len == -1 or len_w < self.min_len:
                self.min_len = len_w
            if self.max_len == -1 or len_w > self.max_len:
                self.max_len = len_w
        if self.end_test(s, wordDict):
            return self.dfs(s, 0, wordDict)
        else:
            return False
    
    def dfs(self, s, i_start, wordDict):
        if i_start == len(s):
            return True
        for i in range(self.min_len, self.max_len+1):
            if i_start + i > len(s):
                break
            if s[i_start:i_start+i] in wordDict:
                if self.dfs(s, i_start+i, wordDict):
                    return True
        return False
    
    def end_test(self, s, wordDict):
        len_s = len(s)
        for i in range(self.min_len, self.max_len+1):
            if s[len_s - i:] in wordDict:
                return True
        return False
        
```

### Python for DP

```
class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        self.max_len = -1
        self.min_len = -1
        for word in wordDict:
            len_w = len(word)
            if self.min_len == -1 or len_w < self.min_len:
                self.min_len = len_w
            if self.max_len == -1 or len_w > self.max_len:
                self.max_len = len_w
        len_s = len(s)
        dp = [False for i in range(len_s+1)]
        dp[0] = True
        i = 0
        while i < len_s:
            if not dp[i]:
                i += 1
                continue
            for j in range(self.min_len, self.max_len+1):
                if i+j > len_s:
                    break
                if s[i:i+j] in wordDict:
                    dp[i+j] = True
            i += 1
        return dp[len_s]
```

### C++

```cpp

```