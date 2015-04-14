# 001-Two Sum

## Question

> 给定一个数组，从数组中找出两个数，使两个数之和等于特定值。

具体要求：

给定数组numbers和特定值target，返回数组中两个数的索引，索引从1开始算， 假定数组中一定存在两个数，它们之和是target。


## Solution

- 暴力算法

	枚举所有的两位数的组合，查看是否有和target相等的组合。时间复杂度为O(n<sup>2</sup>)，空间复杂度为O(1)。

- 排序算法
	
	先将数组排序，然后使用双指示器，从前后两端向中间进发，若双指示器指向的两个值之和大于目标值，则第二个指示器减1；反之，其和小于目标值，则第一个指示器加1。该方法需要记录数字在原始数组中的位置。该方法时间复杂度为O(nlog(n))，空间复杂度为O(n)。

- 映射算法

	使用字典存储，字典的key是数组中的数字，value是数字的索引。对于数组中的一个数a，在字典中查找target-a，若查找得到，则此两个数即为结果。
	
	若使用哈希字典，该方法时间复杂度为O(n)，空间复杂度也为O(n)。
	若使用树字典，该方法时间复杂度为O(nlog(n))，空间复杂度为O(n)。
	
综上所述，基于哈希字典的方法最优。

## code

### python code
	
	class Solution:
		# @return a tuple, (index1, index2)
		def twoSum(self, num, target):
			len_num = len(num)
			index_dict = {}
			i = 0
			while i < len_num:
				value = target - num[i]
				if value in index_dict:
					return (index_dict[value]+1, i+1)
				else:
					index_dict[num[i]] = i
					i += 1

### cpp code

> 在下面的代码中，unordered_map可用map替代。

	class Solution {
	public:
		vector<int> twoSum(vector<int> &numbers, int target) {
			vector<int> result;
			unordered_map<int, int> map_numbers;
			unordered_map<int, int>::iterator find_iter;
			for (int i=0; i < numbers.size(); i++) {
				int num = numbers[i];
				int minus_num = target - num;
				find_iter = map_numbers.find(minus_num);
				if (find_iter == map_numbers.end()) {
					map_numbers.insert(make_pair(num, i));
				} else {
					result.push_back(find_iter->second + 1);
					result.push_back(i+1);
					break;
				}
			}
			return result;
		}
	};







