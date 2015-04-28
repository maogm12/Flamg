# 103-Binary Tree Zigzag Level Order Traversal

## Problem

> Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

> For example:
Given binary tree `{3,9,20,#,#,15,7}`,
>
```
    3
   / \
  9  20
    /  \
   15   7
```
>
return its zigzag level order traversal as:
>
```
[
  [3],
  [20,9],
  [15,7]
]
```

## Solution

- 使用队列类似的数据结构进行BFS，即访问当前节点时，将其左右子节点加到队列的末尾。
- 使用一个标志位来判断新的一层是否反转

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def zigzagLevelOrder(self, root):
		if root == None:
			return []
		results = []
		queue = [root]
		begin = 0
		end = 1
		is_reverse = False
		result = []
		while begin < end:
			node = queue[begin]
			if node.left != None:
				queue.append(node.left)
			if node.right != None:
				queue.append(node.right)
			result.append(node.val)
			if begin == end - 1:
			    if is_reverse:
			        result.reverse()
			    is_reverse = not is_reverse
			    results.append(result)
			    result = []
			    end = len(queue)
			begin += 1
		return results
```

### C++

```cpp
class Solution {
public:
    vector<vector<int> > zigzagLevelOrder(TreeNode *root) {
        vector<vector<int> > results;
        vector<int> result;
        
        if (root == NULL) {
            return results;
        }
        
        vector<TreeNode *> levels;
        levels.push_back(root);
        
        int begin = 0, end = 1;
        bool is_reverse = false;
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
                if (is_reverse) {
                    reverse(result.begin(), result.end());
                }
                is_reverse = !is_reverse;
                results.push_back(result);
                result.clear();
                end = levels.size();
            }
            begin++;
        }
        
        return results;
    }
};
```