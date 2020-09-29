#include "iostream"
using namespace std;

int Step(int max, int * dp)
{
    if(max < -1) { return 0; }
    if(max == -1) { return 1; }

    if(dp[max] == -1)
    {
        dp[max] = Step(max - 3, dp) + Step(max - 2, dp) + Step(max - 1, dp); 
    }

    return dp[max];
}

int main()
{
    const int size = 3;
    int dp[size];
    for(int i = 0; i < size; ++i) { dp[i] = -1; }
    cout << Step(size - 1, dp) << endl;
    return 0;
}