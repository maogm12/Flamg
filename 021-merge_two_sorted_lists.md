# 021-Merge Two Sorted Lists

## Problem

> Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

## Solution

同时扫描两个 list，那个小就接到 result 后面

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        auto p1 = l1, p2 = l2, cur = &dummy;
        while (p1 && p2) {
            if (p1->val < p2->val) {
                cur->next = p1;
                p1 = p1->next;
            } else {
                cur->next = p2;
                p2 = p2->next;
            }
            cur = cur->next;
        }

        if (p1) cur->next = p1;
        if (p2) cur->next = p2;
        return dummy.next;
    }
};
```
