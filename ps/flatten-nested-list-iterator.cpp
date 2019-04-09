/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

struct Pair {
    vector<NestedInteger> nested;
    int idx;
    Pair(vector<NestedInteger> _nested, int _idx) {
        nested = _nested;
        idx = _idx;
    }
};
class NestedIterator {
public:
    stack<Pair*> stk;
    int nexts;
    NestedIterator(vector<NestedInteger> &nestedList) {
        Pair *pair = new Pair(nestedList, 0);
        if (nestedList.size() != 0) 
            stk.push(pair);
    }

    int next() {
        return nexts;
    }

    bool hasNext() {
        if (stk.size() == 0) return false;
        Pair *pair = stk.top();
        int res;
        
        while (!pair->nested[pair->idx].isInteger()) {
            if (pair->idx + 1 >= pair->nested.size()) stk.pop();
            pair = new Pair(pair->nested[pair->idx++].getList(), 0);
            if (pair->nested.size() != 0)
                stk.push(pair);
            else {
                if (stk.size() == 0) return false;
                pair = stk.top();
            }
        }
        res = pair->nested[pair->idx].getInteger();
        pair->idx++;
        if (pair->idx == pair->nested.size()) {
            stk.pop();
        }
        
        nexts = res;
        return true;
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
