# 089-Gray_Code

## Question
> The gray code is a binary numeral system where two successive values differ in only one bit.

> Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

> For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

>```
00 - 0
01 - 1
11 - 3
10 - 2
```

> Note:
> For a given n, a gray code sequence is not uniquely defined.

> For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

> For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.

## Solution

- 典型的回溯问题，先声明一个长度为n的0/1数组：
	- 控制第1位不变
	- 变换第2-n位
	- 第一位反转
	- 再变换第2-n位
以此类推

- 回溯方法之二，通过题目中的那个只有两位的示例也可发现，第一个数和第二个数与第三个数和第四个数其实是有关系的，即，第一个数和第二个数顺序变化后再加上2即得到第三个数和第四个数。可以利用此性质来结题

## Code

### python code

- 第一种解法：

```python
class Solution:
    # @return a list of integers
	def grayCode(self, n):
		if n == 0:
			return [0]
		num = [0 for i in range(n)]
		results = []
		self.generate(0, num, results)
		return results
	
	def generate(self, index, num, results):
		if index == len(num):
			result = self.binary2num(num)
			results.append(result)
			return
		self.generate(index+1, num, results)
		num[index] = 1 - num[index]
		self.generate(index+1, num, results)
	
	# 将0/1数组转换为整数
	def binary2num(self, num):
		result = 0
		for i in range(len(num)):
			result += num[i] * (2**(len(num) - i - 1))
		return result
```

- 第二种解法：

```python
class Solution:
    # @param n, an integer
    # @return an integer[]
    def grayCode(self, n):
        if n == 0:
            return [0]
        result = [0, 1]
        i = 1
        product = 1
        while i < n:
            product *= 2
            j = len(result)-1
            while j >= 0:
                result.append(result[j] + product)
                j -= 1
            i += 1
        return result
```

### cpp code

- 第二种解法

```cpp
class Solution {
public:
    vector<int> grayCode(int n) {
        vector<int> result;
        result.push_back(0);
        if (n == 0) {
            return result;
        }
        result.push_back(1);
        int i = 1, product = 1;
        while (i < n) {
            product *= 2;
            int j = result.size() - 1;
            while (j >= 0) {
                result.push_back(result[j] + product);
                j--;
            }
            i++;
        }
        return result;
    }
};
```



