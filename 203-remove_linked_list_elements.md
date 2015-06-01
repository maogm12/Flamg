# 203-Remove Linked List Elements

## Problem

> Remove all elements from a linked list of integers that have value val.

> Example
> Given: `1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6`, val = 6
> 
> Return: `1 --> 2 --> 3 --> 4 --> 5`

## Solution

保存上一个节点，如果当前节点等于目标值，即删除。

## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        ListNode dummy(-1);
        dummy.next = head;
        ListNode *prev = &dummy, *cur = head;
        while (cur) {
            if (cur->val == val) {
                prev->next = cur->next;
                free(cur);
                cur = prev->next;
            } else {
                prev = cur;
                cur = cur->next;
            }
        }
        return dummy.next;
        
    }
};
```