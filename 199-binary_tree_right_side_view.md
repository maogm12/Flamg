# 199-Binary Tree Right Side View

## Problem

> Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

> For example:
Given the following binary tree,
>
```
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
```
You should return `[1, 3, 4]`.

## Solution

- 层次遍历，但右子节点比左子结点先入队列，对每一层次，只加最开始的那个节点

## Code

### Python

```python
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        if root == None:
            return []
        queue = [root]
        result = []
        
        begin = 0
        end = 1
        is_find = False
        while begin < end:
            node = queue[begin]
            if not is_find:
                result.append(node.val)
                is_find = True
            if node.right != None:
                queue.append(node.right)
            if node.left != None:
                queue.append(node.left)
            if begin == end - 1:
                end = len(queue)
                is_find = False
            begin += 1
        
        return result
```

### C++

```cpp

```