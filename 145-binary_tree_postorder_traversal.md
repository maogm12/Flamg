# 145-Binary_Tree_Postorder_Traversal

## Question


> Given a binary tree, return the postorder traversal of its nodes' values.

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
return [3,2,1].

> Note: Recursive solution is trivial, could you do it iteratively?

## Solution

数据结构基础题目，虽然也是hard，当然，非递归是hard。树的后续遍历是指对某个节点，先遍历树的左子树，然后遍历右子树，最后访问当前节点。

具体做法：

1 从当前节点一路向左，直到左子节点为NULL，将这些节点压入栈中

2 从栈中弹出一个节点，这样，它的左子树肯定已经访问过了，因为左子结点在栈中的顺序肯定比它先弹出。

3 判断右子树是否已经访问过了，这就需要记录上一个弹出的节点
> 3.1 如果上一个弹出的节点是该节点的右子节点，则右子树已访问过，那么访问当前节点。

> 3.2 如果上一个弹出的节点不是右子节点，则将该节点压入栈中，再对其右子节点做一路向左的压栈操作。

4 返回第2步

## Code

### python

```python
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        result = []
        stack = []
        node = root
        while node != None:
            stack.append(node)
            node = node.left
        pre_pop_node = None
        while len(stack) > 0:
            node = stack.pop()
            if node.right == pre_pop_node or node.right == None:
                result.append(node.val)
                pre_pop_node = node
            else:
                stack.append(node)
                node = node.right
                while node != None:
                    stack.append(node)
                    node = node.left
        return result
```

### cpp

```cpp
class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        vector<TreeNode *> stack;
        vector<int> result;
        TreeNode *node = root;
        TreeNode *pre_pop_node = NULL;
        while (node != NULL) {
            stack.push_back(node);
            node = node->left;
        }
        while (stack.size() != 0) {
            node = *(stack.end() - 1);
            stack.pop_back();
            if (node->right == pre_pop_node || node->right == NULL) {
                result.push_back(node->val);
                pre_pop_node = node;
            } else {
                stack.push_back(node);
                node = node->right;
                while (node != NULL) {
                    stack.push_back(node);
                    node = node->left;
                }
            }
        }
        return result;
    }
};
```
