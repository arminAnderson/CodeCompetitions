#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

struct Pair
{
    int a = 0, b = 0;
    void Print()
    {
        cout << a << "," << b << endl;
    }
    bool Equals(Pair p)
    {
        return a == p.a && b == p.b;
    }
};

void Print(string s)
{
    cout << s << endl;
}

int main()
{
    int cases;
    Pair board;
    cin >> cases >> board.a >> board.b;
    ++cases;
    string input;
    for(int i = 1; i < cases; ++i)
    {
        Pair temp {-5, -5};
        for(int j = 0; j < 11; ++j)
        {
            for(int k = 0; k < 11; ++k)
            {
                cout << temp.a + j << " " << temp.b + k << endl;
                cin >> input;
                if(input == "WRONG" || input == "CENTER")
                {
                    break;
                }
            }
            if(input == "WRONG" || input == "CENTER")
            {
                break;
            }
        }
        if(input == "WRONG")
        {
            break;
        }
    }
    return 0;
}