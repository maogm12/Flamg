# 187-Repeated DNA Sequences

## Problem

> All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: `"ACGAATTCCG"`. When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

> Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

> For example,

> Given s = `"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"`,

> Return:
`["AAAAACCCCC", "CCCCCAAAAA"]`.

## Solution

- 使用hash表存储所有可能的10字符长的字串，记录他们的次数，超过1次的返回.



## Code

### Python

> 根据上述思路，可以轻松的写出py代码，AC过

```python
class Solution:
    # @param s, a string
    # @return a list of strings
	def findRepeatedDnaSequences(self, s):
		i = 0
		dna_map = {}
		len_s = len(s)
		i = 0
		while i < len_s - 9:
			dna_map.setdefault(s[i:i+10], 0)
			dna_map[s[i:i+10]] += 1
			i += 1
		results = []
		for key in dna_map:
			if dna_map[key] > 1:
				results.append(key)
		return results
```

### C++

但依据上述想法直接写出的cpp代码，却内存超限，内存超限的代码如下，经过变通后可以AC的代码如下下。

```cpp
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> results;
        unordered_map<string, int> dna_map;
        for (int i = 9; i < s.length(); i++) {
            string sub_str = s.substr(i-9, 10);
            unordered_map<string, int>::iterator it = dna_map.find(sub_str);
            if (it != dna_map.end()) {
                dna_map[sub_str]++;
            } else {
                dna_map.insert(make_pair(sub_str, 1));
            }
        }
        for (unordered_map<string,int>::iterator it = dna_map.begin();  it != dna_map.end(); it++) {
            if (it->second > 1) {
                results.push_back(it->first);
            }
        }
        return results;    
    }
};

```

```cpp
class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        vector<string> results;
        unordered_map<int, pair<int,int>> dna_map;
        int length = s.length();
        if (length < 10) {
            return results;
        }
        
        for (int i = 0; i < length - 9; i++) {
            string str = s.substr(i, 10);
            int code = encode_str(str);
            auto it = dna_map.find(code);
            if (it != dna_map.end()) {
                (it->second).second++;
            } else {
                dna_map.insert(make_pair(code, make_pair(i, 1)));
            }
        }
        for (auto it : dna_map) {
            pair<int, int> index_count = it.second;
            int index = index_count.first;
            int count = index_count.second;
            if (count > 1) {
                results.push_back(s.substr(index, 10));
            }
        }
        return results;
    }
    
    int encode_str(string &s) {
        int code = 0;
        for(int i = 0; i < s.length(); i++) {
            if (s[i] == 'A') {
                code = code * 4 + 1;
            } else if (s[i] == 'C') {
                code = code * 4 + 2;
            } else if (s[i] == 'G') {
                code = code * 4 + 3;
            } else {
                code = code * 4;
            }
        }
        return code;
    }
};

```