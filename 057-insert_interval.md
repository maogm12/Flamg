# 057-Insert Interval

## Problem

> Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

> You may assume that the intervals were initially sorted according to their start times.

> Example 1:
Given intervals `[1,3],[6,9]`, insert and merge `[2,5]` in as `[1,5],[6,9]`.

> Example 2:
Given `[1,2],[3,5],[6,7],[8,10],[12,16]`, insert and merge `[4,9]` in as `[1,2],[3,10],[12,16]`.

> This is because the new interval `[4,9]` overlaps with `[3,5],[6,7],[8,10]`.

## Solution

因为区间都是按照起点排好序的，所以，遍历原有的区间，其中的每个区间a，与新区间b分为三种情况：

- a的终点小于b的起点，此时a与b无关。可访问下一个区间
- a的起点大于b的终点，此时a与b无关，且因为是按照起点排序的，所以其后的区间与b也无关，所以不需要访问下一个区间
- a与b有交叉，将其从原有数组中删除，并如果可以扩展，则用a的值扩展b。


## Code

### Python

```python
class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        i = 0
        len_intervals = len(intervals)
        while i < len_intervals:
            interval = intervals[i]
            if interval.start > newInterval.end:
                intervals.insert(i, newInterval)
                return intervals
            if interval.end < newInterval.start:
                i += 1
            else:
                newInterval.start = min(interval.start, newInterval.start)
                newInterval.end   = max(interval.end,   newInterval.end)
                intervals.pop(i)
                len_intervals -= 1
        intervals.append(newInterval)
        return intervals
```

### C++

奇怪，使用同样的算法，C++会超时，看来大python还是做了很多优化滴。

> 注意，下面的代码超时了，待我想出不超时的再写。
	
```cpp
class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        vector<Interval>::iterator it = intervals.begin();
        while (it != intervals.end()) {
            if (it->start > newInterval.end) {
                intervals.insert(it, newInterval);
                return intervals;
            }
            if (it->end < newInterval.start) {
                it++;
            } else {
                newInterval.start = min(newInterval.start, it->start);
                newInterval.end   = max(newInterval.end,   it->end);
                it = intervals.erase(it);
            }
        }
        intervals.push_back(newInterval);
        return intervals;
    }
};
```


使用一个新的数组来表示，就不超时了。应该是erase操作，导致的超时。不过何以python不超时呢？
 
**TODO**

py和cpp在删除上的具体实现还是很不一样的。待我以后查查

> 注意，下面的代码已不超时。

```cpp
class Solution {
public:
    vector<Interval> insert(vector<Interval>& intervals, Interval newInterval) {
        vector<Interval> new_intervals;
        vector<Interval>::iterator it = intervals.begin();
        while (it != intervals.end()) {
            if (it->start > newInterval.end) {
                new_intervals.push_back(newInterval);
                new_intervals.insert(new_intervals.end(), it, intervals.end());
                return new_intervals;
            }
            if (it->end < newInterval.start) {
                new_intervals.push_back(*it);
            } else {
                newInterval.start = min(newInterval.start, it->start);
                newInterval.end   = max(newInterval.end,   it->end);
            }
            it++;
        }
        new_intervals.push_back(newInterval);
        return new_intervals;
    }
};
```