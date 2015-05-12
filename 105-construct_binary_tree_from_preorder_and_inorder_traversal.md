# 105-Construct Binary Tree from Preorder and Inorder Traversal

## Problem

> Given preorder and inorder traversal of a tree, construct the binary tree.

> Note:
You may assume that duplicates do not exist in the tree.

## Solution

先序遍历是当前节点->左子树->右子树
中序遍历是左子树->当前节点->右子树
又因为没有重复元素存在，所以，可以递归的方法进行构造。

- 递归：
	- 从先序遍历中取出当前节点
	- 在中序遍历中找到当前节点位置，那么中序遍历该节点位置的左侧就是左子树，右侧就是右子树，可以根据左右子树的数目在先序遍历中找到对应的左子树节点和右子树节点
	- 构造左子树
	- 构造右子树
	- 当前节点所代表的树构建成功

## Code

### Python

```python
class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.build(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)

    def build(self, preorder, inorder, pb, pe, ib, ie):
        if pb > pe:
            return None
        num = preorder[pb]
        index = self.find_in(inorder, ib, ie, num)
        node = TreeNode(num)
        node.left = self.build(preorder, inorder, pb+1, pb+index-ib, ib, index-1)
        node.right = self.build(preorder, inorder, pb+index-ib+1, pe, index+1, ie)
        return node

    def find_in(self, inorder, ib, ie, num):
        for i in range(ib, ie+1):
            if inorder[i] == num:
                return i
        return -1
```

### C++

```cpp
class Solution {
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        return build(preorder, inorder, 0, preorder.size()-1, 0, inorder.size()-1);
    }
    TreeNode *build(vector<int> &preorder, vector<int> &inorder, int pre_b, int pre_e, int in_b, int in_e) {
        if (pre_b > pre_e) {
            return NULL;
        }
        int num = preorder[pre_b];
        int index = find_in(inorder, in_b, in_e, num);
        TreeNode *node = new TreeNode(num);
        node->left = build(preorder, inorder, pre_b+1, pre_b+index-in_b, in_b, index-1);
        node->right = build(preorder, inorder, pre_b+index-in_b+1, pre_e, index+1, in_e);
        return node;

    }
    int find_in(vector<int> &inorder, int b, int e, int num) {
        for (int i = b; i <= e; i++) {
            if (inorder[i] == num) {
                return i;
            }
        }
        return -1;
    }
};
```

use lambda

```cpp
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        typedef vector<int>::iterator Itor;
        function<TreeNode*(Itor,Itor,int)> build = [&](Itor prestart, Itor instart, int size) {
            TreeNode *root = nullptr;
            if (size == 0) { return root; }
            root = new TreeNode(*prestart);
            auto pos = find(instart, instart + size, *prestart);
            int leftSize = pos - instart;
            int rightSize = size - leftSize - 1;
            root->left = build(prestart + 1, instart, leftSize);
            root->right = build(prestart + 1 + leftSize, pos + 1, rightSize);
            return root;
        };

        return build(preorder.begin(), inorder.begin(), preorder.size());
    }
};
```
