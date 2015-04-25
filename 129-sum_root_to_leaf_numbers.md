# 129-Sum Root to Leaf Numbers

## Problem

> Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

> An example is the root-to-leaf path 1->2->3 which represents the number 123.

> Find the total sum of all root-to-leaf numbers.

> For example,
>
```
    1
   / \
  2   3
```

> The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

> Return the sum = 12 + 13 = 25.

## Solution

- 递归，当到达叶子节点时，将结果加到最终结果中。

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.result = 0
        self.sum_num(root, 0)
        return self.result
    
    def sum_num(self, node, current_sum):
        if node == None:
            return
        current_sum = current_sum * 10 + node.val
        if (node.left == None and node.right == None):
            self.result += current_sum
            return
        self.sum_num(node.left, current_sum)
        self.sum_num(node.right, current_sum)
```

### C++

```cpp
class Solution {
public:
    int sumNumbers(TreeNode *root) {
        result = 0;
        sum_num(root, 0);
        return result;
    }
    void sum_num(TreeNode *node, int current_sum) {
        if (node == NULL) {
            return;
        }
        current_sum = current_sum * 10 + node->val;
        if (node->left == NULL && node->right == NULL) {
            result += current_sum;
            return;
        }
        sum_num(node->left,  current_sum);
        sum_num(node->right, current_sum);
    }
private:
    int result;
};
```