/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {}

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
public:
    Node* cloneGraph(Node* node) {
        if (!node) {
            return NULL;
        }
        Node *copied = new Node(node->val, vector<Node*>());
        unordered_map<Node *,Node *> map;
        queue<Node *> que;

        map[node] = copied;
        que.push(node);
        while (!que.empty()) {
            Node *cur = que.front();
            que.pop();
            for (auto neighbor: cur->neighbors) {
                if (map.find(neighbor) == map.end()) {
                    que.push(neighbor);
                    map[neighbor] = new Node(neighbor->val, vector<Node*>());
                }
                map[cur]->neighbors.push_back(map[neighbor]);
            }
        }
        return copied;
    }
};
