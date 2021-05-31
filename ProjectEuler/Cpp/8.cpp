#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
    string line;
    ifstream myfile ("8_test.txt");
    vector<int> sequence;
    while(getline(myfile, line)) {
        for(char s : line)
        {
            sequence.push_back(s - '0');
        }
    }
    myfile.close();
    long long best = 1;
    long long temp = 1;
    for(int i = 0; i < sequence.size(); ++i)
    {
        for(int j = 0; j < 13; ++j) { temp *= sequence[i + j]; }
        if(temp > best) { best = temp; }
        temp = 1;
    }
    cout << best << endl;
}