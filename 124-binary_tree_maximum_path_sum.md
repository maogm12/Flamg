# 124-Binary_Tree_Maximum_Path_Sum

## Question

> Given a binary tree, find the maximum path sum.

> The path may start and end at any node in the tree.

> For example:
> Given the below binary tree,
> 
       1
      / \
     2   3
> Return 6.


## Solution

此题是要找出树中任何两个节点之间的路径和中的最大者。

### 第一轮分析

对于两个节点间的路径，必然要经过它们的最近公共父节点。也就是说，对每个节点node。

- 找到其左子树上到该节点的最大和路径，left_path_sum
- 找到其右子树上到该节点的最大和路径，right_path_sum
- 那么，经过节点node的的最大和路径为以下四个值的最大值。
	- left_path_sum + node.val, 
	- right_path_sum + node.val, 
	- left_path_sum + node.val + right_path_sum,
	- node.val

那么，依照此方式遍历所有的节点后，就可以找到最大和路径了。

### 第二轮分析

先放一个多层的树在下边。

>

```
     1
    /  \
  2      3
 / \    / \
4   5  6   7
```

对于第一轮分析中的left_path_sum和right_path_sum的计算，其技巧在于低层次的left_path_sum和right_path_sum是高层次的left_path_sum和right_path_sum的计算的一部分。

比如对于值为2的节点，其left_path_sum=4, right_path_sum=5,那么对于值为1的节点，其left_path_sum就等于如下三个值的最大值：

- left_path_sum_of_node2 + val_of_node2
- right_path_sum_of_node2 + val_of_node2
- val_of_node2

因而是7。

而由低层次到高层次的计算方法恰好就是递归所能完成的，所以本题的解法是递归方法。

## Code

### python

```python
class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root == None:
            return 0
        self.max_sum = root.val
        self.max_path(root)
        return self.max_sum
    
    def max_path(self, node):
        if node == None:
            return 0
        left_path_sum  = self.max_path(node.left)
        right_path_sum = self.max_path(node.right)
        max_tmp = node.val
        if left_path_sum > 0:
            max_tmp += left_path_sum
        if right_path_sum > 0:
            max_tmp += right_path_sum
        if max_tmp > self.max_sum:
            self.max_sum = max_tmp
        return max(node.val, node.val + left_path_sum, node.val + right_path_sum)
```

### cpp

```cpp
class Solution {
public:
    int maxPathSum(TreeNode *root) {
        if (root == NULL) {
            return 0;
        }
        max_sum = root->val;
        max_path_sum(root);
        return max_sum;
    }
    
    int max_path_sum(TreeNode *node) {
        if (node == NULL) {
            return 0;
        }
        int left_path_sum  = max_path_sum(node->left);
        int right_path_sum = max_path_sum(node->right);
        int path1 = left_path_sum  + node->val;
        int path2 = right_path_sum + node->val;
        int path3 = left_path_sum + right_path_sum + node->val;
        int path4 = node->val;
        int max_tmp = max(max(max(path1, path2), path3), path4);
        if (max_tmp > max_sum) {
            max_sum = max_tmp;
        }
        return max(max(path1, path2), path4);
    }
private:
    int max_sum;
};
```


