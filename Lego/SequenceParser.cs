int num = 0;
string ret = "";
if (char.IsDigit(s[0]))
{
    for (int i = 0; i < s.Length; ++i)
    {
        if (char.IsDigit(s[i]))
        {
            num *= 10; 
            num += (int)char.GetNumericValue(s[i]);
        }
        else
        {
            while (num > 0)
            {
                --num; ret += s[i];
            }
        }
    }
}
else
{
    char prev = s[0];
    for (int i = 0; i < s.Length; ++i)
    {
        if(prev != s[i]) 
        { 
            ret += num.ToString() + prev;
            prev = s[i];
            num = 0;
        }
        ++num;
    }
    ret += num.ToString() + prev;
}
return ret;