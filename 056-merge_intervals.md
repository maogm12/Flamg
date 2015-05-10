# 056-Merge Intervals

## Problem

> Given a collection of intervals, merge all overlapping intervals.

> For example,
Given `[1,3],[2,6],[8,10],[15,18]`,
>
return `[1,6],[8,10],[15,18]`.

## Solution

- 暴力算法，每个区间都遍历其他区间，找到有交叉的，合并。时间复杂度O(n<sup>2</sup>).
- 按照起点对所有区间排序，那么判断交叉只需要在相邻的区间中判断就可以了。如果下一个区间的起点在当前区间内，那么就需要合并，否则不需要。

> 这道题奇怪的地方在于相同的C++和python算法，C++居然比python慢


## Code

### Python

```python
class Solution:
    # @param {Interval[]} intervals
    # @return {Interval[]}
    def merge(self, intervals):
        def cmp(a, b):
            if a.start < b.start:
                return -1
            elif a.start > b.start:
                return 1
            else:
                return 0
        intervals.sort(cmp)
        results = []
        result = None
        for item in intervals:
            if result == None:
                result = item
            else:
                if result.start <= item.start <= result.end:
                    result.end = max(result.end, item.end)
                else:
                    results.append(result)
                    result = item
        if result != None:
            results.append(result)
        return results
```

### C++

```cpp
class Solution {
public:
    vector<Interval> merge(vector<Interval>& intervals) {
        sort(intervals.begin(), intervals.end(), Solution::cmp);
        vector<Interval> results;
        Interval *result = NULL;
        for (auto it = intervals.begin(); it != intervals.end(); it++) {
            if (result == NULL) {
                result = new Interval(it->start, it->end);
            } else {
                if (it->start >= result->start && it->start <= result->end) {
                    result->end = max(result->end, it->end);
                } else {
                    results.push_back(*result);
                    result->start = it->start;
                    result->end = it->end;
                }
            }
        }
        if (result != NULL) {
            results.push_back(*result);
            delete result;
        }
        return results;
        
    }
    static bool cmp(Interval a, Interval b) {
        return a.start < b.start;
    }
};
```