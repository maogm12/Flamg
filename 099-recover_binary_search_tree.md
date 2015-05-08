# 099-Recover Binary Search Tree

## Problem

> Two elements of a binary search tree (BST) are swapped by mistake.

> Recover the tree without changing its structure.

> **Note:**

> A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

## Solution

- 栈遍历法

    即使用普通中序遍历法

    二叉搜索树有一个牛逼闪闪的性质，就是中序遍历是有序的，如果两个节点交换过了，中序遍历必定会出现不有序的地方（后面的数比前面小），那就是异常点，有两种情况：

    1. 相邻的两点交换，比如 `[1,2,3,4]` 变成 `[1,3,2,4]` 有1个点异常
    2. 不相邻的两点交换，比如 `[1,2,3,4]` 变成 `[4,2,3,1]` 有2个点异常

  可惜普通的中序遍历是要一个栈的，时间复杂度为 O(n)

- Morris 中序遍历法

    [Morris 中序遍历请看这里](./094-binary_tree_inorder_traversal.md)

    空间复杂度为 O(1) 哦~~~

## Code

### Python

```python

```

### C++

栈法

```cpp
class Solution {
public:
    void recoverTree(TreeNode* root) {
        vector<TreeNode*> inorder;
        // 记录异常点
        TreeNode *first = nullptr, *second = nullptr;
        stack<TreeNode*> s;
        TreeNode *node = root;
        while (node) {
            s.push(node);
            node = node->left;
        }
        while (!s.empty()) {
            node = s.top(); s.pop();

            // 检测是否是异常的
            if (!inorder.empty()) {
                auto back = inorder.back();
                if (back->val > node->val) {
                    first = second ? first : back;
                    if (second) {
                        // 已经有两处异常，可以返回了
                        second = node;
                        break;
                    }
                    second = node;
                }
            }

            inorder.push_back(node);
            node = node->right;
            while (node) {
                s.push(node);
                node = node->left;
            }
        }

        if (first && second) {
            swap(first->val, second->val);
        }
    }
};
```

Morris 法

```cpp
class Solution {
public:
    void recoverTree(TreeNode* root) {
        TreeNode* current = root, *prev = nullptr ,*node;
        TreeNode *first = nullptr, *second = nullptr;
        // 检查是否是异常点
        auto detect = [&] {
            if (prev && current && prev->val > current->val) {
                first = first ? first : prev;
                second = current;
            }
        };
        while (current) {
            if (current->left == nullptr) {
                // 这里要先检测，应为 current->right 并不一定是 current 的后趋节点
                detect();
                prev = current;
                current = current->right;
            } else {
                node = current->left;
                while (node->right != nullptr && node->right != current) {
                    node = node->right;
                }

                if (node->right == nullptr) {
                    node->right = current;
                    current = current->left;
                } else {
                    // 这里也要先检测，应为 current->right 并不一定是 current 的后趋节点
                    detect();
                    node->right = nullptr;
                    prev = current;
                    current = current->right;
                }
            }
        }

        if (first && second) {
            swap(first->val, second->val);
        }
    }
};
```
