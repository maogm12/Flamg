# 108-Convert Sorted Array to Binary Search Tree

## Problem

> Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

## Solution

- 递归法

    每次取数组最中间的元素做根节点，然后递归生成左右子树

## Code

### Python

```python
# blah
```

### C++

```cpp
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        function<TreeNode*(int, int)> build = [&](int begin, int end) {
            if (begin == end) { return (TreeNode*)nullptr; }
            int mid = (begin + end) / 2;
            TreeNode *root = new TreeNode(nums[mid]);
            root->left = build(begin, mid);
            root->right = build(mid + 1, end);
            return root;
        };

        return build(0, nums.size());
    }
};
```
