## 模板

```
int lengthOfSomeThing(string s, int k) {
	// 字典，保存当前窗口的各种元素的个数
	unordered_map<char, int> dict;
		
	int begin = 0; // 窗口左端，闭区间
	int end = 0;   // 窗口右端，开区间
	int max_length = 0;
		
	while (end < s.length()) {
		max_length = max(end - begin, max_length); // 更新结果
		/* 去字典中找当前元素，
		 * 	如果找到，对应的值+1
		 * 	如果没找到，则插入前需要判断
		 *			如果字典到达上限，则先收缩左端，再插入
		 * 		如果字典维达上限，则直接插入
		 */
		auto it = dict.find(s[end]);
		if (it == dict.end()) {
			if (dict.size() == k) {
				// 收缩左端,直到dict.size() < k
				// 插入右端元素
			} else {
				// 直接插入
			}
		} else {
			dict[s[end]]++;
		}
	}
	// 不要忘了end==s.length()后其实还可以更新max_length, 
	// 或者左端还可以收缩（在遇到求最短长度的问题的时候）
	return max_value;
}		
```

## 最多有k个不同字符的最长子字符串

```
class Solution {
public:
    /**
     * @param s : A string
     * @return : The length of the longest substring 
     *           that contains at most k distinct characters.
     */
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        // write your code here
        if (k <= 0) {
            return 0;
        }
        unordered_map<char, int> k_chs;
        int begin = 0;
        int end   = 0;
        int max_length = 0;
        while (end <= s.length()) {
            max_length = max(max_length, end - begin);
            if (end == s.length()) {
                break;
            }
            auto it = k_chs.find(s[end]);
            if (it == k_chs.end()) {
                if (k_chs.size() == k) {
                    while (begin < end) {
                        k_chs[s[begin]]--;
                        if (k_chs[s[begin]] == 0) {
                            k_chs.erase(s[begin]);
                            begin++;
                            break;
                        }
                        begin++;
                    }
                } 
                k_chs.insert(make_pair(s[end], 1));
            } else {
                it->second++;
            }
            end++;
        }
        
        return max_length;
    }
};

```

## 最少子串覆盖

```
class Solution {
public:    
    /**
     * @param source: A string
     * @param target: A string
     * @return: A string denote the minimum window
     *          Return "" if there is no such a string
     */
    string minWindow(string &source, string &target) {
        // write your code here
        unordered_map<char, int> char_dict;
        for (char c : target) {
            auto it = char_dict.find(c);
            if (it == char_dict.end()) {
                char_dict.insert(make_pair(c, 1));
            } else {
                it->second++;
            }
        }
        
        int begin = 0; 
        int end = 0;
        
        pair<int, int> result(-1, -1);
        while (end < source.length()) {
            auto it = char_dict.find(source[end]);
            if (it != char_dict.end()) {
                it->second--;
                if (check_dict(char_dict)) {
                    while (begin < end) {
                        auto begin_it = char_dict.find(source[begin]);
                        if (begin_it != char_dict.end()) {
                            if (begin_it->second == 0) {
                                break;
                            } else {
                                begin_it->second++;
                            }
                        }
                        begin++;
                    }
                    if (result.first == -1 || 
                            end - begin < result.second - result.first) {
                        result.first = begin;
                        result.second = end;
                    } 
                }
            }
            end++;
        }
        if (result.first == -1) {
            return "";
        } else {
            return source.substr(result.first, result.second - result.first + 1);
        }
    }
    bool check_dict(unordered_map<char, int> &char_dict) {
        for (auto it : char_dict) {
            if (it.second > 0) {
                return false;
            }
        }
        return true;
    }
};

```