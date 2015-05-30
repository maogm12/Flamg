# 155-Min Stack

## Problem

> Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

> - `push(x)` -- Push element x onto stack.
> - `pop()` -- Removes the element on top of the stack.
> - `top()` -- Get the top element.
> - `getMin()` -- Retrieve the minimum element in the stack.

## Solution

第一印象就是保存最小值，每次 push 的时候就更新，但是 pop 的时候这个最小值就失效了，这个时候我们应该拿出纸来画一画

比如依次 push 2 3 1，然后依次 pop，过程如下，邮编是最小值

    [2]       2
    [2 3]     2
    [2 3 1]   1
    [2 3]     2
    [2]       2

恩，我们发现在栈里面的东西一样的时候，最小值是一样的，那么我们是不是可以为栈每一个位置维护一个最小值呢！

只此一点，该题便是一个大水题。。。

## Code

### Python

```python

```

### C++

额外保存一个栈记录每个位置的最小值，同步更新

```cpp
class MinStack {
public:
    void push(int x) {
        dataStack.push(x);
        if (minStack.empty() || minStack.top() > x) {
            minStack.push(x);
        } else {
            minStack.push(minStack.top());
        }
    }

    void pop() {
        if (dataStack.empty()) {
            throw out_of_range("Empty stack");
        }
        dataStack.pop();
        minStack.pop();
    }

    int top() {
        if (dataStack.empty()) {
            throw out_of_range("Empty stack");
        }
        return dataStack.top();
    }

    int getMin() {
        if (minStack.empty()) {
            throw out_of_range("Empty stack");
        }
        return minStack.top();
    }
private:
    stack<int> dataStack;
    stack<int> minStack;
};
```
