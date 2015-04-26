# 104-Maximum Depth of Binary Tree

## Problem

> Given a binary tree, find its maximum depth.

> The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

## Solution

- 递归,当前节点所代表树的最大深度为左子树最大深度与右子树最大深度的最大值加1.

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
```

### C++

```cpp
class Solution {
public:
	int maxDepth(TreeNode *root) {
		if (root == NULL) {
		    return 0;
		}
		return max(maxDepth(root->left), maxDepth(root->right)) + 1;
    }
};
```