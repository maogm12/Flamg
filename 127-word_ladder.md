# 127-Word Ladder

## Problem

> Given two words (beginWord and endWord), and a dictionary, find the length of shortest transformation sequence from beginWord to endWord, such that:
>
- Only one letter can be changed at a time
- Each intermediate word must exist in the dictionary

> For example,

> Given:

> start = `"hit"`

> end = "cog"

> dict = `["hot","dot","dog","lot","log"]`

> As one shortest transformation is `"hit" -> "hot" -> "dot" -> "dog" -> "cog"`,
> return its length 5.

> **Note**:

> 
- Return 0 if there is no such transformation sequence.
- All words have the same length.
- All words contain only lowercase alphabetic characters.

## Solution

- BFS算法，但是有一点需要注意，因为词典里面的词语太多，所以与词典中每个单词去比较会导致超时，不如直接改动字符串中字符得到与当前单词距离为1的单词。

## Code

### Python

```python
class Solution:
    # @param beginWord, a string
    # @param endWord, a string
    # @param wordDict, a set<string>
    # @return an integer
    def ladderLength(self, beginWord, endWord, wordDict):
        alphas = [chr(i) for i in range(ord('a'), ord('z')+1)]
        
        queue = [beginWord]
        len_w = len(beginWord)
        begin = 0
        end = 1
        level = 1
        
        while begin < end:
            word = queue[begin]
            for i in range(len_w):
                for ch in alphas:
                    if word[i] == ch:
                        continue
                    new_word = word[0:i] + ch + word[i+1:]
                    if new_word == endWord:
                        return level + 1
                    if new_word in wordDict:
                        queue.append(new_word)
                        wordDict.remove(new_word)
            if begin == end - 1:
                end = len(queue)
                level += 1
            begin += 1
        return 0
        
```

### C++

```cpp
class Solution {
public:
    int ladderLength(string beginWord, string endWord, unordered_set<string>& wordDict) {
        vector<string> queue;
        queue.push_back(beginWord);
        int len_w = beginWord.length();
        int begin = 0;
        int end = 1;
        int level = 1;
        while (begin < end) {
            string word = queue[begin];
            for (int i = 0; i < len_w; i++) {
                string new_word(word);
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    if (ch == word[i]) {
                        continue;
                    }
                    new_word[i] = ch;
                    if (new_word == endWord) {
                        return level+1;
                    }
                    auto it = wordDict.find(new_word);
                    if (it != wordDict.end()) {
                        queue.push_back(new_word);
                        wordDict.erase(it);
                    }
                }
            }
            if (begin == end - 1) {
                end = queue.size();
                level++;
            }
            begin++;
        }
        return 0;
    }
};
```