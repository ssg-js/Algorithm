#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
    int a[5];
    int avg, middle;
    int sum = 0;
    for (int i = 0; i < 5; i++) {
        cin >> a[i];
        sum += a[i];
    }
    avg = sum / 5;
    sort(a, a + 5);
    cout << avg << endl << a[2];
}