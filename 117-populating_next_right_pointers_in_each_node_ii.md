# 117-Populating Next Right Pointers in Each Node II

## Problem

> Follow up for problem "Populating Next Right Pointers in Each Node".

> What if the given tree could be any binary tree? Would your previous solution still work?

> ***Note***:

> You may only use constant extra space.
For example,
Given the following binary tree,
>
```
         1
       /  \
      2    3
     / \    \
    4   5    7
```

> After calling your function, the tree should look like:
>
```
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
```

## Solution

与116问题不同，本问题中的树，不一定是完全的，所以，116中得解法不奏效了，比如上述题干中的树，因为3没有左子节点，所以5和7连接不上。

为了解决这个问题，往往首先想到的是BFS，但是显然，BFS空间复杂度不是O(1)，不能解决。`先用暴力得初解，再据题意破玄奇`。BFS可以被看成暴力算法，那么有什么东西可以代替BFS呢？

根据题意，将树的一层连上后，该层就成为了一个链表，你可以将这个链表看成是队列的一部分，然后将该层所有的子节点按照从左向右的顺序连接起来。相当于构建了一个新队列。

所以，本题的递归方法与前面树的递归方法不同，前面的树都是以子树为单位递归，本题是以层为单位递归。

## Code

### Python

```python
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        head = TreeLinkNode(0)
        
        father = root
        son = head
        while father != None:
            if father.left != None:
                son.next = father.left
                son = son.next
            if father.right != None:
                son.next = father.right
                son = son.next
            father = father.next
        self.connect(head.next)
```

### C++

```cpp
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root == NULL) {
            return;
        }
        TreeLinkNode *head = new TreeLinkNode(0);
        TreeLinkNode *father = root;
        TreeLinkNode *son = head;
        while (father != NULL) {
            if (father->left != NULL) {
                son->next = father->left;
                son = son->next;
            }
            if (father->right != NULL) {
                son->next = father->right;
                son = son->next;
            }
            father = father->next;
        }
        son = head->next;
        delete head;
        connect(son);
    }
};
```