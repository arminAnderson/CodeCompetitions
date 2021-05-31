#include <iostream>
using namespace std;

int main()
{
    int num = 19;
    bool passed = false;
    while(true)
    {
        passed = true;
        for(int i = 1; i < 21; ++i)
        {
            if(num % i != 0)
            {
                passed = false;
                break;
            }
        }
        if(passed) { cout << num << endl; break; }
        num += 19;
    }
}