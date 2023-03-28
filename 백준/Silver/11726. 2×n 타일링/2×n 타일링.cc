#include <iostream>
#include <algorithm>

using namespace std;

int value[10007];

int main(void) {
    int N;
    cin >> N;
    value[0] = 0;
    value[1] = 1;
    value[2] = 2;
    for(int i=3; i<=N; i++){
        value[i] = ((value[i-1] % 10007) + (value[i-2] % 10007)) % 10007;
    }
    cout << value[N];
}