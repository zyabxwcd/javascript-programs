def bracketChecker(string):
    bracket = ('(','{','[')
    s = []
    balanced = True
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]
        if symbol in bracket:
            s.append(symbol)
        else:
            if len(s) == 0:
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and len(s) == 0:
        return True
    else:
        return False

string = input('Enter string: ')
print(bracketChecker(string))