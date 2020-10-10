#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

const int SIZE = 1000000;
int init[] {0,0,0,0,0};
int primes[SIZE];
vector<int> primesOnly;

bool GetConcats(int a, int b, int c, int d, int e)
{
    init[0] = a; init[1] = b; init[2] = c; init[3] = d; init[4] = e;
    for(int i = 0; i < 5; ++i)
    {
        for(int j = i + 1; j < 5; ++j)
        {
            if(primes[int(pow(10, int(log10(init[j]))+1)*init[i]+init[j])] == 0) { return false; }
            if(primes[int(pow(10, int(log10(init[i]))+1)*init[j]+init[i])] == 0) { return false; }
        }
    }
    return true;
}

int main()
{
    for(int i = 0; i < SIZE; ++i) { primes[i] = 1; }
    primes[0] = 0;
    primes[1] = 0;

    for(int i = 2; i < SIZE; ++i)
    {
        if(primes[i] == 1)
        {
            primesOnly.push_back(i);
            for(int j = i * 2; j < SIZE; j += i)
            {
                primes[j] = 0;
            }
        }
    }

    int smallest = INT_MAX;
    int LIMIT = 1000;
    int length = 0;

    while (primesOnly[length] < LIMIT)
    {
        ++length;
    }

    for(int a = 0; a < length; a++)
    {
        if(primesOnly[a] * 5 > smallest) { break; }
        for(int b = a + 1; b < length; ++b)
        {
            if(primesOnly[a] + primesOnly[b] * 4 > smallest) { break; }
            for(int c = b + 1; c < length; ++c)
            {
                if(primesOnly[a] + primesOnly[b] + primesOnly[c] * 3 > smallest) { break; }
                for(int d = c + 1; d < length; ++d)
                {
                    if(primesOnly[a] + primesOnly[b] + primesOnly[c] + primesOnly[d] * 2 > smallest) { break; }
                    for(int e = d + 1; e < length; ++e)
                    {
                        if(primesOnly[a] + primesOnly[b] + primesOnly[c] + primesOnly[d] + primesOnly[e] > smallest) { break; }
                        /*if(GetConcats(primesOnly[a],primesOnly[b],primesOnly[c],primesOnly[d], primesOnly[e]))
                        {
                            smallest = primesOnly[a] + primesOnly[b] + primesOnly[c] + primesOnly[d] + primesOnly[e];
                            cout << smallest << endl;
                        }*/
                    }
                }
            }
        }
    }
    
    return 0;
}

