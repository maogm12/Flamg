# 141-Linked List Cycle

## Problem

> Given a linked list, determine if it has a cycle in it.

> Follow up:
> Can you solve it without using extra space?

## Solution

- 哈希

    用哈希记录访问过的节点，如果重新访问到这个节点了，说明有环！！！

    时间复杂度 O(n)，空间复杂度 O(n)

- 快慢指针

    快指针每次跑 2 步，慢指针每次跑 1 步，如果有环，他们肯定会跑到一个环里面，这样的话快指针肯定能追上慢指针，如果追上了说明有环，如果快指针跑到尾部了，说明没有环

    时间复杂度 O(n)，空间复杂度 O(1)

## Code

### Python

```python
class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False

        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True

        return False
```

### C++

```cpp
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if (head == nullptr) {
            return false;
        }

        // 自从用了for，妈妈再也不担心我漏了slow = slow->next了
        for (ListNode *slow = head, *fast = head->next;
                fast != nullptr && fast->next != nullptr;
                slow = slow->next, fast = fast->next->next) {
            if (slow == fast) {
                return true;
            }
        }

        return false;
    }
};
```
