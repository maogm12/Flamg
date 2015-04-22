# 061-Rotate List

## Problem

> Given a list, rotate the list to the right by k places, where k is non-negative.

> For example:

> Given `1->2->3->4->5->NULL` and k = 2,

> return `4->5->1->2->3->NULL`.

## Solution

- 切分法

    把链表切成两节，然后换过来连起来就好了。边界条件超级多。。。

    注意这个 k 可能超级大，所以要先算长度，求个模

- 切圈圈法

    把链表头尾相接连成圈圈，然后走 `size - k － 1` 步后切圈圈

## Code

### Python

```python

```

### C++

切圈圈法

```c
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
    ListNode* rotateRight(ListNode* head, int k) {
        if (head == nullptr) {
            return head;
        }

        ListNode *cur = head;
        int size = 1;
        while (cur->next != nullptr) {
            cur = cur->next;
            ++size;
        }
        cur->next = head;  // 结成环
        k %= size;

        cur = head;
        k = size - k - 1;
        while (k--) {
            cur = cur->next;
        }

        ListNode *result = cur->next;
        cur->next = nullptr;
        return result;
    }
};
```
