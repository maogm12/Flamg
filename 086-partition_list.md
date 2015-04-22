# 086-Partition List

## Problem

> Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

> You should preserve the original relative order of the nodes in each of the two partitions.

> For example,

> Given `1->4->3->2->5->2` and x = 3,

> return `1->2->2->4->3->5`.

把小于某个值的节点移动到前面来

## Solution

- 常规做法

    先找到第一个大于等于指定值的点，然后往后搜索，发现小于指定值的点就
    插入到这个点前面

    上面的例子运算过程为下

    ```
  1->4->3->2->5->2
     ^  找到第一个比3大节点
  1->4->3->2->5->2
     ^     ^  找到比3小的节点
  1->2->4->3->5->2
     ^  ^  插入到4前面
    ```

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
    ListNode *partition(ListNode *head, int x) {
        ListNode dummy(0);
        dummy.next = head;

        ListNode *pivot = &dummy,
                 *cur = pivot->next;
        while (cur != nullptr && cur->val < x) {
            pivot = cur;
            cur = cur->next;
        }

        ListNode *pre = pivot;
        while (cur != nullptr) {
            if (cur->val < x) {
                pre->next = cur->next;
                cur->next = pivot->next;
                pivot->next = cur;
                cur = pre->next;
                pivot = pivot->next;
            } else {
                pre = cur;
                cur = cur->next;
            }
        }

        return dummy.next;
    }
};
```
