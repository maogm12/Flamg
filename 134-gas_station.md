# 134-Gas Station

## Problem

> There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

> You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

> Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

> Note:

>  The solution is guaranteed to be unique.


## Solution

- 暴力算法

    很容易想到暴力算法，我们从每个点开始，往后搜索，记录剩余的汽油量，如果在油量降到负数之前到达了开始搜索的点，那么这个点就是要找的结果了。

    每次搜索的时间是线性的，所以时间复杂度在 O(n^2)

- 搜索

    有没有发现，我们其实不用每次都从头开始搜索。

    比如我们从一个起点 `startPos` 开始往后搜索了，可到达了一个 `reachMostPos` 的地方，说明在这个地方油不够了，那么怎么办呢？我们可以从 `startPos - 1` 的地方开始，这样可以加上 `startPos - 1` 到 `startPos` 剩余的油，如果油量增加了，继续往下跑，如果油量减少了，我们再往前一个点，直到成功跑圈圈或者遇到 `reachMostPos` 为止。

    这样每个点只被访问一次，时间复杂度 O(n)

- 搜索nb版

    我们还可以这么搜索。

    我们从头（`0`）开始，跑到一个最远能跑到的地方（`end`），然后 `[0, end]` 这之间不用管了，如果跑圈圈的时候能跑到 `0`，一定也能跑到 `end`。然后我们开始从 `end + 1` 的继续搜索，直到搜到最后一个 station

    另一方面，如果总共的油比总共的耗油量大的话，我们一定是可以跑完全程的。

    代码量减少一万倍！

## Code

### Python

```python
# 画圈圈
```

### C++

感觉代码可以被精简！

```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int size = gas.size();
        if (size == 0) {
            return -1;
        }

        // 先计算出每个点到下一站可以剩下多少油
        vector<int> remain(size);
        int maxRemain = -1, maxPos = -1;
        for (int i = 0; i < size; ++i) {
            remain[i] = gas[i] - cost[i];
            if (remain[i] > maxRemain) {
                maxRemain = remain[i];
                maxPos = i;
            }
        }

        if (maxRemain < 0) {
            return -1;
        }
        int reachMostPos = (maxPos + 1) % size;
        int reachMostRemain = maxRemain;
        while (reachMostRemain + remain[reachMostPos] >= 0) {
            reachMostRemain += remain[reachMostPos];
            reachMostPos = (reachMostPos + 1) % size;
            if (reachMostPos == maxPos) {
                return maxPos;
            }
        }

        // 向前搜索
        for (int i = 1; i < size; ++i) {
            int startPos = (size + maxPos - i) % size;
            reachMostRemain += remain[startPos];
            while (reachMostRemain + remain[reachMostPos] >= 0) {
                reachMostRemain += remain[reachMostPos];
                reachMostPos = (reachMostPos + 1) % size;
                if (reachMostPos == startPos) {
                    return startPos;
                }
            }

            if (startPos == reachMostPos) {
                break;
            }
        }

        return -1;
    }
};
```

搜索nb版！！！

```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {
        int remain = 0, // 在到达当前站点剩余的油量
            total = 0,  // 只要总油量比消耗的大，就可以跑圈圈了
            end = -1;   // 可以到达的位置
        for (int i = 0; i < gas.size(); ++i) {
            int left = gas[i] - cost[i];
            remain += left;
            total += left;
            if (remain < 0) { // 不够到下一站，我们从这一站从新开始看
                end = i;
                remain = 0;
            }
        }

        return total >= 0 ? end + 1 : -1;
    }
};
```
