# 114-Flatten Binary Tree to Linked List

## Problem

> Given a binary tree, flatten it to a linked list in-place.

> For example,
> Given
>
         1
        / \
       2   5
      / \   \
     3   4   6
> The flattened tree should look like:
>
	1
	 \
	  2
	   \
	    3
	     \
	      4
	       \
	        5
	         \
	          6

## Solution

从题目中看，是将树节点的右子树指针作为链表的指针。

- 递归解法

	对于一个节点node，
	- 将其左子树展平，返回左子树展平链表的开始和结尾节点
	- 将其右子树展平，返回右子树展平链表的开始和结尾节点
	- 将node和这两个链表链接起来

	> 优化：每个展平链表的开始节点必然是根节点，所以只需返回展平链表的结尾节点即可。

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.sub_flatten(root)
    
    def sub_flatten(self, node):
        if node == None:
            return None, None
        left_begin, left_end   = self.sub_flatten(node.left)
        right_begin, right_end = self.sub_flatten(node.right)
        node.left = None
        node.right = None
        current_end = node
        if left_begin != None:
            current_end.right = left_begin
            current_end = left_end
        if right_begin != None:
            current_end.right = right_begin
            current_end = right_end
        return node, current_end
```

### Optimized Python

```python
class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.sub_flatten(root)
    
    def sub_flatten(self, node):
        if node == None:
            return None
        left_begin  = node.left
        right_begin = node.right
        node.left  = None
        node.right = None
        left_end  = self.sub_flatten(left_begin)
        right_end = self.sub_flatten(right_begin)
        
        current_end = node
        if left_begin != None:
            current_end.right = left_begin
            current_end = left_end
        if right_begin != None:
            current_end.right = right_begin
            current_end = right_end
        return current_end
```

### C++

```cpp
class Solution {
public:
    void flatten(TreeNode *root) {
        sub_flatten(root);
    }
    TreeNode* sub_flatten(TreeNode *node) {
        if (node == NULL) {
            return NULL;
        }
        TreeNode *left_begin  = node->left;
        TreeNode *right_begin = node->right;
        node->left  = NULL;
        node->right = NULL;
        TreeNode *left_end = sub_flatten(left_begin);
        TreeNode *right_end = sub_flatten(right_begin);
        TreeNode *current_end = node;
        if (left_begin != NULL) {
            current_end->right = left_begin;
            current_end = left_end;
        }
        if (right_begin != NULL) {
            current_end->right = right_begin;
            current_end = right_end;
        }
        return current_end;
    }
};
```