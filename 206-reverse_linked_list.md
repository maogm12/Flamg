# 206-Reverse Linked List

## Problem

> Reverse a singly linked list.

## Solution

反转链表，链表题目之必备技能。

## Code

### Python

```python

```

### C++

```cpp

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL) {
            return head;
        }
        ListNode *pre, *cur, *next;
        for (pre = head, cur = head->next, next = cur->next; cur != NULL; pre = cur, cur = next, next = cur ? cur->next: NULL) {
            cur->next = pre;
        }
        head->next = NULL;
        return pre;
        
    }
};
```