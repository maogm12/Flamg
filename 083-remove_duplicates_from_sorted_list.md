# 083-Remove Duplicates from Sorted List

## Problem

> Given a sorted linked list, delete all duplicates such that each element appear only once.

> For example,

> Given `1->1->2`, return `1->2`.

> Given `1->1->2->3->3`, return `1->2->3`.

## Solution

- 往后搜索法

    往后搜索，发现与当前节点相同就继续，不同则把那个节点接到当前节点后面

    时间复杂度 O(n)，空间复杂度 O(1)


## Code

### Python

```python
# hello world
```

### C++

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        if (head == nullptr) {
            return head;
        }

        ListNode *cur = head,
                 *post = cur->next;
        while (post != nullptr) {
            // 只接不同的元素，貌似内存泄露了 ->_->
            if (cur->val != post->val) {
                cur->next = post;
                cur = cur->next;
            }

            // 解决内存泄露
            // auto pre = post;
            post = post->next;
            // pre->next = nullptr;
            // delete pre;
        }
        cur->next = nullptr;
        return head;
    }
};
```
