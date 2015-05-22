# 160-Intersection of Two Linked Lists

## Problem

> Write a program to find the node at which the intersection of two singly linked lists begins.


> For example, the following two linked lists:
> 
```
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
```
begin to intersect at node c1.


> **Notes**:
> 
- If the two linked lists have no intersection at all, return null.
- The linked lists must retain their original structure after the function returns.
- You may assume there are no cycles anywhere in the entire linked structure.
- Your code should preferably run in O(n) time and use only O(1) memory.

## Solution

- 求取两个链表的长度，
- 较长的链表先走一些，先走的步数为长度的差额
- 两个链表同时走，当当前节点相同时，返回。

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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if (headA == NULL || headB == NULL) {
            return NULL;
        }
        int lengthA = get_length(headA);
        int lengthB = get_length(headB);
        if (lengthA >= lengthB) {
            for (int i = 0; i < lengthA - lengthB; i++) {
                headA = headA->next;
            }
        } else {
            for (int i = 0; i < lengthB - lengthA; i++) {
                headB = headB->next;
            }
        }
        while (headA != headB) {
            headA = headA->next;
            headB = headB->next;
        }
        return headA;
        
    }
    int get_length(ListNode *headA) {
        int length = 0;
        while (headA != NULL) {
            headA = headA->next;
            length++;
        }
        return length;
    }
};
```