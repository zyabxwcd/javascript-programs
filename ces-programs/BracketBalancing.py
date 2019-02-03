from pythonds.basic.stack import Stack

def bracketChecker(string):
    bracket = ('(','{','[')
    s = Stack()
    balanced = True
    index = 0
    while index < len(string) and balanced:
        symbol = string[index]
        if symbol in bracket:
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        return False

string = input('Enter string: ')
print(bracketChecker(string))