# 094-Binary Tree Inorder Traversal

## Problem

> Given a binary tree, return the inorder traversal of its nodes' values.

> For example:
Given binary tree {1,#,2,3},
>
```
   1
    \
     2
    /
   3
```
return [1,3,2].

> Note: Recursive solution is trivial, could you do it iteratively?

## Solution

- 栈法

	非递归遍历：中序遍历的顺序是

	- 访问左子树
	- 访问当前节点
	- 访问右子树

  所以，在访问某个节点的时候，需要保证其左子树已被访问，然后如果其有右子树，访问其右子树。

	使用栈来非递归的解决中序遍历，具体操作如下：
	1. 当前节点一路向左走全都压入栈中，直至左子结点为NULL(这样保证栈中元素弹出被访问的时候，其左子树都被访问)
	2. 从栈中弹出节点node，访问它
	3. 如果node有右子节点，那么从右子节点开始，再一路向左走，所遇节点全都压入栈中。(如果有右子树，访问其右子树)

- Morris 中序遍历

    Morris 遍历是一种利用了 [Threaded Binary Tree](http://en.wikipedia.org/wiki/Threaded_binary_tree) 的遍历方法，该算法遍历二叉树可以做得到 O(1) 的空间复杂度，同时还有 O(n) 的时间复杂度

    其实中序遍历关键是遍历完子树后回到根节点，传统的方法是用栈也是为了把根节点留着，等子树遍历完后可以从栈里面直接娶到父节点。

    Morris 遍历利用了节点没利用的 right 指针指向中序遍历的后驱节点（其实就是遍历完子树后回到了根节点），这样就可以避免额外的空间。那么怎么找到某一个根节点的前驱结点呢？很简单，在中序便利里面，根节点的前驱结点一定是左子树最右边的节点，想明白没？没想明白画图慢慢琢磨。

    还有一点很关键就是要把这些多加进去的关系删掉，让树恢复成原来的结构。在 Morris 里面回到根节点后会再找一遍前驱结点，算法和原来一样，这次是要把前驱结点的 right 置空

    Morris 算法流程为：

    1. 当前节点的左孩子为空，那么我们可以访问当前节点，并将当前节点置为右孩子
	2. 当前节点的左孩子不为空
		- 找前驱结点（左子树的最右边那个节点）
		- 若前驱结点的右孩子为空，那么就指向当前节点，我们可以从左子树继续遍历
		- 若前驱结点的右孩子指向了当前节点，这是恢复树结构的过程了，将其置空。然后左边访问完毕了，我们继续从右子树继续遍历

## Code

### Python

```python
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        stack  = []
        result = []
        node = root
        while node != None:
            stack.append(node)
            node = node.left
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)
            node = node.right
            while node != None:
                stack.append(node)
                node = node.left
        return result
```

### C++

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        vector<TreeNode *> stack;
        vector<int> result;
        TreeNode *node = root;
        while (node != NULL) {
            stack.push_back(node);
            node = node->left;
        }
        while (stack.size() != 0) {
            node = stack.back();
            stack.pop_back();
            result.push_back(node->val);
            node = node->right;
            while (node != NULL) {
                stack.push_back(node);
                node = node->left;
            }
        }
        return result;
    }
};
```

## Code Challenge of MGM

祥爷的代码十分精妙，无法改进 TT，唯一能做的就是改用 `std::stack` 了

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;

        stack<TreeNode*> s;
        TreeNode *node = root;
        while (node != nullptr) {
            s.push(node);
            node = node->left;
        }

        while (!s.empty()) {
            node = s.top(); s.pop();
            result.push_back(node->val);

            node = node->right;
            while (node != nullptr) {
                s.push(node);
                node = node->left;
            }
        }

        return result;
    }
};
```

我是发言者mgm，厚颜无耻的来贴递归代码了

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        if (root == nullptr) {
            return result;
        }

        auto leftVec = inorderTraversal(root->left);
        auto rightVec = inorderTraversal(root->right);
        result.insert(result.end(), leftVec.begin(), leftVec.end());
        result.push_back(root->val);
        result.insert(result.end(), rightVec.begin(), rightVec.end());
        return result;
    }
};
```

我是发言者 mgm，贴上 Morris 中序遍历法，代码还是挺短的

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> result;
        TreeNode *cur = root, *pre = nullptr;
        while (cur) {
            if (cur->left == nullptr) {
                result.push_back(cur->val);
                cur = cur->right;
            } else {
                pre = cur->left;
                while (pre->right != nullptr && pre->right != cur) {
                    pre = pre->right;
                }

                if (pre->right == nullptr) {
                    pre->right = cur;
                    cur = cur->left;
                } else { // 恢复树结构
                    pre->right = nullptr;
                    result.push_back(cur->val);
                    cur = cur->right;
                }
            }
        }
        return result;
    }
};
```

## Code Re-Challenge of ZYX

毛神的递归感觉用到会用到好多vector的临时变量。下面的代码长度差不多，赶脚更具可读性，当然，我也是在更加无耻的贴递归代码

```cpp
class Solution {
public:
    vector<int> inorderTraversal(TreeNode *root) {
        result.clear();
        inorder(root);
        return result;
    }
    
    void inorder(TreeNode *node) {
        if (node == NULL) {
            return;
        }
        inorder(node->left);
        result.push_back(node->val);
        inorder(node->right);
    }
private:
    vector<int> result;
};
```

