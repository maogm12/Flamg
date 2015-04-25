# 112-Path Sum

## Problem

> Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

> For example:
Given the below binary tree and sum = 22,

>
```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
```
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

## Solution

- 递归，保存到从根节点到当前节点的路径和，再将该和传递给当前节点的左右子节点。

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        return self.path_sum(root, sum, 0)
    def path_sum(self, node, sum, current_sum):
        if node == None:
            return False
        current_sum += node.val
        if node.left == None and node.right == None:
            if current_sum == sum:
                return True
            return False
        return self.path_sum(node.left, sum, current_sum) or self.path_sum(node.right, sum, current_sum)
```

### C++

```cpp
class Solution {
public:
    bool hasPathSum(TreeNode *root, int sum) {
        return sum_path(root, sum, 0);
        
    }
    bool sum_path(TreeNode *node, int sum, int current_sum) {
        if (node == NULL) {
            return false;
        }
        current_sum += node->val;
        if (node->left == NULL && node->right == NULL) {
            if (current_sum == sum) {
                return true;
            }
            return false;
        } 
        return sum_path(node->left, sum, current_sum) || sum_path(node->right, sum, current_sum);
    }
};
```