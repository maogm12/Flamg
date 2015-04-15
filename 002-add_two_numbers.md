# 002-Add Two Numbers

## Question

> You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
>
> ```
> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
> Output: 7 -> 0 -> 8
> ```


这是大数加法的简化版本，大数加法一般用模拟竖式的方法做，从低位向高位做，所以数字是反向存储的，加的时候注意进位就好。

## Solution

- 循环

	同时遍历两个链表（即从低向高相加的过程），相应的位相加再加上进位的数，得到结果的每一位

- 还有更牛逼的解法么 ==

## Code

### Extra

单链表定义如下：

```python
# python
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
```

```cpp
// cpp
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};
```


### python

```python
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        current = head
        remain = 0
        while l1 is not None or l2 is not None:
            if l1:
                remain += l1.val
                l1 = l1.next
            if l2:
                remain += l2.val
                l2 = l2.next
            
            current.next = ListNode(remain % 10)
            remain /= 10
            current = current.next
            
        # 不要忘了可能剩下的进位哦
        if remain != 0:
            current.next = ListNode(remain)
            
        return head.next
```

### cpp

```cpp
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *head = new ListNode(0),
                 *current = head;
        int remain = 0;
        while (l1 != nullptr || l2 != nullptr) {
            if (l1 != nullptr) {
                remain += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                remain += l2->val;
                l2 = l2->next;
            }

            current->next = new ListNode(remain % 10);
            remain /= 10;
            current = current->next;
        }
        
        // 不要忘了可能剩下的进位哦
        if (remain != 0) {
            current->next = new ListNode(remain);
        }
        
        return head->next;
    }
};
```
