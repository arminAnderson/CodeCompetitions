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
    long long check = 600851475143;
    int mid = int(sqrt(check));
    int underside = 0;
    for(int i = 1; i <= mid; ++i)
    {
        if(check % i == 0)
        {
            if(IsPrime(check/i)) { cout << check/i << endl; break; }
            else
            {
                if(IsPrime(i)) { underside = i; }
            }
        }
    }
    cout << underside << endl;
}