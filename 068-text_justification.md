# 068-Text Justification

## Problem

> Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

> You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

> Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

> For the last line of text, it should be left justified and no extra space is inserted between words.

> For example,

> words: `["This", "is", "an", "example", "of", "text", "justification."]`
> L: `16`.

> Return the formatted lines as:
> 
```
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
```

> Note: Each word is guaranteed not to exceed L in length.

## Solution

最主要的操作在于将字符串中间的空格数计算清楚，比如对于五个单词，一共有23个空格，那么空格数目应该是`[6,6,6,5]`，五个单词有四个位置需要填空格，尽量均匀且如果不能整除，则左边比右边多。

细节实现题，上代码了。


## Code

### Python

```python
class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        results = []
        len_w = len(words)
        i = 1
        start_i = 0
        now_length = len(words[0])
        while i < len_w:
            
            if now_length + 1 + len(words[i]) > maxWidth:
                # 如果大于最大长度了，则做拼接操作，然后从头开始算
                results.append(self.connect(words, start_i, i, now_length, maxWidth) )
                now_length = len(words[i])
                start_i = i
            else:
                # 如果不足最大长度，继续添加单词
                now_length += 1 + len(words[i])
            i += 1
        blank_space = ' ' * (maxWidth - now_length)
        results.append(' '.join(words[start_i:]) + blank_space )
        return results
        
    def connect(self, words, start_i, end_i, now_length, maxWidth):
        word_num = end_i - start_i
        if word_num == 1:
            blank_space = ' ' * (maxWidth - now_length)
            return words[start_i] + blank_space
        # 因为now_length已经为每个位置放上了一个空格，所以average_num是空格数目-1
        average_num = (maxWidth - now_length) / (word_num - 1)
        # bonus_num是除不尽的情况，除不尽就把空格均匀的放置在前面的位置
        bonus_num   = (maxWidth - now_length) % (word_num - 1)
        result_str  = words[start_i]
        for i in range(start_i+1, end_i):
            if bonus_num == 0:
                blank_space = ' ' * (average_num + 1)
            else:
                blank_space = ' ' * (average_num + 2)
                bonus_num -= 1
            result_str += blank_space + words[i]
        return result_str
            
```

### C++

```cpp

```