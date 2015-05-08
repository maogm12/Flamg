# 102-Binary Tree Level Order Traversal

## Problem

> Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

> For example:
Given binary tree `{3,9,20,#,#,15,7}`,

>
```
    3
   / \
  9  20
    /  \
   15   7
```
return its level order traversal as:
>
```
[
  [3],
  [9,20],
  [15,7]
]
```

## Solution

使用队列类似的数据结构进行BFS，即访问当前节点时，将其左右子节点加到队列的末尾。

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
		if root == None:
			return []
		results = []
		queue = [root]
		begin = 0
		end   = 1
		result = []
		while begin < end:
			node = queue[begin]
			if node.left != None:
				queue.append(node.left)
			if node.right != None:
				queue.append(node.right)
			result.append(node.val)
			if begin == end - 1:
				results.append(result)
				result = []
				end = len(queue)
			begin += 1
		return results
```

### C++

```cpp
class Solution {
public:
    vector<vector<int> > levelOrder(TreeNode *root) {
        vector<vector<int> > results;
        vector<int> result;

        if (root == NULL) {
            return results;
        }

        vector<TreeNode *> levels;
        levels.push_back(root);

        int begin = 0, end = 1;
        TreeNode *node = NULL;

        while (begin < end) {
            node = levels[begin];
            result.push_back(node->val);
            if (node->left != NULL) {
                levels.push_back(node->left);
            }
            if (node->right != NULL) {
                levels.push_back(node->right);
            }
            if (begin == end - 1) {
                results.push_back(result);
                result.clear();
                end = levels.size();
            }
            begin++;
        }

        return results;
    }
};
```

keke, I am the speaker mgm, 照旧，我就只能稍微改改祥爷的代码来凑数了

这里我们可以直接使用 `std::queue`,可以简洁一点点

```cpp
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> result;
        queue<TreeNode*> current;
        if (root != nullptr) {
            current.push(root);
        }

        TreeNode *node = nullptr; // 当前访问的节点
        while (!current.empty()) {
            auto size = current.size();
            vector<int> level;
            level.reserve(size);
            while (size-- > 0) {
                node = current.front(); current.pop();
                level.push_back(node->val);
                if (node->left != nullptr) {
                    current.push(node->left);
                }
                if (node->right != nullptr) {
                    current.push(node->right);
                }
            }
            result.push_back(level);
        }

        return result;
    }
};
```
