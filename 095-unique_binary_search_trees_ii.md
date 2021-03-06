# 095-Unique Binary Search Trees II

## Problem

> Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

> For example,
Given n = 3, your program should return all 5 unique BST's shown below.
>
```
   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

## Solution

- 递归：该问题很容易就能想出其递归表达，对于n个数，首先选择一个作为根节点，比如i，然后在1,...,i-1 上构建左子树， 在i+1,...,n上构建右子树，当然，左子树可能不止一颗，右子树也可能不止一颗，将所有左右子树的组合都连接到根节点上，就得到了该根节点所对应的所有的树。

> 旁白先生：又是递归，为毛树上多用递归？
> 
> 我：因为两点：1、树具有深层结构；2、树的左右子树都与原来的树结构相似。


## Code

### Python

```python
class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.generate(1, n)
        
    def generate(self, begin, end):
        nodes = []
        if begin > end:
            nodes.append(None)
        else:
            for i in range(begin, end+1):
                left_nodes = self.generate(begin, i-1)
                right_nodes = self.generate(i+1, end)
                for l_node in left_nodes:
                    for r_node in right_nodes:
                        node = TreeNode(i)
                        node.left = l_node
                        node.right = r_node
                        nodes.append(node)
        return nodes
```

### C++

```cpp
class Solution {
public:
    vector<TreeNode *> generateTrees(int n) {
        return generate(1, n);
    }
    vector<TreeNode *> generate(int begin, int end) {
        vector<TreeNode *> nodes;
        if (begin > end) {
            nodes.push_back(NULL);
        } else {
            for (int i = begin; i <= end; i++) {
                vector<TreeNode *> left_nodes = generate(begin, i-1);
                vector<TreeNode *> right_nodes = generate(i+1, end);
                for (auto left_it : left_nodes) {
                    for (auto right_it : right_nodes) {
                        TreeNode *node = new TreeNode(i);
                        node->left = left_it;
                        node->right = right_it;
                        nodes.push_back(node);
                    }
                }
            }
        }
        return nodes;
    }
};
```