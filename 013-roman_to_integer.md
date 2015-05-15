# 013-Roman to Integer

## Problem

> Given a roman numeral, convert it to an integer.

> Input is guaranteed to be within the range from 1 to 3999.

## Solution

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    int romanToInt(string s) {
    	int number = 0;
    	int i = 0, size = s.size();
    	while (i < size) {
    		switch (s[i]) {
    		case 'I':
    			if (i + 1 < size && s[i + 1] == 'V') {
    				number += 4;
    				i += 2;
    			} else if (i + 1 < size && s[i + 1] == 'X') {
    				number += 9;
    				i += 2;
    			} else {
    				number += 1;
    				i += 1;
    			}
    			break;
    		case 'V':
    			number += 5;
    			i += 1;
    			break;
    		case 'X':
    			if (i + 1 < size && s[i + 1] == 'L') {
    				number += 40;
    				i += 2;
    			} else if (i + 1 < size && s[i + 1] == 'C') {
    				number += 90;
    				i += 2;
    			} else {
    				number += 10;
    				i += 1;
    			}
    			break;
    		case 'L':
    			number += 50;
    			i += 1;
    			break;
    		case 'C':
    			if (i + 1 < size && s[i + 1] == 'D') {
    				number += 400;
    				i += 2;
    			} else if (i + 1 < size && s[i + 1] == 'M') {
    				number += 900;
    				i += 2;
    			} else {
    				number += 100;
    				i += 1;
    			}
    			break;
    		case 'D':
    			number += 500;
    			i += 1;
    			break;
    		case 'M':
    			number += 1000;
    			i += 1;
    			break;
    		}
    	}
    	return number;
    }
};
```
