# 146-LRU Cache

## Problem

> Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.

> `get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.

> `set(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

## Solution

- 链表 + 哈希

    首先这个 key-value 结构分分钟想到用哈希，太特喵的应景了，但是关键是这个 LRU 怎么处理，最近最少使用的优先级比较低，
    在 cache 容量用尽时要从 cache 里移除，所以我们可以维护一个容量有限的队列，里面放这些键，某个 cache 一旦被使用，
    就应该移动到前面，如何在常数时间找到这个 cache 呢，就要借助哈希表了，如何在常数时间里面移动这个节点呢？链表！

    情况很明朗，我们使用链表记录 cache，并且用哈希表记录 key 对应的 cache，方便查找

## Code

### Python

```python

```

### C++

```cpp
class LRUCache{
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }

    int get(int key) {
        if (cachePos.find(key) == cachePos.end()) {
            return -1;
        }

        // 移动 cache 到头部，并更新键对应的 cache
        cache.splice(cache.begin(), cache, cachePos[key]);
        cachePos[key] = cache.begin();
        return cache.front().second;
    }

    void set(int key, int value) {
        if (cachePos.find(key) == cachePos.end()) {
            if (cache.size() >= capacity) {
                cachePos.erase(cache.back().first);
                cache.pop_back();
            }
            cache.push_front(make_pair(key, value));
            cachePos[key] = cache.begin();
        } else {
            cachePos[key]->second = value;
            cache.splice(cache.begin(), cache, cachePos[key]);
            cachePos[key] = cache.begin();
        }
    }
private:
    int capacity;
    list<pair<int, int>> cache;
    unordered_map<int, list<pair<int, int>>::iterator> cachePos;
};
```
