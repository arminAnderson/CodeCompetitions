#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int cases;
    std::cin >> cases;
    ++cases;

    for(int i = 1; i < cases; ++i)
    {
        int words;
        cin >> words;

        string temp, base = "";
        vector<string> strings;
        for(int j = 0; j < words; ++j)
        {
            cin >> temp;
            strings.push_back(temp);
        }
        for(int j = 0; j < strings.size(); ++j)
        {
            if(base == "")
            {
                base = strings[j].substr(1, strings[j].size());
            }
            else
            {
                temp = strings[j].substr(1, strings[j].size());
                if(temp.size() > base.size())
                {
                    base = temp;
                    j = -1;
                }
                else
                {
                    /*string s = base;
                    bool good = false;
                    while(s.size() > 0 && s.find(temp) != string::npos)
                    {
                        s = s.substr(s.find(temp) + temp.size(), s.size());
                        if(s == "") { good = true; break; }
                        cout << base + " " + temp + " " + s << endl;
                    }
                    if(!good) { base = "*"; break; }
                    */
                    if(base.substr(base.size() - temp.size(), base.size()) != temp)
                    {
                        base = "*";
                        break;
                    }
                }
                
            }
        }

        std::cout << "Case #" << i << ": " << base << std::endl;
    }
    return 0;
}