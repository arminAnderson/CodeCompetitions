#include <iostream>
using namespace std;

int main()
{
    int a = 1, b = 2, sum = 0;
    while(b < 4000000)
    {
        if(b % 2 == 0)
        {
            sum += b;
        }
        b = a + b;
        a = b - a;
    }
    cout << sum << endl;
}