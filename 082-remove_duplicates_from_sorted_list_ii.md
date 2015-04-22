# 082-Remove Duplicates from Sorted List II

## Problem

> Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

> For example,

> Given `1->2->3->3->4->4->5`, return `1->2->5`.

> Given `1->1->1->2->3`, return `2->3`.

## Solution

- 迭代法

    如果下个元素和下下个元素值相同，我们就需要往后删除这些重复元素

    第一个元素也有可能被删除，所以我们还是要搞一个假头节点，方便嘛

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
    ListNode *deleteDuplicates(ListNode *head) {
        ListNode dummy(0);
        dummy.next = head;

        ListNode *cur = &dummy, *post;
        while (cur->next != nullptr && cur->next->next != nullptr) {
            if (cur->next->val == cur->next->next->val) {
                // 往后删除重复元素
                post = cur->next;
                int val = post->val;
                while (post != nullptr && post->val == val) {
                    auto temp = post;
                    post = post->next;
                    temp->next = nullptr;
                    delete temp;
                }
                cur->next = post;
            } else {
                cur = cur->next;
            }
        }

        ListNode *result = dummy.next;
        dummy.next = nullptr;
        return result;
    }
};
```
