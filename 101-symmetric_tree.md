# 101-Symmetric Tree

## Problem

> Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

> For example, this binary tree is symmetric:
>
```
    1
   / \
  2   2
 / \ / \
3  4 4  3
```
> But the following is not:

>
```
    1
   / \
  2   2
   \   \
   3    3
```

> Note:
Bonus points if you could solve it both recursively and iteratively.

## Solution

- 递归，对于两个节点来说，判断它们所代表的子树是否对称，需要判断如下三个方面：
	- 两个节点相等
	- A节点的左子树和B节点的右子树相等
	- A节点的右子树和B节点的左子树相等


## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root == None:
            return True
        return self.is_sy(root.left, root.right)

    def is_sy(self, l_node, r_node):
        if l_node == None and r_node == None:
            return True
        elif l_node == None or r_node == None:
            return False
        else:
            return l_node.val == r_node.val \
            and self.is_sy(l_node.left, r_node.right) \
            and self.is_sy(l_node.right, r_node.left)
```

### C++

```cpp
class Solution {
public:
    bool isSymmetric(TreeNode *root) {
        if (root == NULL) {
            return true;
        }
        return is_sy(root->left, root->right);
    }
    bool is_sy(TreeNode *l_node, TreeNode *r_node) {
        if (l_node == NULL && r_node == NULL) {
            return true;
        } else if (l_node == NULL || r_node == NULL) {
            return false;
        } else {
            return l_node->val == r_node->val && is_sy(l_node->left, r_node->right) && is_sy(l_node->right, r_node->left);
        }
    }
};
```

迭代版

```cpp
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if (!root) return true;
        vector<TreeNode*> level;
        queue<TreeNode*> q;
        TreeNode *node;
        q.push(root);
        while (!q.empty()) {
            auto size = q.size();
            (vector<TreeNode*>()).swap(level);
            for (auto i = 0; i < size; ++i) {
                node = q.front();
                q.pop();
                level.push_back(node);
                if (node) {
                    q.push(node->left);
                    q.push(node->right);
                }
            }

            for (auto i = 0; i < size / 2; ++i) {
                auto low = level[i], high = level[size - 1 -i];
                if (!low && !high || low && high && low->val == high->val) {
                    continue;
                } else {
                    return false;
                }
            }
        }

        return true;
    }
};
```
