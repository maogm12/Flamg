# 023-Merge k Sorted Lists

## Problem

> Merge <i>k</i> sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

## Solution

- 穿针引线法

    每次遍历 k 个 list，找出最小值，接到结果后面

    时间复杂度为 O(kn)，n 为平均长度，会超时 =.=

- 一个一个 merge 法（什么鬼）

    利用 merge 2 lists 的算法，从头到尾，一个一个 merge

## Code

### Python

```python

```

### C++

穿针引线法

```cpp
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode dummy(0);
		ListNode *cur = &dummy;
		int minIndex = findMin(lists);
		while (minIndex != -1) {
			cur->next = lists[minIndex];
			cur = cur->next;
			lists[minIndex] = lists[minIndex]->next;
			minIndex = findMin(lists);
		}
		return dummy.next;
    }

private:
	int findMin(vector<ListNode*>& lists) {
		ListNode *minNode = nullptr;
		int minIndex = -1;
		for (int i = 0; i < lists.size(); ++i) {
			if (lists[i] == nullptr) continue;
			if (!minNode || minNode->val > lists[i]->val) {
				minNode = lists[i];
				minIndex = i;
			}
		}
		return minIndex;
	}
};
```

一个一个 merge 法

```cpp
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if (lists.empty()) return nullptr;

        ListNode *p = lists[0];
        for (int i = 1; i < lists.size(); ++i) {
            p = merge2Lists(lists[i], p);
        }
        return p;
    }

private:
	ListNode* merge2Lists(ListNode *lh, ListNode *rh) {
		ListNode dummy(0), *cur = &dummy;
		while (lh && rh) {
		    if (lh->val > rh->val) {
		        cur->next = rh;
		        rh = rh->next;
		    } else {
		        cur->next = lh;
		        lh = lh->next;
		    }
		    cur = cur->next;
		}
		cur->next = lh ? lh : rh;
		return dummy.next;
	}
};
```
