#include <iostream>
#include <vector>

using namespace std;

struct Pair
{
    int a = 0, b = 0;
    string d = "";
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

vector<Pair> Find(vector<Pair> path, Pair target, int step = 0, int sum = 0)
{
    vector<Pair> empty, test;
    path[0].a = sum;
    if(path.size() == 0) { return empty; }
    if(path[path.size() - 1].Equals(target)) { return path; }
    if(sum > abs(target.a) + abs(target.b)) { return empty; }

    if(!step) { step = 1; }
    else { step *= 2; }
    sum += step;
    
    Pair np = path[path.size() - 1];
    path.push_back(np);

    path[path.size() - 1].a += step;
    path[path.size() - 1].d = "E";
    empty = Find(path, target, step, sum);

    path[path.size() - 1].a -= step * 2;
    path[path.size() - 1].d = "W";
    test = Find(path, target, step, sum);
    if(empty.size() > 0 && test.size() > 0) 
    { 
        if(test[0].a < empty[0].a)
        {
            empty = test;
        }
    }
    else if(test.size() > 0) { empty = test; }
    

    path[path.size() - 1].a += step;
    path[path.size() - 1].b += step;
    path[path.size() - 1].d = "N";
    test = Find(path, target, step, sum);
    if(empty.size() > 0 && test.size() > 0) 
    { 
        if(test[0].a < empty[0].a)
        {
            empty = test;
        }   
    }
    else if(test.size() > 0) { empty = test; }

    path[path.size() - 1].b -= step * 2;
    path[path.size() - 1].d = "S";
    test = Find(path, target, step, sum);
    if(empty.size() > 0 && test.size() > 0) 
    { 
        if(test[0].a < empty[0].a)
        {
            empty = test;
        }
    }
    else if(test.size() > 0) { empty = test; }

    return empty;
}

void PrintResult(vector<Pair> * p)
{
    for(int i = 0; i < p->size(); ++i)
    {
        cout << (*p)[i].d;
    }
    cout << endl;
}
int main()
{
    int cases;
    std::cin >> cases;
    ++cases;
    for(int i = 1; i < cases; ++i)
    {
        vector<Pair> dirs;
        Pair target;
        dirs.push_back(target);
        cin >> target.a >> target.b;
        vector<Pair> r = Find(dirs, target);
        string ret = "POSSIBLE";
        if(r.size() == 0) { ret = "IMPOSSIBLE"; }
        else { ret = ""; }
        std::cout << "Case #" << i << ": ";
        if(ret != "")
        {
            cout << "IMPOSSIBLE" << endl;
        }
        else
        {
            PrintResult(&r);
        }
        
    }
    return 0;
}