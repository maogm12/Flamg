#include <iostream>
#include <chrono>
using namespace std;

int main()
{
    int times = 1000000;
    int number = 15, temp;
    auto t1 = chrono::system_clock::now();
    for (int i = 0; i < times; ++i) {
        temp = number % 10;
    }
    auto t2 = chrono::system_clock::now();
    for (int i = 0; i < times; ++i) {
        temp = number - 10;
    }
    auto t3 = chrono::system_clock::now();
    cout << "%: " << chrono::duration_cast<chrono::microseconds>(t2 - t1).count() << " microseconds" << endl
        << "-: " << chrono::duration_cast<chrono::microseconds>(t3 - t2).count() << " microseconds" << endl;

    /**
     * The output on my RMBP is as follows:
     * %: 5128 microseconds
     * -: 2273 microseconds
     */

    return 0;
}
