bool Func(std::string s)
{
    //1 -> p, 2 -> b, 3 -> c
    std::stack<int> stack;
    for(int i = 0; i < s.length(); ++i)
    {
        switch (s[i])
        {
        case '(': stack.push(1); break;
        case '[': stack.push(2); break;
        case '{': stack.push(3); break;
        case ')': if(stack.size() == 0 || stack.top() != 1) { return false; } else { stack.pop(); break; }
        case ']': if(stack.size() == 0 || stack.top() != 2) { return false; } else { stack.pop(); break; }
        case '}': if(stack.size() == 0 || stack.top() != 3) { return false; } else { stack.pop(); break; }
        default:
            std::cout << "Invalid char in sequence: " << s[i] << std::endl;
            return false;
        }
    }
    return stack.size() == 0;
}