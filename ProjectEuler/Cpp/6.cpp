#include <iostream>
using namespace std;

int main()
{
    int sumOfSquares = 0;
    int squareOfSums = 0;
    for(int i = 1; i <= 100; ++i)
    {
        squareOfSums += i;
        sumOfSquares += i * i;
    }
    squareOfSums *= squareOfSums;
    cout << squareOfSums - sumOfSquares << endl;

}