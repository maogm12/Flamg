# 116-Populating Next Right Pointers in Each Node

## Problem

> Given a binary tree
>
    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.

> Initially, all next pointers are set to `NULL`.

> **Note**:
>
- You may only use constant extra space.
- You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

>
For example,
Given the following perfect binary tree,
>
```
         1
       /  \
      2    3
     / \  / \
    4  5  6  7
```
>
After calling your function, the tree should look like:
>
```
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
```

## Solution

- 递归，以上述样例的2、3节点为例，需要
	1. 2号节点的next指向3号节点
	2. 2号节点的两个子节点需要链接
	3. 3号节点的两个子节点需要链接
	4. 2号节点的右子节点指向3号节点的左子节点
	
	所以，递归算法就是先调第一步，然后递归调第2，3，4步
	
## Code

### Python

> 奇怪，cpp程序可以过，几乎同样的py却超时了，@mgm，元芳，你怎么看？

```python
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root != None:
            self.double_connect(root.left, root.right)
            
    def double_connect(self, l_node, r_node):
        if l_node != None:
            l_node.next = r_node
            self.double_connect(l_node.left, l_node.right)
            if r_node != None:
                self.double_connect(l_node.right, r_node.left)
                self.double_connect(r_node.left,  r_node.right)
```

### C++

```cpp
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root != NULL) {
            double_connect(root->left, root->right);
        }
    }
    void double_connect(TreeLinkNode *l_node, TreeLinkNode *r_node) {
        if (l_node != NULL) {
            l_node->next = r_node;
            double_connect(l_node->left, l_node->right);
            if (r_node != NULL) {
                double_connect(l_node->right, r_node->left);
                double_connect(r_node->left,  r_node->right);
            }
        }
    }
};
```