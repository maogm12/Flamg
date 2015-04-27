# 094-Binary Tree Inorder Traversal

## Problem

> Given a binary tree, return the inorder traversal of its nodes' values.

> For example:
Given binary tree {1,#,2,3},
>
```
   1
    \
     2
    /
   3
```
return [1,3,2].

> Note: Recursive solution is trivial, could you do it iteratively?

## Solution

> 非递归遍历：中序遍历的顺序是
> 
	- 访问左子树
	- 访问当前节点
	- 访问右子树

> 所以，在访问某个节点的时候，需要保证其左子树已被访问，然后如果其有右子树，访问其右子树。

- 使用栈来非递归的解决中序遍历，具体操作如下：
	1. 当前节点一路向左走全都压入栈中，直至左子结点为NULL(这样保证栈中元素弹出被访问的时候，其左子树都被访问)
	2. 从栈中弹出节点node，访问它
	3. 如果node有右子节点，那么从右子节点开始，再一路向左走，所遇节点全都压入栈中。(如果有右子树，访问其右子树)


## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack  = []
        result = []
        node = root
        while node != None:
            stack.append(node)
            node = node.left
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)
            node = node.right
            while node != None:
                stack.append(node)
                node = node.left
        return result
```

### C++

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<TreeNode *> stack;
        vector<int> result;
        TreeNode *node = root;
        while (node != NULL) {
            stack.push_back(node);
            node = node->left;
        }
        while (stack.size() != 0) {
            node = stack.back();
            stack.pop_back();
            result.push_back(node->val);
            node = node->right;
            while (node != NULL) {
                stack.push_back(node);
                node = node->left;
            }
        }
        return result;
    }
};
```