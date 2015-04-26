# 110-Balanced Binary Tree

## Problem

> Given a binary tree, determine if it is height-balanced.

> For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

## Solution

- 递归，判断左子树是否平衡且返回左子树的高度， 判断右子树是否平衡且返回右子树的高度，当左右子树都平衡且左右子树的高度差不大于1时，该树平衡。

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.balance(root)[1]
    
    def balance(self, node):
        if node == None:
            return 0, True
        l_height, is_left  = self.balance(node.left)
        r_height, is_right = self.balance(node.right)
        return max(l_height, r_height)+1, is_left and is_right and abs(l_height - r_height) <= 1
```

### C++

```cpp
class Solution {
public:
    bool isBalanced(TreeNode *root) {
        int height = 0;
        return balance(root, height);
    }
    bool balance(TreeNode *node, int &height) {
        if (node == NULL) {
            return true;
        }
        int l_height = 0;
        int r_height = 0;
        bool is_left  = balance(node->left,  l_height);
        bool is_right = balance(node->right, r_height);
        height = max(l_height, r_height) + 1;
        return is_left && is_right && abs(l_height - r_height) <=1;
        
    }
};
```