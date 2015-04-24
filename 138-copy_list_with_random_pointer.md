# 138-Copy List with Random Pointer

## Problem

> A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

> Return a deep copy of the list.


## Solution

- 哈希法

    复制链表简单，关键是这个 `random` 指针的处理，我们可以用哈希表记录新旧节点的对应关系，然后根据这个查出新的链表里面 `random` 应该是哪个

    要扫描两遍，一遍复制，一遍重建 `random` 指针的值，时间复杂度 O(n)，空间复杂度 O(n)

- 复制节点法

    先把每个节点都复制一个，插入后面，然后新节点的 `random` 值就是他上一个节点（就是旧节点）的 `random` 的下一个，精妙啊！！！然后把新加的节点拿出来串成串即可。

    这样空间复杂度为 O(1)，时间复杂度依然是 O(n)，扫描了三遍

## Code

### Python

NB闪闪的复制节点法

```python
# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # duplicate nodes
        cur = head
        while cur:
            node = RandomListNode(cur.label)
            node.next = cur.next
            cur.next = node
            cur = cur.next.next

        # rebuild the random pointer
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # take out new nodes and link them up
        dummy = RandomListNode(0)
        cur = head
        pick = dummy
        while cur:
            pick.next = cur.next
            pick = pick.next
            cur.next = pick.next
            cur = cur.next

        return dummy.next
```

### C++

哈希法

```cpp
/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        unordered_map<RandomListNode*, RandomListNode*> old2new;
        RandomListNode dummy(0);
        RandomListNode *cur = head, *newPrev = &dummy;
        while (cur != nullptr) {
            newPrev->next = new RandomListNode(cur->label);
            newPrev = newPrev->next;
            old2new[cur] = newPrev;
            cur = cur->next;
        }

        cur = head;
        while (cur != nullptr) {
            if (cur->random != nullptr) {
                old2new[cur]->random = old2new[cur->random];
            }

            // 这句话老是忘。。。看来得多用用for了
            cur = cur->next;
        }

        ListNode *result = dummy.next;
        dummy.next = nullptr;
        return result;
    }
};
```

哈希法 Anti-while 版，看起来整洁一点呢

```cpp
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        unordered_map<RandomListNode*, RandomListNode*> old2new;
        RandomListNode dummy(0);

        for (RandomListNode *cur = head, *newPrev = &dummy;
            cur != nullptr;
            cur = cur->next) {
            newPrev->next = new RandomListNode(cur->label);
            newPrev = newPrev->next;
            old2new[cur] = newPrev;
        }

        for (RandomListNode *cur = head; cur != nullptr; cur = cur->next) {
            if (cur->random != nullptr) {
                old2new[cur]->random = old2new[cur->random];
            }
        }

        return dummy.next;
    }
};
```

复制节点法

```cpp
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        for (RandomListNode *cur = head; cur != nullptr;) {
            RandomListNode *duplicate = new RandomListNode(cur->label);
            duplicate->next = cur->next;
            cur->next = duplicate;
            cur = duplicate->next;
        }

        for (RandomListNode *cur = head; cur != nullptr;) {
            if (cur->random != nullptr) {
                cur->next->random = cur->random->next;
            }
            cur = cur->next->next;
        }

        RandomListNode dummy(0);
        for (RandomListNode *cur = head, *pick = &dummy; cur != nullptr;) {
            pick->next = cur->next;
            pick = pick->next;
            cur->next = pick->next;
            cur = cur->next;
        }

        return dummy.next;
    }
};
```
