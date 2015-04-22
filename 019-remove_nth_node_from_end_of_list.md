# 019-Remove Nth Node From End of List

## Problem

> Given a linked list, remove the nth node from the end of list and return its head.

> For example,

> ```
> Given linked list: 1->2->3->4->5, and n = 2.

> After removing the second node from the end, the linked list becomes 1->2->3->5.
> ```

> **Note:**

> Given n will always be valid.

> Try to do this in one pass.

删除链表的倒数第 n 个元素

## Solution

- 快慢指针法

    使用一个快指针，比慢指针先 n 步，然后同时移动，这样快指针到达尾部，
    慢指针就是倒数第 n 个结点，一遍完成

    时间复杂度 O(n)，空间复杂读 O(1)

- 计算长度法

    先循环一遍计算链表长度，然后从头少走 n 步，得到倒数第 n 个元素

    时间复杂度 O(n)，空间复杂读 O(1)

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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // 第一个元素也可能被删除，使用假头结点
        ListNode dummy(0);
        dummy.next = head;

        ListNode *slow = &dummy, *fast = &dummy;
        while (n--) {
            fast = fast->next;
            if (fast == nullptr) {
                return head;
            }
        }

        while (fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next;
        }

        if (slow->next != nullptr) {
            ListNode *temp = slow->next;
            slow->next = temp->next;
            temp->next = nullptr;
            delete temp;
        }

        ListNode *result = dummy.next;
        dummy.next = nullptr;
        return result;
    }
};
```
