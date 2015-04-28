# 107-Binary Tree Level Order Traversal II

## Problem

> Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

> For example:
Given binary tree {3,9,20,#,#,15,7},
>
```
    3
   / \
  9  20
    /  \
   15   7
```
> return its bottom-up level order traversal as:
>
```
[
  [15,7],
  [9,20],
  [3]
]
```

## Solution

- 与102问题类似，使用队列类似的数据结构进行BFS，即访问当前节点时，将其左右子节点加到队列的末尾。
- 在返回结果之前，将结果反转即可

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
		if root == None:
			return []
		results = []
		queue = [root]
		begin = 0
		end   = 1
		result = []
		while begin < end:
			node = queue[begin]
			if node.left != None:
				queue.append(node.left)
			if node.right != None:
				queue.append(node.right)
			result.append(node.val)
			if begin == end - 1:
				results.append(result)
				result = []
				end = len(queue)
			begin += 1
		results.reverse()
		return results
```

### C++

```cpp
class Solution {
public:
    vector<vector<int> > levelOrderBottom(TreeNode *root) {
        vector<vector<int> > results;
        vector<int> result;
        
        if (root == NULL) {
            return results;
        }
        
        vector<TreeNode *> levels;
        levels.push_back(root);
        
        int begin = 0, end = 1;
        TreeNode *node = NULL;
        
        while (begin < end) {
            node = levels[begin];
            result.push_back(node->val);
            if (node->left != NULL) {
                levels.push_back(node->left);
            }
            if (node->right != NULL) {
                levels.push_back(node->right);
            }
            if (begin == end - 1) {
                results.push_back(result);
                result.clear();
                end = levels.size();
            }
            begin++;
        }
        reverse(results.begin(), results.end());
        return results;
    }
};
```