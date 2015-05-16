# 147-Insertion Sort List

## Problem

> Sort a linked list using insertion sort.

## Solution

插入排序

    每次将一个节点插入前面有序的链表里面，关键是找插入位置

## Code

### Python

```python
# blahblah
```

### C++

插入排序

```cpp
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        if (head == nullptr) {
            return head;
        }

        ListNode dummy(0);
        dummy.next = head;
        auto divider = dummy.next->next;
        head->next = nullptr;
        while (divider) {
            auto toInsert = divider;
            divider = divider->next;

            // find the place to insert node
            auto cur = dummy.next, pre = &dummy;
            while (cur && cur->val < toInsert->val) {
                pre = cur;
                cur = cur->next;
            }
            toInsert->next = cur;
            pre->next = toInsert;
        }
        return dummy.next;
    }
};
```

选择排序版。。。我是来砸场的 hiahia

每次选最小的数接到有序链表后面

```cpp
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        ListNode dummy(0), *result = &dummy;;
        ListNode newHead(0); newHead.next = head;
        while (newHead.next != nullptr) {
            ListNode *minPre = &newHead, *minNode = newHead.next;
            for (ListNode *cur = newHead.next, *pre = &newHead;
                    cur != nullptr;
                    pre = cur, cur = cur->next) {
                if (cur->val < minNode->val) {
                    minPre = pre;
                    minNode = cur;
                }
            }
            minPre->next = minNode->next;
            result->next = minNode;
            result = result->next;
        }
        return dummy.next;
    }
};
```
