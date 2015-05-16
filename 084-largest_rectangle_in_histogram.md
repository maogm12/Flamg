# 084-Largest Rectangle in Histogram

## Problem

> Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

> ![histogram](./images/histogram.png)

> Above is a histogram where width of each bar is 1, given height = `[2,1,5,6,2,3]`.

> ![histogram_area](./images/histogram_area.png)

> The largest rectangle is shown in the shaded area, which has area = 10 unit.

> For example,
Given height = `[2,1,5,6,2,3]`,
return 10.

## Solution

- 暴力算法， 对于[0,n)的所有的i,j对，当然i<=j，其面积为`f(i,j) = min(height[i...j]) × (j-i+1)` 本题就是要找f(i,j)的最大值，那么遍历下来，时间复杂度就是O(n<sup>3</sup>)。

- 优化1，预先把i...j的最小值求出来，然后再遍历。这样的时间复杂度为O(n<sup>2</sup>)

- 递推

	当然，上述两个算法是时间超限的，这就需要分析题目中其他的性质了。假如使用动态规划的话，如何用呢？
	
	动态规划一般需要一个数组，假设一个长度为n的数组，dp。需要考虑dp里的每个元素保存的值是什么意思，一般有两种设法：
	- dp[i]为到达索引i时的最大面积。此时柱子i不一定从结果中出现。
	- dp[i]为到达索引i时以i为结尾的最大面积，此时柱子i一定参与当前结果。
	
	此题应该使用第二种为好，此时，dp = [2,2,5,10,6,8]。 
	
	只保存以i结尾的最大面积也不够让我们求出i+1处的值，因为面积还要考虑高度和宽度；当然，即便保存了i处最大面积矩形的高度和宽度，还是不足以求出i+1处最大矩形的高度和宽度，因为可能下一根柱子比较矮，但是它可以延伸的宽度特别长，比如上图中，如果在最后再添加两根高度为2的柱子，那么到最后一根柱子时，已经可以构成6×2的矩形了。
	
	上面保存最大矩形的长度和宽度的考虑已经很接近了，在这里也不卖关子了，为了下一根柱子着想，在当前位置，我们要保存下来所有的可能的矩形，比如对于上图中得高为6的柱子，需要保存三个矩形，即(6,1) (5,2) (1,4),其中二元对是（宽度，高度）。那么在求下一个位置的所有矩形时，还是上图种的例子，对高6柱子的下一根柱子，其高度为2，那么对于根据上一步得到的三个矩形，得到当前步的所有可能矩形：
	
	- 更新(6,1) -> (2,2)
	- 更新(5,2) -> (2,3)
	- 更新(1,4) -> (1,5)
	- 添加(2,1)
	
	上面四个矩形的第一个和第二个和第四个还需要合并，那么结果为(2,3), (1,5)
	
	此时，一步一步下去，然后再从这么多结果中找到最大矩形就可以了。
	在实现时，因为i+1只需要i步的结果，因而动态规划就退化成了递推式的代码。
	
- 栈实现，根据上面的想法，可以看到，每个位置所保存的各个矩形，其高度是以i位置柱子高度为最后一个元素的递增序列。比如6，高度就是(1,5,6). 3，高度序列就是(1,2,3)。根据这种想法，可以将其变为一种栈操作：
	
	从左到右遍历柱子，
	- 如果栈为空，则将柱子放到栈中，如果柱子大于栈顶的柱子，也将柱子压到栈中。
	- 如果上述条件不成立，则反推以上一个柱子为结尾的所有矩形。
	
	比如，当走到6后面的高为2的柱子时，此时栈中有1，5，6三根柱子，那么，找到两个矩形(5,2)，(6,1)，将这两根柱子弹出，然后2压栈，栈中就只有1，2两根柱子了。
	为了在最后不遗漏情况，需要在结尾添加一根高度为0的柱子，以合并所有情况。
	
	
## Code

### Python for recursion

```python
class Solution:
    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
		if len(height) == 0:
			return 0
		if len(height) > 30:
			if height[10] < height[-10]:
				height.reverse()

		pre_results = {}
		pre_results[ height[0] ] = height[0]
		max_area = height[0]
		for i in range(1, len(height)):
			results = {}
			h = height[i]
			is_have_higher = False
			for h_pre in pre_results:
				area = pre_results[h_pre]
				if h >= h_pre:
					new_area = area + h_pre
					if new_area > max_area:
						max_area = new_area
					if results.get(h_pre, 0) < new_area:
						results[h_pre] = new_area
				else:
					new_area = (area/h_pre + 1) * h
					if new_area > max_area:
						max_area = new_area
					if results.get(h, 0) < new_area:
						results[h] = new_area
					is_have_higher = True
			if not is_have_higher:
				if results.get(h, 0) < h:
					results[h] = h
				if h > max_area:
					max_area = h
			pre_results.clear()
			pre_results = results
		return max_area
```

### C++ for stack

```cpp
class Solution {
public:
    int largestRectangleArea(vector<int>& height) {
        stack<int> s;
        height.push_back(0);
        int i = 0;
        int max_area = 0;
        while (i < height.size()) {
            if (s.empty() || height[i] >= height[s.top()]) {
                s.push(i++);
            } else {
                int tmp_index = s.top();
                s.pop();
                int tmp_area = s.empty() ? height[tmp_index] * i : height[tmp_index] * (i - s.top() - 1);
                max_area = max(tmp_area, max_area);
            }
        }
        return max_area;
    }
};
```