# 148-Sort List

## Problem

> Sort a linked list in O(n log n) time using constant space complexity.

## Solution

排序链表，这是一个单链表，又要O(nlogn)的时间复杂度，所以使用选择排序

1. 把链表分成两半
2. 递归地对两边排序
3. merge

使用快慢指针找中点，每次需要O(n)的时间，每次分成两个子问题

T(n) = 2T(n/2) + o(n)

嗯，由主定理可知，时间复杂度为 O(nlogn)

## Code

### Python

```python

```

### C++

```cpp
ListNode* sortList(ListNode* head) {
    if (head == nullptr || head->next == nullptr) return head;
    auto slow = head, fast = head->next;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    auto latter = sortList(slow->next);
    slow->next = nullptr;
    auto former = sortList(head);
    return mergeSort(former, latter);
}

ListNode* mergeSort(ListNode* lh, ListNode* rh) {
    if (lh == nullptr) return rh;
    if (rh == nullptr) return lh;
    ListNode dummy(0);
    auto lp = lh, rp = rh, cur = &dummy;
    while (lp != nullptr && rp != nullptr) {
        if (lp->val < rp->val) {
            cur->next = lp;
            lp = lp->next;
        } else {
            cur->next = rp;
            rp = rp->next;
        }
        cur = cur->next;
    }
    if (lp) cur->next = lp;
    if (rp) cur->next = rp;
    return dummy.next;
}
```
