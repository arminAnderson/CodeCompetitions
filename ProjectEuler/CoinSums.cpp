#include <iostream>
using namespace std;

//make [0] the end
const int s = 201;
int dp[s];
int val = 200;
int coins[] {1, 2, 5, 10, 20, 50, 100, 200};

void A()
{
    dp[0] = 1;
    for(int i = 0; i < sizeof(coins)/sizeof(int); ++i)
    {
        for (int j = coins[i]; j <= val; j++) {
            dp[j] += dp[j - coins[i]];
        }
    }
    cout << dp[val] << endl;
}

int B(int val, int depth)
{
    int w = 0;
    if(val == 0) { return 1; }
    if(val < 0) { return 0; }
    for(int i = depth; i >= 0; --i)
    {
        w += B(val - coins[i], i);
    }
    return w;
}

int F(int n, int k)
{
    if(n < 0) { return 0; }
    if(n == 0) { return 1; }
    if(k < 0) { return 0; }
    return F(n, k-1) + F(n - coins[k], k);
}

int main()
{
    cout << "A: ";
    for(int i = 0; i < s; ++i) { dp[i] = 0; }
    A();
    cout << "B: ";
    for(int i = 0; i < s; ++i) { dp[i] = 0; }
    cout << B(200, 7) << endl;
    cout << "C: ";
    cout << F(200, 7) << endl;
    return 0;
}