#include <iostream>
#include <unordered_set>
using namespace std;

unordered_set<int> products;
unordered_set<int> temp;
bool IsPandigital(int a, int b, int c)
{
    temp.clear();
    temp.insert(0);
    for(int i = 0; i < 3; ++i)
    {
        int t;
        switch (i)
        {
        case 0: t = a; break;
        case 1: t = b; break;
        case 2: t = c; break;
        }
        while(t > 0)
        {
            auto v = temp.insert(t % 10);
            if(!v.second) { return false; }
            t /= 10;
        }
    }

    return temp.size() == 10;
}

int main()
{
    int sum = 0;
    for(int i = 0; i < 2000; ++i)
    {
        for(int j = 0; j < 2000; ++j)
        {
            if(products.count(i * j) == 0)
            {
                if(IsPandigital(i, j, i * j))
                {
                    cout << i << " " << j << " " << i * j << " ";
                    cout << endl;
                    products.insert(i * j);
                    sum += i * j;
                }
            }
        }
    }
    cout << sum << endl;
    return 0;
}
