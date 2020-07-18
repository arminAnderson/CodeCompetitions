#include <iostream>
#include <unordered_set>
using namespace std;

int main()
{
    int cases;
    std::cin >> cases;
    ++cases;

    int ** matrix = NULL;
    unordered_set<int> checkX, checkY;
    
    int size, tempA, k, r, c;
    for(int i = 1; i < cases; ++i)
    {
        cin >> size;
        tempA = size * size;
        matrix = new int*[size];
        for(int a = 0; a < size; ++a) { matrix[a] = new int[size]; }
        k = 0;
        r = 0;
        c = 0;
        for(int a = 0; a < size; ++a)
        {
            tempA = 1;
            for(int b = 0; b < size; ++b)
            {
                cin >> matrix[a][b];
                if(a == b) { k += matrix[a][b]; }
                if(tempA)
                {
                    auto p = checkX.insert(matrix[a][b]);
                    if(!p.second)
                    {
                        ++r;
                        tempA = 0;
                    }
                }
            }
            checkX.clear();
        }    

        for(int b = 0; b < size; ++b)
        {
            tempA = 1;
            for(int a = 0; a < size; ++a)
            {
                if(tempA)
                {
                    auto p = checkX.insert(matrix[a][b]);
                    if(!p.second)
                    {
                        ++c;
                        tempA = 0;
                    }
                }
            }
            checkX.clear();
        }    

        cout << "Case #" << i << ": " << k << " " << r << " " << c <<endl;
        for(int i = 0; i < size; i++) { delete[] matrix[i]; }
        delete[] matrix;
    }
    
    return 0;
}