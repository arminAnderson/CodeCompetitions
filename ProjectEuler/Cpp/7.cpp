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
    int count = 0;
    int i = 2;
    while(count != 10001)
    {
        if(IsPrime(i)) { ++count; }
        ++i;
    }
    cout << --i << endl;
}