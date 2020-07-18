#include <iostream>
#include <vector>
#include <math.h>
#include <unordered_set>
#include <algorithm>  
#include <climits>
using namespace std;

template <typename D>
struct Duo 
{ 
    Duo() {}
    Duo(D a, D b) : a(a), b(b) {}
    D a; 
    D b; 
};

template <typename D>
inline bool operator==(const Duo<D> &a, const Duo<D> &b) { return a.a == b.a && a.b == b.b; }

template <typename D>
void Print(Duo<D> d) { cout << d.a << "," << d.b << endl; }
template <typename T>
void Print(T t) { cout << t << endl; }
template <typename T>
void Print(vector<T> * v) { for(int i = 0; i < v->size(); ++i) { Print((*v)[i]); } }

template <typename D>
bool SortDuo(Duo<D> a, Duo<D> b) { return a.a < b.a; }

template <typename D>
void SortVector(vector<Duo<D>> * v) { sort(v->begin(), v->end(), SortDuo<D>); }
template <typename V>
void SortVector(vector<V> * v) { sort(v->begin(), v->end()); }

int Search(Duo<int> me, Duo<int> pep, string * path, int mins = 0)
{
    if(me == pep) { return mins; }
    if(mins == path->size()) { return -1; }
    int a = pep.a - me.a;
    int b = pep.b - me.b;
    if(sqrt(a * a + b * b) > (path->size() - mins) * 2) { return -1; }

    if((*path)[mins] == 'N') { ++pep.b; }
    if((*path)[mins] == 'S') { --pep.b; }
    if((*path)[mins] == 'E') { ++pep.a; }
    if((*path)[mins] == 'W') { --pep.a; }

    int test;
    int best = INT_MAX;

    if(abs(a) <= 1 && abs(b) <= 1)
    {
        test = Search(me, pep, path, mins + 1); 
        if(test != -1 && test < best) { best = test; }
    }
    
    if(pep.a > me.a)
    {
        ++me.a;
        test = Search(me, pep, path, mins + 1);
        if(test != -1 && test < best) { best = test; }
        --me.a;
    }

    if(pep.a < me.a)
    {
        --me.a;
        test = Search(me, pep, path, mins + 1);
        if(test != -1 && test < best) { best = test; }
        ++me.a;
    }

    if(pep.b > me.b)
    {
        ++me.b;
        test = Search(me, pep, path, mins + 1);
        if(test != -1 && test < best) { best = test; }
        --me.b;
    }

    if(pep.b < me.b)
    {
        --me.b;
        test = Search(me, pep, path, mins + 1);
        if(test != -1 && test < best) { best = test; }
        ++me.b;
    }
    
    if(best == INT_MAX) { best = -1; }
    return best;
}

int main()
{
    int cases;
    std::cin >> cases;
    ++cases;

    for(int i = 1; i < cases; ++i)
    {
        Duo<int> offset {0,0};
        Duo<int> peppur;
        cin >> peppur.a >> peppur.b;
        string path;
        cin >> path;
        int s = -1;
        if(abs(peppur.b - offset.b) <= path.size() * 2)
        {
            s = Search(offset, peppur, &path);
        }

        if(s == -1)
        {
            cout << "Case #" << i << ": " << "IMPOSSIBLE" <<endl;   
        }
        else
        {
            cout << "Case #" << i << ": " << s <<endl;
        }
    }
    return 0;
}