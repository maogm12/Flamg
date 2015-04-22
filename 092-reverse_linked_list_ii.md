# 092-Reverse Linked List II

## Problem

> Reverse a linked list from position m to n. Do it in-place and in one-pass.

> For example:

> Given `1->2->3->4->5->NULL`, m = 2 and n = 4,

> return `1->4->3->2->5->NULL`.

> Note:

> Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

反转链表的一部分

## Solution

- 常规做法

    反转链表关键是不要把指针指错了

    因为是反转一部分，我们先要保存左边不动部分的尾部，然后反转中间那段，
    保存新的头尾，然后重新接上左边和右边

    可以第一个也可能在反转的范围里，所以我们可以给链表加个头，方便处理

## Code

### Python

```python

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
    ListNode *reverseBetween(ListNode *head, int m, int n) {
        if (m == n) {
            return head;
        }

        // 加一个假的头
        ListNode *dummy = new ListNode(0);
        dummy->next = head;
        ListNode *leftTail = nullptr,  // 左边的尾部
                 *cur = dummy;
        for (int i = 0; i < m; ++i) {
            leftTail = cur;
            cur = cur->next;
        }

        ListNode *reverseTail = cur, // 反转后的尾部
                 *pre = nullptr;

        // 反转
        for (int i = m; i <= n; ++i) {
            auto next = cur->next;
            cur->next = pre;
            pre = cur;
            cur = next;
        }

        // 重新接起来
        leftTail->next = pre;
        reverseTail->next = cur;

        auto result = dummy->next;
        dummy->next = nullptr;
        delete dummy;
        return result;
    }
};
```
