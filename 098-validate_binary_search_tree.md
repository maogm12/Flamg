# 098-Validate Binary Search Tree

## Problem

> Given a binary tree, determine if it is a valid binary search tree (BST).

> Assume a BST is defined as follows:
>
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

> 判断一个二叉树是不是二叉搜索树。

## Solution

二叉搜索树的性质是对于一个节点，其左子树中的数都比该节点小，右子树中的数都比该节点大。

对于树这种结构，需要经常使用递归，此题也不例外。本题有两种递归方法：

- 自上而下：定义两个变量，上限high和下限low，那么，访问当前节点node，若当前节点在上下限之间，那么其左子树必须在low，node.val之间；右子树必须在node.val,high之间。该方法相当于先序遍历。
- 自下而上：对于一个节点，先访问其左子树，返回其最大值left_max和最小值left_min，再访问其右子树，返回其最大值right_max和最小值right_min。然后对当前节点node判断，left_max < node.val < right_min,然后返回left_min,right_max作为该节点所代表子树的最大值和最小值。该方法相当于后序遍历。

- 中序遍历法

	二叉搜索树的中序遍历为有序的，若树里面没有重复的节点，可用中序遍历解

## Code

### Python for Up-to-Down

```python
class Solution:
    # @param root, a tree node
    # @return a boolean
	def isValidBST(self, root):
	    return self.is_valid(root, -2**32, 2**32)

	def is_valid(self, node, low, high):
	    if node == None:
	        return True
	    return low < node.val < high and self.is_valid(node.left, low, node.val) and self.is_valid(node.right, node.val, high)

```
### Python for Down-to-Up

```python

class Solution:
    # @param root, a tree node
    # @return a boolean
	def isValidBST(self, root):
		if root == None:
			return True
		return self.is_valid(root)[2]

	def is_valid(self, root):
		if root.left == None and root.right == None:
			return root.val, root.val, True
		elif root.left == None:
			min_value, max_value, is_v = self.is_valid(root.right)
			if is_v and root.val < min_value:
				return root.val, max_value, True
			else:
				return -1, -1, False
		elif root.right == None:
			min_value, max_value, is_v = self.is_valid(root.left)
			if is_v and root.val > max_value:
				return min_value, root.val, True
			else:
				return -1, -1, False
		else:
			min_left,  max_left,  is_v_left  = self.is_valid(root.left)
			min_right, max_right, is_v_right = self.is_valid(root.right)
			if is_v_left and is_v_right and max_left < root.val < min_right:
				return min_left, max_right, True
			else:
				return -1, -1, False

```

### C++

```cpp
class Solution {
public:
    bool isValidBST(TreeNode *root) {
        return is_valid(root, 0, 0, false, false);
    }
    bool is_valid(TreeNode *node, int low, int high, bool have_low, bool have_high) {
        if (node == NULL) {
            return true;
        }
        if (have_low && node->val <= low) {
            return false;
        }
        if (have_high && node->val >= high) {
            return false;
        }
        return is_valid(node->left, low, node->val, have_low, true) && is_valid(node->right, node->val, high, true, have_high);
    }
};
```

中序遍历法迭代版

```cpp
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        TreeNode *cur = root, *pre = nullptr;
        stack<TreeNode*> s;
        while (cur) {
            s.push(cur);
            cur = cur->left;
        }

        while (!s.empty()) {
            cur = s.top(); s.pop();
            if (pre && pre->val >= cur->val) {
                return false;
            }
            pre = cur;
            cur = cur->right;
            while (cur) {
                s.push(cur);
                cur = cur->left;
            }
        }

        return true;
    }
};
```
