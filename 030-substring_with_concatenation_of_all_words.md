# 030-Substring with Concatenation of All Words

## Problem

> You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

> For example, given:  
> s: `"barfoothefoobarman"`  
> words: `["foo", "bar"]`

> You should return the indices: [0,9].  
> (order does not matter).

## Solution

`s` 大小 `n`，单词数组大小 `m`

- 暴力搜索法

    我们对 s 里面的每一个下标都检测一下，检测接下来的一段字串是不是由给定的单词数组连起来的。

    为了检测，我们维护一个哈希表，记录单词在单词数组里出现的次数。每解析到一个在表里面的单词，单词次数减 1，如果某一个单词不在表里，或者次数已经降到 0 了，说明这个下标不是我们需要的下标，我们接着解析下一个下标。

    时间复杂度为 O(nm)

- 滑动窗口法

    每个单词长度为 *k* 的话，我们可以把处理过程分为 *k* 组：

    ```
0   k    2k   ...
1   k+1  2k+1 ...
...
k-1 2k-1 3k-1 ...
    ```

    这样我们在每一组内，以 *k* 为一个单元，前面检查过的信息后面还可以使用，比如某一段中统计的单词次数。

    我们可以使用一个滑动窗口，保证窗口内单词数量不超过给定的数组内单词的数目，并且里面的单词都合法，并且出现次数不比给定的数组内单词出现次数多。这样往后滑动窗口，一旦窗口内部单词数量等于给定的数组大小，说明这是一个合法的字串。

    时间复杂为 O(nk)

## Code

### Python

```python

```

### C++

```cpp
vector<int> findSubstring(string s, vector<string>& words) {
	vector<int> result;
	if (words.empty()) return result;
	unordered_map<string, int> times;

	int i = 0;
	int wordSize = words[0].size();
	int wordsTotalSize = words.size() * wordSize;
	int strSize = s.size();
    // 注意 s.size() 为 string::size_type，是一个 unsigned 的
    // 我们这里直接转成了 int 防止 wordsTotalSize 更大的时候溢出。。。
	while (i <= strSize - wordsTotalSize) {
	    resetTimes(times, words);
		int j = 0;
		while (j < words.size()) {
			string sub = s.substr(i + j * wordSize, wordSize);
			if (times.find(sub) == times.end() || times[sub] == 0) {
				break;
			}
			times[sub] -= 1;
			++j;
		}

		if (j == words.size()) {
			result.push_back(i);
		}
		++i;
	}

	return result;
}

void resetTimes(unordered_map<string, int>& times, vector<string>& words) {
	for (string word : words) {
		times[word] = 0;
	}
	for (string word : words) {
		times[word] += 1;
	}
}
```

滑动窗口

```cpp
vector<int> findSubstring(string s, vector<string>& words) {
	vector<int> result;
	if (words.empty()) return result;
	unordered_map<string, int> times;
	for (auto word : words) {
	    if (times.find(word) == times.end()) {
	        times[word] = 1;
	    } else {
	        times[word]++;
	    }
	}

	int wordSize = words[0].size();
	int strSize = s.size();
	for (int start = 0; start < wordSize; ++start) {
		int counting = 0;  // 窗口内单词数量
		unordered_map<string, int> window;
		for (int i = start; i <= strSize - wordSize; i += wordSize) {
		    string sub = s.substr(i, wordSize);
		    if (times.find(sub) == times.end()) { // 非法词汇，窗口清零
		        counting = 0;
		        window.clear();
		    } else {
		        if (counting == words.size()) { // 窗口满了，把最前面的单词删掉
		            string toRm = s.substr(i - counting * wordSize, wordSize);
		            counting--;
		            window[toRm]--;
		        }

		        counting++;
		        if (window.find(sub) == window.end()) {
		            window[sub] = 1;
		        } else {
		            window[sub]++;
		        }

		        while (window[sub] > times[sub]) {
                    // 某个单词出现次数太多，缩小窗口直到窗口内的串合法
		            string toRm = s.substr(i - (counting - 1) * wordSize, wordSize);
		            counting--;
		            window[toRm]--;
		        }
		    }

		    if (counting == words.size()) {
		        result.push_back(i - (counting - 1) * wordSize);
		    }
		}
	}
	return result;
}
```
