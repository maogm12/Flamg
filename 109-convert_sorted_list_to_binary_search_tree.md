# 109-Convert Sorted List to Binary Search Tree

## Problem

> Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

## Solution

- 递归，自顶向下

    找中点，然后递归处理左子树和右子树

    找中点可用快慢指针法，每次找中点要遍历整个链表，一共遍历了 log(n) 遍，所以时间复杂度为 O(nlog n)，空间复杂度只要是递归占用的空间，为 O(log n)

- 递归，自底向上

    先构造左子树，然后我们就到了中间的节点，构建根节点，然后构建右子树，以下时间复杂度降低到了 O(n)!

## Code

### Python

```python

```

### C++

自顶向下

```cpp
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        return buildBST(head, nullptr);
    }
private:
    TreeNode* buildBST(ListNode *start, ListNode *end) {
        if (start == end || !start) {
            return nullptr;
        }

        // 找中点
        ListNode *slow = start, *fast = start;
        while (fast && fast->next && fast != end && fast->next != end) {
            fast = fast->next->next;
            slow = slow->next;
        }

        TreeNode *root = new TreeNode(slow->val);
        root->left = buildBST(start, slow);
        root->right = buildBST(slow->next, end);
        return root;
    }
};
```

自底向上

```cpp
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        int size = 0;  // 先求长度，然后我们可以知道距离头多远是根节点
        ListNode *cur = head;
        while (cur) {
            ++size;
            cur = cur->next;
        }

        cur = head;
        return buildBST(cur, 0, size);
    }
private:
    // head 按引用传递，head可以一直往后移动
    TreeNode* buildBST(ListNode*& head, int begin, int end) {
        if (begin == end) {
            return nullptr;
        }
        int mid = (begin + end) / 2;
        TreeNode *leftTree = buildBST(head, begin, mid);
        TreeNode *root = new TreeNode(head->val);
        root->left= leftTree;
        head = head->next;
        root->right = buildBST(head, mid + 1, end);
        return root;
    }
};
```
