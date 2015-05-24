# 087-Scramble String

## Problem

> Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

> Below is one possible representation of s1 = `"great"`:
> 
```
    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
```

> To scramble the string, we may choose any non-leaf node and swap its two children.

> For example, if we choose the node `"gr"` and swap its two children, it produces a scrambled string `"rgeat"`.
>
```
    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
```

> We say that `"rgeat"` is a scrambled string of `"great"`.

> Similarly, if we continue to swap the children of nodes `"eat"` and `"at"`, it produces a scrambled string `"rgtae"`.
>
```
    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
```
> We say that `"rgtae"` is a scrambled string of `"great"`.

> Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

## Solution

- 暴力算法，递归处理，比如两个字符串s1和s2，长度都为n，那么对于题意中得scramble字符串来说，有如下两种对应的切分方式：
	- 两者按照相同方向切分，即字符串s1的前a个字符与s2的前a个字符比对，s1的后b个字符和s2的后b个字符对比
	- 两者按照相反方向切分，即字符串s1的前a个字符与s2的后a个字符比对，s1的后b个字符和s2的前b个字符对比。
	
	使用公式表示的话，使用`f(b1, e1, b2, e2)`来表示s1字符串从b1到e1处的子串，s2字符串从b2到e2处的子串，是否为scramble字符串。当然，`e1 - b1 == e2 - b2`
	
	`f(b1, e1, b2, e2) = (f(b1, k1, b2, k2) && f(k1+1, e1, k2+1, e2)) `
	`|| (f(b1, k1, k2, e2) && f(k1+1, e1, b2, k2-1))`

- 使用字符数目来剪枝，如果两个子串的各个字符数目不相等，那么一定不是scramble字符串

## Code

### Python for Pruning

```python
class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        if len(s1) != len(s2):
            return False
        return self.is_scramble(s1, 0, len(s1)-1, s2, 0, len(s2)-1)
    
    def is_scramble(self, s1, begin_1, end_1, s2, begin_2, end_2):
        if self.check_same(s1, begin_1, end_1, s2, begin_2, end_2):
            return True
        count = [0 for i in range(26)]
        i1 = begin_1
        i2 = begin_2
        while i1 < end_1 and i2 < end_2:
            count[ord(s1[i1]) - ord('a')] += 1
            count[ord(s2[i2]) - ord('a')] -= 1
            if self.check_count(count):
                is_left  = self.is_scramble(s1, begin_1, i1, s2, begin_2, i2)
                is_right = self.is_scramble(s1, i1+1, end_1, s2, i2+1, end_2)
                if is_left and is_right:
                    return True
            i1 += 1
            i2 += 1
        
        count = [0 for i in range(26)]
        i1 = begin_1
        i2 = end_2
        while i1 < end_1 and i2 > begin_2:
            count[ord(s1[i1]) - ord('a')] += 1
            count[ord(s2[i2]) - ord('a')] -= 1
            if self.check_count(count):
                is_left  = self.is_scramble(s1, begin_1, i1, s2, i2, end_2)
                is_right = self.is_scramble(s1, i1+1, end_1, s2, begin_2, i2-1)
                if is_left and is_right:
                    return True
            i1 += 1
            i2 -= 1
        return False
    
    def check_same(self, s1, b1, e1, s2, b2, e2):
        while b1 <= e1 and b2 <= e2:
            if s1[b1] != s2[b2]:
                return False
            b1 += 1
            b2 += 1
        return True
    
    def check_count(self, count):
        for c in count:
            if c != 0:
                return False
        return True
        
```

### C++

```cpp
class Solution {
public:
    bool isScramble(string s1, string s2) {
        return is_scramble(s1, 0, s1.length()-1, s2, 0, s2.length()-1);
    }
    
    bool is_scramble(string &s1, int begin_1, int end_1, string &s2, int begin_2, int end_2) {
        if (check_substr(s1, begin_1, end_1, s2, begin_2, end_2)) {
            return true;
        }
        int count[26];
        fill(count, count+26, 0);
        int i1 = begin_1;
        int i2 = begin_2;
        while (i1 < end_1 && i2 < end_2) {
            count[s1[i1] - 'a']++;
            count[s2[i2] - 'a']--;
            if (check_count(count)) {
                bool left  = is_scramble(s1, begin_1, i1, s2, begin_2, i2);
                bool right = is_scramble(s1, i1+1, end_1, s2, i2+1, end_2);
                if (left && right) {
                    return true;
                }
            }
            i1++;
            i2++;
        }
        i1 = begin_1;
        i2 = end_2;
        fill(count, count+26, 0);
        while (i1 < end_1 && i2 > begin_2) {
            count[s1[i1] - 'a']++;
            count[s2[i2] - 'a']--;
            if (check_count(count)) {
                bool left  = is_scramble(s1, begin_1, i1, s2, i2, end_2);
                bool right = is_scramble(s1, i1+1, end_1, s2, begin_2, i2-1);
                if (left && right) {
                    return true;
                }
            }
            i1++;
            i2--;
        }
        return false;
    }
    
    bool check_substr(string &s1, int begin_1, int end_1, string &s2, int begin_2, int end_2) {
        while (begin_1 <= end_1 && begin_2 <= end_2) {
            if (s1[begin_1++] != s2[begin_2++]) {
                return false;
            }
        }
        return true;
    }
    bool check_count(int count[]) {
        for (int i = 0; i < 26; i++) {
            if (count[i] != 0) {
                return false;
            }
        }
        return true;
    }
};
```