# 113-Path Sum II

## Problem

> Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

> For example:
Given the below binary tree and sum = 22,
>
```
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
```
return
>
```
[
   [5,4,11,2],
   [5,8,4,5]
]
```

## Solution

- 递归，相当于先序遍历，当遍历到当前节点时，将根节点到当前节点的路径和以及路径值都保存下来，传递给子节点。当到达叶子节点时，判断是否与sum相等。

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        self.results = []
        self.sub_path(root, sum, 0, [])
        return self.results
    
    def sub_path(self, node, sum, current_sum, result):
        if node == None:
            return
        current_sum += node.val
        result.append(node.val)
        if node.left == None and node.right == None:
            if current_sum == sum:
                new_result = [v for v in result]
                self.results.append(new_result)
        self.sub_path(node.left,  sum, current_sum, result)
        self.sub_path(node.right, sum, current_sum, result)
        result.pop()
```

### C++

```cpp
class Solution {
public:
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        vector<int> result;
        results.clear();
        sub_path_sum(root, sum, 0, result);
        return results;
    }
    
    void sub_path_sum(TreeNode *node, int sum, int current_sum, vector<int> &result) {
        if (node == NULL) {
            return;
        }
        current_sum += node->val;
        result.push_back(node->val);
        if (node->left == NULL && node->right == NULL) {
            if (current_sum == sum) {
                results.push_back(result);
            }
        }
        sub_path_sum(node->left, sum, current_sum, result);
        sub_path_sum(node->right, sum, current_sum, result);
        result.pop_back();
    }
private:
    vector<vector<int> > results;
};
```