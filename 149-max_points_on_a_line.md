# 149-Max Points on a Line

## Problem

> Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

## Solution

- 暴力枚举

    对每个点，算经过这个点的所有直线的斜率，同斜率的就在一条直线上！！记得处理重合的点

## Code

### Python

```python

```

### C++

```cpp
/**
 * Definition for a point.
 * struct Point {
 *     int x;
 *     int y;
 *     Point() : x(0), y(0) {}
 *     Point(int a, int b) : x(a), y(b) {}
 * };
 */
class Solution {
public:
    int maxPoints(vector<Point>& points) {
        int size = points.size();
        if (size == 0) {
            return 0;
        }

        int maxNum = 1;
        unordered_map<double, int> slopes;
        for (int i = 0; i < size; ++i) {
            // 对每一个点维护经过的所有直线的斜率，统计个数就行，待会反正也只需要知道最大值
            slopes.clear();
            // 重合点数目！
            int samePointsNumber = 0;
            // 当前点同线点数的最大值
            int curMaxNum = 1;
            for (int j = i + 1; j < size; ++j) {
                double slope;
                if (points[i].x == points[j].x) {
                    if (points[i].y == points[j].y) { // 同一个点
                        samePointsNumber++;
                        continue;
                    }

                    slope = numeric_limits<double>::infinity();
                } else {
                    slope = double(points[i].y - points[j].y) / (points[i].x - points[j].x);
                }

                if (slopes.find(slope) == slopes.end()) {
                    slopes[slope] = 2;
                } else {
                    slopes[slope]++;
                }
                curMaxNum = max(curMaxNum, slopes[slope]);
            }
            maxNum = max(maxNum, curMaxNum + samePointsNumber);
        }
        return maxNum;
    }
};
```
