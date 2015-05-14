# 071-Simplify Path

## Problem

> Given an absolute path for a file (Unix-style), simplify it.

> For example,

> **path** = "/home/", => "/home"

> **path** = "/a/./b/../../c/", => "/c"

## Solution

解法很直观，就是先按`/`切分，使用一个栈做目录的存储，父目录在栈底，子目录在栈顶，然后根据情况分析：

- 如果遇到`"."`或者`""`，不做处理
- 如果遇到`".."`，如果栈不为空，弹出栈顶元素
- 其他情况，压栈处理。

详细看代码

## Code

### Python

```python
class Solution:
    # @param {string} path
    # @return {string}
    def simplifyPath(self, path):
        sub_paths = path.split('/')
        dirs = []
        for sub_path in sub_paths:
            if sub_path == '..':
                if len(dirs) > 0:
                    dirs.pop()
            elif sub_path != '' and sub_path != '.':
                dirs.append(sub_path)
        result = '/' + '/'.join(dirs)
        return result
        
```

### C++

```cpp
class Solution {
public:
    string simplifyPath(string path) {
        int len = path.length();
        vector<string> dirs;
        int start_i = 0;
        int i = 1;
        while (i <= len) {
            if (i == len || path[i] == '/') {
                string dir = path.substr(start_i+1, i - start_i - 1);
                if (dir == "..") {
                    if (!dirs.empty()) {
                        dirs.pop_back();
                    }
                } else if (dir != "." && dir != "") {
                    dirs.push_back(dir);
                }
                start_i = i;
            }
            i++;
        }
        stringstream result;
        if (dirs.empty()) {
            result << "/";
        } else {
            for (auto it : dirs) {
                result << "/" << it;
            }
        }
        
        return result.str();
    }
};
```