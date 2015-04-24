# 025-Reverse Nodes in k-Group

## Problem

> Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

> If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

> You may not alter the values in the nodes, only nodes itself may be changed.

> Only constant memory is allowed.

> For example,

> Given this linked list: `1->2->3->4->5`

> For `k = 2`, you should return: `2->1->4->3->5`

> For `k = 3`, you should return: `3->2->1->4->5`

## Solution

- 头插法

    逆转链表用头插法，每次把节点插入头节点的后面

    至于具体到本题，我们从头开始，把后面的 k 个节点逆转，如果发现没有 k 个节点就到尾部了，我们就得把刚刚逆转的最后一小段在转回去

    细节很重要，不然分分钟就弄出个环，然后死循环了，多么痛的领悟 TT

## Code

### Python

头插法

```python
# ListNode 定义就不贴了
class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        if head is None or k <= 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        begin = dummy
        end = dummy.next
        while end:
            cur = end.next
            reverse = False
            for i in xrange(1, k):
                if cur:
                    next = cur.next
                    end.next = next
                    cur.next = begin.next
                    begin.next = cur
                    cur = next
                else:
                    reverse = True
                    break

            if reverse:
                cur = begin.next
                begin.next = None
                while cur:
                    next = cur.next
                    cur.next = begin.next
                    begin.next = cur
                    cur = next
                break
            else:
                begin = end
                end = begin.next

        return dummy.next
```

### C++

头插法

```cpp
// 链表定义就不贴了
class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (head == nullptr || k <= 1) {
            return head;
        }

        ListNode dummy(0);
        dummy.next = head;

        ListNode *begin = &dummy,
                 *end = begin->next,
                 *cur = nullptr,
                 *next = nullptr;
        while (end != nullptr) {
            cur = end->next;
            bool reverse = false;
            for (int i = 1; i < k; ++i) {
                if (cur != nullptr) {
                    next = cur->next;
                    end->next = next;
                    cur->next = begin->next;
                    begin->next = cur;
                    cur = next;
                } else {
                    reverse = true;
                    break;
                }
            }

            // 需要反转
            if (reverse) {
                cur = begin->next;
                begin->next = nullptr;
                while (cur != nullptr) {
                    next = cur->next;
                    cur->next = begin->next;
                    begin->next = cur;
                    cur = next;
                }
                break;
            } else {
                begin = end;
                end = begin->next;
            }
        }

        ListNode *result = dummy.next;
        dummy.next = nullptr;
        return result;
    }
};
```
