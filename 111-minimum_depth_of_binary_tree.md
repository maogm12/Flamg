# 111-Minimum Depth of Binary Tree

## Problem

> Given a binary tree, find its minimum depth.

> The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

## Solution

- 递归，对于当前节点，计算左子树的最小深度left，右子树的最小深度right，当前节点所代表的树的最小深度就是min(left,right)+1.

－ 迭代，层次遍历

    BFS，扫描到节点为叶子节点停止

    时间复杂度 O(n)，空间复杂度 O(n)

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        elif root.left == None:
            return self.minDepth(root.right) + 1
        elif root.right == None:
            return self.minDepth(root.left) + 1
        else:
            min_left = self.minDepth(root.left)
            min_right = self.minDepth(root.right)
            return min(min_left, min_right) + 1
```

### C++

```cpp
class Solution {
public:
    int minDepth(TreeNode *root) {
        if (root == NULL) {
            return 0;
        }
        if (root->left == NULL && root->right == NULL) {
            return 1;
        } else if (root->right == NULL) {
            return minDepth(root->left) + 1;
        } else if (root->left  == NULL) {
            return minDepth(root->right) + 1;
        } else {
            int min_left  = minDepth(root->left);
            int min_right = minDepth(root->right);
            return min(min_left, min_right) + 1;
        }
    }
};
```

```cpp
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> q;
        q.push(root);
        int level = 0;
        TreeNode* node;
        while (!q.empty()) {
            level++;
            int size = q.size();
            while (size--) {
                node = q.front(); q.pop();
                if (node->left == nullptr && node->right == nullptr) {
                    return level;
                }

                if (node->left) {
                    q.push(node->left);
                }

                if (node->right) {
                    q.push(node->right);
                }
            }
        }

        return level;
    }
};
```
