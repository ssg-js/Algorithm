#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
    int N, ans[1001];
    cin >> N;
    ans[1] = 1;
    ans[2] = 3;
    for(int i=3; i<=N; i++) {
        ans[i] = (ans[i-2] * 2 % 10007 + ans[i-1] % 10007) % 10007;
    }
    cout << ans[N];
}