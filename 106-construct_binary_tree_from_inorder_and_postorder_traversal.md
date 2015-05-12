# 106-Construct Binary Tree from Inorder and Postorder Traversal

## Problem

> Given inorder and postorder traversal of a tree, construct the binary tree.

> Note:
You may assume that duplicates do not exist in the tree.

## Solution

后序遍历是左子树->右子树->当前节点
中序遍历是左子树->当前节点->右子树
又因为没有重复元素存在，所以，可以递归的方法进行构造。

- 递归：
	- 从后序遍历中取出当前节点
	- 在中序遍历中找到当前节点位置，那么中序遍历该节点位置的左侧就是左子树，右侧就是右子树，可以根据左右子树的数目在先序遍历中找到对应的左子树节点和右子树节点
	- 构造左子树
	- 构造右子树
	- 当前节点所代表的树构建成功


## Code

### Python

```python
class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self.build(inorder, postorder, 0, len(inorder)-1, 0, len(postorder)-1)

    def build(self, inorder, postorder, ib, ie, pb, pe):
        if ib > ie or pb > pe:
            return None
        num = postorder[pe]
        index = self.find_in(inorder, ib, ie, num)
        node = TreeNode(num)
        node.left = self.build(inorder, postorder, ib, index-1, pb, pb+index-ib-1)
        node.right = self.build(inorder, postorder, index+1, ie, pb+index-ib, pe-1)
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
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        return build(inorder, postorder, 0, inorder.size()-1, 0, postorder.size()-1);
    }
    TreeNode *build(vector<int> &inorder, vector<int> &postorder, int ib, int ie, int pb, int pe) {
        if (ib > ie || pb > pe) {
            return NULL;
        }
        int num = postorder[pe];
        int index = find_in(inorder, ib, ie, num);
        TreeNode *node = new TreeNode(num);
        node->left  = build(inorder, postorder, ib, index-1, pb, pb+index-ib-1);
        node->right = build(inorder, postorder, index+1, ie, pb+index-ib, pe-1);
        return node;
    }
    int find_in(vector<int> &inorder, int ib, int ie, int num) {
        for (int i = ib; i <= ie; i++) {
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        typedef vector<int>::iterator Itor;
        function<TreeNode*(Itor, Itor, int)> build = [&](Itor inStart, Itor postStart, int size) {
            TreeNode* root = nullptr;
            if (size == 0) return root;
            int val = *(postStart + size - 1);
            root = new TreeNode(val);
            auto pos = find(inStart, inStart + size, val);
            int leftSize = pos - inStart;
            int rightSize = size - leftSize - 1;
            root->left = build(inStart, postStart, leftSize);
            root->right = build(pos + 1, postStart + leftSize, rightSize);
            return root;
        };

        return build(inorder.begin(), postorder.begin(), inorder.size());
    }
};
```
