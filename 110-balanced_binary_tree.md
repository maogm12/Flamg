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

This is speaker mgm, 我觉得祥爷的解法不好，哦，不是，是祥爷的解法很好，但是不太符合最优解法的预期，唉，当个程序猿企业家真TM难

该解法中我们有两个值需要返回，一个是该子树是否为平衡的，还有一个就是字数的高度，以便上一层继续判断。但是喜家家不能返回多个值，搞毛啊，引用传递来救命。（估计祥爷要跳出来当头一棒，这特喵的不就是我的解法么）

改进就是我们可以用 `-1` 来表示树是不平衡的，这样我们可以省去引用传递的 `height` 参数，让代码更紧凑，有张力（扯犊子）

```cpp
class Solution {
public:
    bool isBalanced(TreeNode* root) {
        return calculateHeight(root) != -1;
    }
private:
    int calculateHeight(TreeNode *root) {
        if (!root) {
            return 0;
        }

        int leftHeight = calculateHeight(root->left);
        if (leftHeight == -1) {
            return -1;
        }
        int rightHeight = calculateHeight(root->right);
        if (rightHeight == -1) {
            return -1;
        }
        return abs(leftHeight - rightHeight) <= 1 ? max(leftHeight, rightHeight) + 1 : -1;
    }
};
```
