# 142-Linked List Cycle II

## Problem

> Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

> Follow up:

> Can you solve it without using extra space?

## Solution

- 哈希法

    用哈希表记录访问过的节点，分分钟可破之

    总共有 n 个节点的话，时间复杂度 O(n)，空间复杂度 O(n)

- 快慢指针法

    我们先来看一个示意图，我们看到里面有个环哈

    ```
  a - n - b - n - c
          |       |
          o - m - o
    ```

    其中 `a - b` 是环外部分，长度为 `n`，`b - c` 长度为 `n`，`c - b` 的长度为 `m`

    我们用一个慢指针，一个快指针，慢指针每次跑一步，快指针每次跑两步。慢指针到达 `b` 节点的时候，快指针应该跑到了 `c` 节点处。`c` 到 `b` 还有 `m` 的路要走（也就是离慢指针还有这么远），每次快指针只能追上一步，所以要走 `m` 步才能遇到慢指针

    你有木有发现这个环只有 `m + n` 长，慢指针走了 `m` 步的话，离 `b` 就只差 `n` 步了有木有。同时头结点和 `b` 也只差 `n` 步，我们另外搞一个指针从头部同时跑，最后和慢指针回合的地方就是 `b` 节点了

## Code

### Python

快慢指针法

```python
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                node = head
                while node is not slow:
                    node = node.next
                    slow = slow.next
                return node

        return None
```

### C++

哈希法，代码超级简介哈

```cpp
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        unordered_set<ListNode*> visited;

        for (ListNode *cur = head; cur != nullptr; cur = cur->next) {
            if (visited.find(cur) != visited.end()) {
                return cur;
            } else {
                visited.insert(cur);
            }
        }

        return nullptr;
    }
};
```

快慢指针法

```cpp
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head, *fast = head;
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
            if (slow == fast) {
                ListNode *node = head;
                while (slow != node) {
                    slow = slow->next;
                    node = node->next;
                }
                return node;
            }
        }

        return nullptr;
    }
};
```
