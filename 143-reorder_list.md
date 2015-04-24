# 143-Reorder List

## Problem

> Given a singly linked list L: L0→L1→…→Ln-1→Ln,

> reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

> You must do this in-place without altering the nodes' values.

> For example,

> Given `{1,2,3,4}`, reorder it to `{1,4,2,3}`.

## Solution

- 逆转合并法

    想这个名字都想醉了。。。

    切两半，把后面一半逆转，然后把两个链表合并


> Tips: 链表逆转是个刚需啊！提取出来搞一搞

> - 头插法

>    每次把后面的节点插入到头结点后面，不过需要一个头结点

> - 相邻三个指针法

>    保存相邻的三个指针，前两个逆转用，第三个存放下一个节点用



## Code

### Python

```python

```

### C++

```cpp
class Solution {
public:
    void reorderList(ListNode *head) {
        if (head == nullptr) {
            return;
        }

        int k = 0;
        ListNode *cur = head;
        while (cur != nullptr) {
            ++k;
            cur = cur->next;
        }

        ListNode *prev = nullptr;
        cur = head;
        for (int i = 0; i < (k + 1)/2; ++i) {
            prev = cur;
            cur = cur->next;
        }

        // 头插法逆转
        prev->next = nullptr;
        while (cur != nullptr) {
            ListNode *next = cur->next;
            cur->next = prev->next;
            prev->next = cur;
            cur = next;
        }

        // 合并
        ListNode *rightHalf = prev->next;
        prev->next = nullptr;
        cur = head;
        while (rightHalf != nullptr) {
            ListNode *next = rightHalf->next;
            rightHalf->next = cur->next;
            cur->next = rightHalf;
            cur = rightHalf->next;
            rightHalf = next;
        }
    }
};
```

### Extra

逆转链表

头插法

```cpp
ListNode* reverseList(ListNode *head) {
    ListNode dummy(0);
    dummy.next = head;
    for (ListNode *prev = &dummy, *cur == head;
            cur != nullptr; cur = cur->next) {
        ListNode *next = cur->next;
        cur->next = prev->next;
        prev->next = cur;
        cur = next;
    }

    return dummy.next;
}
```

相邻三个指针法

```cpp
ListNode* reverseList(ListNode *head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }

    ListNode *prev = head;
    for (ListNode *cur = head->next, *next = cur->next; cur != nullptr;
        prev = cur, cur = next, next = cur == nullptr ? nullptr : cur->next) {
        cur->next = prev;
    }

    return prev;
}
```
