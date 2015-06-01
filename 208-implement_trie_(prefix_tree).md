# 208-Implement Trie (Prefix Tree)

## Problem

> Implement a trie with insert, search, and startsWith methods.

## Solution

Trie树实现，我使用字典来存储一个节点的子节点们。

## Code

### Python

```python
class TrieNode:
    # Initialize your data structure here.
    def __init__(self, val):
        self.val = val
        self.next_chs = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode('')

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch in node.next_chs:
                node = node.next_chs[ch]
            else:
                new_node = TrieNode(ch)
                node.next_chs[ch] = new_node
                node = new_node
        if not 'end' in node.next_chs:
            node.next_chs['end'] = TrieNode('end')
    
    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        node = self.root
        for ch in word:
            if not ch in node.next_chs:
                return False
            node = node.next_chs[ch]
        return 'end' in node.next_chs
        

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if not ch in node.next_chs:
                return False
            node = node.next_chs[ch]
        return True
        
```

### C++

```cpp

```