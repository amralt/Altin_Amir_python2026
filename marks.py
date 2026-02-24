def is_correct_brackets(s):
    stack = []  
    for i in s:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    return False

s = input()
if is_correct_brackets(s):
    print("YES")
else:
    print("NO")
        