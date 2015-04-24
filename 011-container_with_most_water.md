#011-Container With Most Water

## Question
> Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water. 

> Note: You may not slant the container. 

这个类似于在一个柱状图里面找最大矩形的问题。比如下面这个：

```
  #
  # #
 ######
 #################
```

这个最大面积应该是最下面那排，看来找两个极大值是不靠谱的，动规也是不靠谱的。

## Solution

- Brute-Force

	暴力算法永远是存在的！！！这个嘛，我们遍历所有的情况，算出最大值。时间复杂度只有 O(n^2) 而已

- Search

	没有什么明显算法特征的题，就可以用搜索来做了。我们从两头往中间搜索，有没有发现最大的面积计算的时候是用选定的两个 `height` 中较小的算的，对于某种情况，选定 `height[i]` 和 `height[j]`，其中 `i < j, height[i] < height[j]`，那么如果我们将 `j` 继续变小，我们不可能得到更大的面积，因为矩形的宽度 `j - i` 变小了，高度最大只能是 `height[i]`，所以这个时候我们应该增大 `i`。
	
	时间复杂度是 O(n)

## Code

### Python

```python
class Solution:
    # @param height, an integer[]
    # @return an integer
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        maxValue = 0
        while left < right:
            if height[left] < height[right]:
                maxValue = max(maxValue, (right - left) * height[left])
                left += 1
            else:
                maxValue = max(maxValue, (right - left) * height[right])
                right -= 1
        return maxValue
```

### C++

```cpp
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxValue = 0;
        while (left < right) {
            while (left < right && height[left] >= height[right]) {
                maxValue = max(maxValue, height[right] * (right - left));
                right--;
            }

			// 因为到现在右边的比左边的高，如果右边继续减小，不可能再找出更大的矩形了，所以换左边来搜索

            while (left < right && height[left] <= height[right]) {
                maxValue = max(maxValue, height[left] * (right - left));
                left++;
            }
        }
        return maxValue;
    }
};

// 代码可以进一步精简
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size() - 1;
        int maxValue = 0;
        while (left < right) {
			if (height[left] >= height[right]) {
				maxValue = max(maxValue, height[right] * (right - left));
				right--;
			} else {
				maxValue = max(maxValue, height[left] * (right - left));
				left++;
			}
        }
        return maxValue;
    }
};
```

## Challenge

咳咳，我是厚颜无耻加点内容来凑数的发言者zyx，毛神的代码简直无懈可击，在下佩服的五体投地，特来challenge解答的描述。

- 先用暴力得初解，再据题意破玄奇。毛神的解答可谓深得此道。
- 本题的题意中所能看到的规律就是：
	
	当选择了两跟柱子，比如柱子A和柱子B，假设柱子A高于柱子B，那么对于柱子AB之间的所有柱子，假设为C,D,E,F,..., 它们与B形成的柱子组合所能容纳的水，肯定比AB组合要少。原因如下：
	- 若C,D,E,...等柱子高度大于B，那么因为容水量与较低高度柱子相关，所以相对AB来说，较低高度柱子的高度没变，而C,D,E,...等柱子在AB之间，所以CB,DB,EB,...等组合的宽度变小，因而容水量变小。
	- 若C,D,E,...等柱子的高度小于B，那么宽度和较低高度柱子的高度同时变小，容水量显然更变小。
	
- 相信上一段描述与毛神的解释也是相同的，只不过更啰嗦的一点。但是从这个性质上可以导出，当达到AB这样的状态时，CB,DB,...,等组合是直接可以排除的，那么再加上当前状态AB，与B相关的状态就完全排除了。
> 旁白先生：“等等，与B相关的状态完全排除了。我读书少，你表骗我，你只是排除了AB之间的柱子，AB之外的柱子呢？你不说出个道道来信不信我分分钟砍四你。” 且看我下面的分解。
- 针对旁白先生的问题，我要说的是，这个算法非常有必要选一个好的起点。最开始，我选最左端和最右端的两跟柱子做起点，假设为A和B1，B1柱子比A要低。此时，旁白先生不得不承认AB1之外没有柱子。此时，将B1向内移动，到达B柱子，使得，height(B) > height(B1)，这是AB的容量才有可能大于AB1。注意此时的性质：
	- A和BB1之间的所有柱子的组合都小于AB1，
	- B和BB1之间的所有柱子的组合都小于AB1，
	- AB和AB1两个组合的大小不确定。
	- BB1之间的柱子和AB之间的柱子的任何组合都小于AB1。
	
- 所以，此时，BB1之间的柱子都可以不考虑了。AB组合B外侧的柱子解决，当然，对A也是同理。此时，若height(A) > height(B)，那么，B还得再往AB之间移动，找到一个比B还要高的柱子B2。若height(A) < height(B)，则移动A。若两者相等，则随便选一个往内移动即可。

### 更深层次的理解

> 旁白先生：“这个题我自己就能想出来了，你为毛讲这么多？”

从这道题中，可以看到，若选择最外侧两端作为初始状态，那根据当前两根柱子的高低状态，就能很确定的移动一根柱子，使得到的结果一定是最大值的候选（此时需要保存一个全局变量，若得到的值最大，更新全局变量即可）。而且忽略了很多确认不是最优解的候选。

	这样的算法就是贪心算法。
	
回顾我们刚才的分析，贪心算法的两大要素就是：

- 起点选的好；
- 根据当前状态能够选出一条正确的路，忽略很多候选解，进一步缩小搜索的范围。

所以，贪心算法的口诀就是：

	贪心大法出身好，正确路线永不倒。

### Init Code

根据上面的描述，写出下面的代码，代码精简后跟毛神的代码一样，可见，毛神做了多少工作！ 银河啊，原谅我在这里投机倒把。

```python

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        begin_i = 0
        end_i = len(height) - 1
        max_area = min(height[begin_i], height[end_i]) * (end_i - begin_i)
        while begin_i < end_i:
            if height[begin_i] <= height[end_i]:
                tmp = begin_i + 1
                while tmp < end_i and height[tmp] < height[begin_i]:
                    tmp += 1
                begin_i = tmp
            elif height[begin_i] > height[end_i]:
                tmp = end_i - 1
                while tmp > begin_i and height[tmp] < height[end_i]:
                    tmp -= 1
                end_i = tmp
            tmp = min(height[begin_i], height[end_i]) * (end_i - begin_i)
            if tmp > max_area:
                max_area = tmp
        return max_area
```