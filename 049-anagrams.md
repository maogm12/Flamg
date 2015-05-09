# 049-Anagrams

## Problem

> Given an array of strings, return all groups of strings that are anagrams.

> Note: All inputs will be in lower-case.


## Solution

anagrams指的是两个字符串所拥有的字符的种类，及各个类别的字符的个数都是相同的。只不过顺序不同。那么，依照此意，可以有两种解法：

- 排序，对每个字符串排序，如果排序后是一样的，那么就是anagrams
- 哈希，对所有的字符都指定一个数，然后构造一个与字母顺序无关的哈希函数，相同哈希值的字符串一定是anagrams。当然，哈希冲突绝对不能出现才行。
	
	我设计的哈希函数如下：
	- 每个字符用其ascii码作为值
	- 所有字符对应值相乘，得到h1
	- 所有字符对应值相加，得到h2
	- h1+h2
	
	> 其实我觉得每个字符都指定一个质数，然后把数字相乘就可以了。不过懒得写找质数的函数了。
	

## Code

### Python for sort

```python
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        str_dict = {}
        result = []
        for s in strs:
            sorted_s = ''.join(sorted(s))
            str_dict.setdefault(sorted_s, [])
            str_dict[sorted_s].append(s)
        for s in str_dict:
            if len(str_dict[s]) > 1:
                result += str_dict[s]
        return result
```

### Python for hash

```
class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        str_dict = {}
        result = []
        for s in strs:
            hash_s = self.str2hash(s)
            str_dict.setdefault(hash_s, [])
            str_dict[hash_s].append(s)
        for hash_s in str_dict:
            if len(str_dict[hash_s]) > 1:
                result += str_dict[hash_s]
        return result
    
    def str2hash(self, s):
        h1 = 1
        h2 = 0
        for c in s:
            h1 *= ord(c)
            h2 += ord(c)
        return h1+h2
        
```

### C++ for sort

```cpp
class Solution {
public:
    vector<string> anagrams(vector<string>& strs) {
        unordered_map<string, vector<string> > str_dict;
        int len_s = strs.size();
        for (int i = 0; i < len_s; i++) {
            string s = strs[i];
            sort(s.begin(), s.end());
            str_dict[s].push_back(strs[i]);
        }
        vector<string> result;
        for (auto dict_it = str_dict.begin(); dict_it != str_dict.end(); dict_it++) {
            if ( (dict_it->second).size() > 1) {
                for (auto vec_it = dict_it->second.begin(); vec_it != dict_it->second.end(); vec_it++) {
                    result.push_back(*vec_it);
                }
            }
        }
        return result;
    }
};
```

### C++ for hash

```
class Solution {
public:
    vector<string> anagrams(vector<string>& strs) {
        unordered_map<int, vector<string> > str_dict;
        int len_s = strs.size();
        for (int i = 0; i < len_s; i++) {
            int hash_v = str2hash(strs[i]);
            str_dict[hash_v].push_back(strs[i]);
        }
        vector<string> result;
        for (auto dict_it = str_dict.begin(); dict_it != str_dict.end(); dict_it++) {
            if ( (dict_it->second).size() > 1) {
                for (auto vec_it = dict_it->second.begin(); vec_it != dict_it->second.end(); vec_it++) {
                    result.push_back(*vec_it);
                }
            }
        }
        return result;
    }
    
    int str2hash(string s) {
        int h1 = 1;
        int h2 = 0;
        for (char c : s) {
            int v = c - 'a' + 97;
            h1 *= v;
            h2 += v;
        }
        return h1 + h2;
    }
};
```