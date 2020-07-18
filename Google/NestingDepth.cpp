#include <iostream>
using namespace std;

int main()
{
    int cases;
    std::cin >> cases;
    ++cases;

    string in, ret;
    int j, t, currInside, v, c, si, prev;
    for(int i = 1; i < cases; ++i)
    {
        cin >> in;
        t = in.size();
        currInside = 0;
        si = 0;
        prev = 0;
        for(j = 0; j < t; ++j)
        {
            v = (int)in[j] - 48;
            if(v >= 0)
            {
                c = v - prev;
                if(c > 0)
                {
                    while(c)
                    {
                        ret.insert(si++, "(");
                        ++currInside;
                        --c;
                    }
                }
                else if(c < 0)
                {
                    while(c)
                    {
                        ret.insert(si++, ")");
                        --currInside;
                        ++c;
                    }
                }
                ret.insert(si++, to_string(v));
            }
            prev = v;
        }
        if(currInside > 0)
        {
            while(currInside)
            {
                ret.insert(si++, ")");
                --currInside;
            }
        }
        cout << "Case #" << i << ": " << ret << endl;
        ret.clear();
    }
    return 0;
}