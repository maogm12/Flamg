# 144-Binary_Tree_Preorder_Traversal

## Question

> Given a binary tree, return the preorder traversal of its nodes' values.

> For example:
> Given binary tree {1,#,2,3},
>
```
   1
    \
     2
    /
   3
```
return [1,2,3].

> Note: Recursive solution is trivial, could you do it iteratively?

## Solution

先序遍历是指先访问当前节点，然后访问当前节点的左子树，然后访问右子树。其非递归的流程可以使用一个栈实现：


1. 将跟节点压入栈
2. 栈不为空时，进行如下操作：
	- 弹出栈尾节点，并访问该节点
	- 如果该节点右子节点不空，加入到栈
	- 如果该节点左子节点不空，加入到栈
	- 继续第2步
	
## Code

### python

```python
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        if root == None:
            return result
        stack = [root]
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)
        return result
```

### cpp

```cpp
class Solution {
public:
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> result;
        vector<TreeNode *> stack;
        if (root == NULL) {
            return result;
        }
        stack.push_back(root);
        TreeNode *node;
        while (stack.size() != 0) {
            node = *(stack.end() - 1);
            result.push_back(node->val);
            stack.pop_back();
            if (node->right != NULL) {
                stack.push_back(node->right);
            }
            if (node->left != NULL) {
                stack.push_back(node->left);
            }
        }
        return result;
    }
};
```