# 100-Same Tree

## Problem

> Given two binary trees, write a function to check if they are equal or not.

> Two binary trees are considered equal if they are structurally identical and the nodes have the same value.

## Solution

- 递归，两颗树相同需满足一下条件：
	- 当前节点相同
	- 当前节点的左子树相同
	- 当前节点的右子树相同

> 相当于先序遍历

## Code

### Python

```python
class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
```

### C++

```cpp
class Solution {
public:
    bool isSameTree(TreeNode *p, TreeNode *q) {
        if (p == NULL && q == NULL) {
            return true;
        } else if (p == NULL || q == NULL) {
            return false;
        } else {
            return p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
    }
};
```

精简版 by mgm

```cpp
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        return !p && !q || p && q && isSameTree(p->left, q->left) && isSameTree(p->right, q->right) && p->val == q->val;
    }
};
```
