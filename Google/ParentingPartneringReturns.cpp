#include <iostream>
#include <algorithm>  
#include <vector>
using namespace std;

struct AB
{
    int a, b, c;
    char n;
    void Print()
    {
        cout << c << " | " << n << endl;
    }
};

bool SortAB(AB a, AB b)
{
    return a.a < b.a;
}

int main()
{
    int cases;
    std::cin >> cases;
    ++cases;
    
    vector<AB> p;
    int n, t;
    AB c, j;
    string ret;
    for(int i = 1; i < cases; ++i)
    {
        cin >> n;
        p.reserve(n);
        ret.reserve(n);
        for(int s = 0; s < n; ++s) { ret += 'X'; }
        t = 0;
        c = {1, 0, 0};
        j = c;
        while(t < n)
        {
            p.push_back(c);
            p[t].c = t;
            cin >> p[t].a >> p[t].b;
            ++t;
        }
        t = 0;
        sort(p.begin(), p.end(), SortAB);
        while(t < n)
        {
            if(p[t].a >= c.b)
            {
                c.b = p[t].b;
                p[t].n = 'C';
            }
            else if(p[t].a >= j.b)
            {
                j.b = p[t].b;
                p[t].n = 'J';
            }
            else
            {
                ret = "IMPOSSIBLE";
                break;
            }
            ++t;
        }

        if(t == n)
        {
            for(t = 0; t < n; ++t)
            {
                ret[p[t].c] = p[t].n;
            }
        }
        
        cout << "Case #" << i << ": " << ret <<endl;
        p.clear();
        ret.clear();
    }
    
    return 0;
}