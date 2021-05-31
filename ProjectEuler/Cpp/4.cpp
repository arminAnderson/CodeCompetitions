#include <iostream>
using namespace std;

bool IsPalindrome(int num)
{
    if(num % 10 == 0) { return false; }
    int choppedNum = 0;
    int left = 0;
    while(left < num)
    {
        choppedNum = num%10;
        num /= 10;
        if(num == left) { return true; }
        left *= 10;
        left += choppedNum;
        if(num == left) { return true; }
    }
    return false;
}

int main()
{
    int max = 0;
    for(int i = 100; i < 1000; ++i)
    {
        for(int j = 100; j < 1000; ++j)
        {
            if(IsPalindrome(i * j))
            {
                if(i * j > max)
                {
                    max = i * j;
                }
            }
        }
    }
    cout << max << endl;
}