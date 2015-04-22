#include <iostream>
#include <vector>
#include <functional>
using namespace std;

int calcStairs(int n) {
    vector<int> ways(n + 1, -1);
    ways[0] = 1;
    ways[1] = 1;
    // ERROR!!! cannot use auto
    auto calcWays = [&](int n) -> int {
        if (ways[n] == -1) {
            ways[n] = calcWays(n - 1) + calcWays(n - 2);
        }
        return ways[n];
    };

    return calcWays(n);
}

int main()
{
    return 0;
}
