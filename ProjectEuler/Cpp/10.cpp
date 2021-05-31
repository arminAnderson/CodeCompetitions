#include <iostream>
#include <math.h>
using namespace std;

bool IsPrime(long long num)
{
    if(num == 2) { return true; }
    if(num < 2 || num % 2 == 0) { return false; }
    int midpoint = int(sqrt(num));
    for(int i = 3; i <= midpoint; ++i)
    {
        if(num % i == 0) { return false; }
    }
    return true;
}

int main()
{
    long long sum = 0;
    for(int i = 0; i < 2000000; ++i)
    {
        if(IsPrime(i))
        {
            sum += i;
        }
    }
    cout << sum << endl;
}