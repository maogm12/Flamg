# 128-Longest Consecutive Sequence

## Problem
> Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
>
> For example,
> Given [100, 4, 200, 1, 3, 2],
> The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
>
> Your algorithm should run in O(n) complexity.

找到数组排序后最长的连续序列长度

## Solution

- Brute-Force

    既然是连续序列，那么咱先排个序呗！然后遍历列表，寻找最长的连续序列。

    时间复杂度是 O(nlogn)

- Hash

    但是这个如果要在 O(n) 的复杂度解决的话，就得考虑哈希了。
    （其实我看了题解才知道的 TT）

    从每个值向两边搜索，寻找最大长度。

    > 如果空间复杂度不怎么要求的话，哈希简直是神器啊！！！！

## Code

### Python

```python
# wait a minute
```

### C++

```cpp
class Solution {
public:
    int longestConsecutive(vector<int> &num) {
        unordered_map<int, bool> used;
        for (auto val: num){
            // 待会儿我们搜索的时候标志为 true，避免重复搜索同一个序列
            used[val] = false;
        }

        int maxLength = 0;
        for (auto i: num) {
            if (used[i]) {
                // 这个序列已经搜索过了
                continue;
            }

            used[i] = true;
            int currentLength = 1;

            // 向两边搜索
            for (int val = i + 1; used.find(val) != used.end(); ++val) {
                used[val] = true;
                currentLength++;
            }
            for (int val = i - 1; used.find(val) != used.end(); --val) {
                used[val] = true;
                currentLength++;
            }
            maxLength = max(maxLength, currentLength);
        }

        return maxLength;
    }
};
```
