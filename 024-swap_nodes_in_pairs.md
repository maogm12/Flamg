# 024-Swap Nodes in Pairs

## Problem

> Given a linked list, swap every two adjacent nodes and return its head.

> For example,

> Given `1->2->3->4`, you should return the list as `2->1->4->3`.

> Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

## Solution

- 迭代法

    对某个节点，如果要交换后面两个节点，先把当前节点指向下下个节点。然后把下个节点，指向下下下个节点，然后把下下个节点指回下个节点。

    关键是小心别指错了，时间复杂度 O(n)，空间复杂度为 O(1)

## Code

### Python

```python

```

### C++

迭代法
```cpp
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode dummy(0);
        dummy.next = head;

        ListNode *cur = &dummy;
        while (cur != nullptr) {
            if (cur->next != nullptr && cur->next->next != nullptr) {
                ListNode *next = cur->next;
                cur->next = next->next;
                next->next = next->next->next;
                cur->next->next = next;
                cur = next;
            } else {
                break;
            }
        }

        ListNode *result = dummy.next;
        dummy.next = nullptr;
        return result;
    }
};
```
