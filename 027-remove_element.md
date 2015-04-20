# 027-Remove Element

## Problem
> Given an array and a value, remove all instances of that value in place and return the new length.
>
> The order of elements can be changed. It doesn't matter what you leave beyond the new length.

去除数组中的某个元素，返回新长度，原地修改。

## Solution

- Loop

    直接往后循环，遇到不是指定元素的元素就往前填。

    时间复杂度为 O(n)，空间复杂度为 O(1)。

- STL

    STL 里面有超级多算法，可以合理利用哦！这里可以使用 STL 里面的 `remove` 算法：

    `remove` 算法的原型大概如下:

    ```cpp
    template <class ForwardIterator, class T>
    ForwardIterator remove (ForwardIterator first, ForwardIterator last, const T& val) {
        ForwardIterator result = first;
        while (first!=last) {
            if (!(*first == val)) {
            *result = move(*first);
            ++result;
            }
            ++first;
        }
        return result;
    }
    ```

    基本和我们要写的代码一模一样。然后使用 `distance` 函数或者直接减法计算新长度即可。

## Code

### Python

```python
# wait a minute
```

### C++

```cpp
class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        int newSize = 0;
        for (int i = 0; i < n; ++i) {
            if (A[i] != elem) {
                A[newSize++] = A[i];
            }
        }
        return newSize;
    }
};
```

### C++ with STL

```cpp
class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        // 也可以用 distance(A, remove(A, A + n, elem))
        return remove(A, A + n, elem) - A;
    }
};
```
