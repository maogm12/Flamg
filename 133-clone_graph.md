# 133-Clone Graph

## Problem

> Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

> OJ's undirected graph serialization:
Nodes are labeled uniquely.

> We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

> The graph has a total of three nodes, and therefore contains three parts as separated by #.

> First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
> Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:
>
       1
      / \
     /   \
    0 --- 2
         / \
         \_/

## Solution

- 使用哈希表来保存新节点和旧节点的对应关系，然后neighbor的设置就会水到渠成



## Code

### Python

```python
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        node_dict = {}
        self.dfs_graph(node, node_dict)
        self.set_neighbor(node_dict)
        return node_dict[node]

    def dfs_graph(self, node, node_dict):
        if node in node_dict:
            return
        new_node = UndirectedGraphNode(node.label)
        node_dict[node] = new_node
        for neighbor in node.neighbors:
            self.dfs_graph(neighbor, node_dict)
    
    def set_neighbor(self, node_dict):
        for node in node_dict:
            new_node = node_dict[node]
            for neighbor in node.neighbors:
                new_node.neighbors.append(node_dict[neighbor])
```

### C++

```cpp
class Solution {
public:
    UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
        if (node == NULL) {
            return NULL;
        }
        unordered_map<UndirectedGraphNode *, UndirectedGraphNode *> node_dict;
        dfs_graph(node, node_dict);
        set_neighbors(node_dict);
        return node_dict[node];
    }
    void dfs_graph(UndirectedGraphNode *node, unordered_map<UndirectedGraphNode *, UndirectedGraphNode *> &node_dict) {
        auto it = node_dict.find(node);
        if (it != node_dict.end()) {
            return;
        }
        UndirectedGraphNode *new_node = new UndirectedGraphNode(node->label);
        node_dict.insert(make_pair(node, new_node));
        for (auto it : node->neighbors) {
            dfs_graph(it, node_dict);
        }
    }
    void set_neighbors(unordered_map<UndirectedGraphNode *, UndirectedGraphNode *> &node_dict) {
        for (auto dict_it : node_dict) {
            UndirectedGraphNode *node = dict_it.first;
            UndirectedGraphNode *new_node = dict_it.second;
            for (auto vec_it : node->neighbors) {
                (new_node->neighbors).push_back((node_dict.find(vec_it))->second);
            }
        }
    }
};
```