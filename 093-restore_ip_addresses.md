# 093-Restore IP Addresses

## Problem

> Given a string containing only digits, restore it by returning all possible valid IP address combinations.

> For example:
Given `"25525511135"`,

> return `["255.255.11.135", "255.255.111.35"]`. (Order does not matter)

## Solution

- 回溯， 每次取一位、两位、三位字符加到结果中

## Code

### Python

```python
class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        self.results = []
        self.generate_IP(s, 0, 4, '')
        return self.results
    
    def generate_IP(self, s, begin, level, result):
        if level == 0:
            if begin < len(s):
                return
            self.results.append(result)
            return
        for i in range(3):
            if begin+i+1 > len(s):
                break
            IP = s[begin: begin+i+1]
            if IP.startswith('0') and len(IP) > 1:
                continue
            if not 0 <= int(IP) <= 255:
                continue
            self.generate_IP(s, begin+i+1, level-1, IP if result == '' else result + '.' + IP)        
```

### C++

```cpp
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        generate_IP(s, 0, 4, "");
        return results;
    }
    void generate_IP(string &s, int begin, int level, string current_result) {
        if (level == 0) {
            if (begin >= s.length()) {
                results.push_back(current_result);
            }
            return;
        }
        for (int i = 1; i <= 3; i++) {
            if (begin+i > s.length()) {
                break;
            }
            string tmp_str = s.substr(begin, i);
            int number = atoi(tmp_str.c_str());
            if (i > 1 && tmp_str[0] == '0') {
                break;
            }
            if (number > 255) {
                continue;
            }
            if (current_result == "") {
                generate_IP(s, begin+i, level-1, tmp_str);
            } else {
                generate_IP(s, begin+i, level-1, current_result + "." + tmp_str);
            }
        }
    }
private:
    vector<string> results;
};
```