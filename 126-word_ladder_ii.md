# 126-Word Ladder II

## Problem

> Given two words (start and end), and a dictionary, find all shortest transformation sequence(s) from start to end, such that:

> Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

> Given:
> 
> start = `"hit"`
> 
> end = `"cog"`
> 
> dict = `["hot","dot","dog","lot","log"]`
> 
Return
>
```
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
```
** Not**:
> 
- All words have the same length.
- All words contain only lowercase alphabetic characters.

## Solution

与word ladder一样，仍然是BFS，但需要记录前一个单词在队列中的位置。同时还要回溯求出结果。


## Code

### Python

```python
class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
	def findLadders(self, start, end, dict):
		len_w = len(start)
		alphas = [chr(v) for v in range(ord('a'), ord('z')+1)]
		
		queue = [start]
		pre_index = [[-1]]
		end_pre = []
		
		begin_i = 0
		end_i = 1
		level = 1
		is_over = False
		visited = {}
		
		while begin_i < end_i:
			word = queue[begin_i]
			for i in range(len_w):
				for ch in alphas:
					if ch == word[i]:
						continue
					new_word = word[0:i] + ch + word[i+1:]
					
					if new_word == end:
						end_pre.append(begin_i)
						is_over = True
					elif new_word in visited:
						index = visited[new_word]
						if index > begin_i:
							pre_index[index].append(begin_i)
					elif new_word in dict:
						queue.append(new_word)
						visited[new_word] = len(queue) - 1
						pre_index.append([begin_i])
						
			if begin_i == end_i - 1:
				level += 1
				if is_over:
					break
				end_i = len(queue)
			begin_i += 1
			
		queue.append(end)
		pre_index.append(end_pre)
		
		self.results = []
		self.gen_path(queue, pre_index, level, [], len(queue)-1)
		
		return self.results
	
	def gen_path(self, queue, pre_index, level, result, current_index):
		if len(result) == level:
			if result[0] == queue[0]:
				self.results.append(result)
			return
		word = queue[current_index]
		pre_is = pre_index[current_index]
		result = [word] + result
		for pre_i in pre_is:
			self.gen_path(queue, pre_index, level, result, pre_i)

```

### C++

> 注意： 使用map过不鸟，使用unordered_map可以过

```cpp
class Solution {
public:
    vector<vector<string> > findLadders(string start, string end, unordered_set<string> &dict) {
        int len_w = start.length();
        
        vector<string> queue;
        vector<vector<int> > pre_index;
        vector<int> end_pre;
        queue.push_back(start);
        pre_index.push_back(vector<int> {-1});
        
        unordered_map<string, int> visited;
        visited.insert(make_pair(start, 0));
        
        int begin_i = 0;
        int end_i = 1;
        bool is_over = false;
        int level = 1;
        while (begin_i < end_i) {
            string word = queue[begin_i];
            for (int i = 0; i < len_w; i++) {
                string new_word(word);
                for (char ch = 'a'; ch <= 'z'; ch++) {
                    if (ch == word[i]) {
                        continue;
                    }
                    new_word[i] = ch;
                    if (new_word == end) {
                        end_pre.push_back(begin_i);
                        is_over = true;
                    } else if (visited.find(new_word) != visited.end()) {
                        unordered_map<string,int>::iterator it = visited.find(new_word);
                        if (it->second > begin_i) {
                            pre_index[it->second].push_back(begin_i);
                        }
                    } else if (dict.find(new_word) != dict.end()) {
                        queue.push_back(new_word);
                        pre_index.push_back(vector<int> {begin_i});
                        visited.insert(make_pair(new_word, queue.size()-1));
                    }
                }
            }
            if (begin_i == end_i - 1) {
                level++;
                if (is_over) {
                    break;
                }
                end_i = queue.size();
            }
            begin_i++;
        }
        queue.push_back(end);
        pre_index.push_back(end_pre);
		vector<string> result;
        gen_path(queue, pre_index, result, queue.size()-1, level);
        return results;
    }
    void gen_path(vector<string> &queue, vector<vector<int> > &pre_index, vector<string> result, int current_index, int level) {
        if (result.size() == level) {
            if (result[level-1] == queue[0]) {
                reverse(result.begin(), result.end());
                results.push_back(result);
            }
            return;
        }
        string word = queue[current_index];
        vector<int> pre_is = pre_index[current_index];
        result.push_back(word);
        for (int it : pre_is) {
            gen_path(queue, pre_index, result, it, level);
        }
    }
private:
    vector<vector<string> > results;
};

```