'''
Given a list of numbers print sub-arrays following a pattern of increasing or decreasing.
'''


def sub_arrays(array, inc=True):
    i = 0
    j = 1
    length = len(array)
    if inc:
        while j < length:
            if array[j] < array[j-1]:
                print( array[i:j] if len( array[i:j] ) != 1 else '', end='')
                i = j
                j = i + 1
            else:
                j += 1
    else:
        while j < length:
            if array[j] > array[j-1]:
                print( array[i:j] if len( array[i:j] ) != 1 else '', end='')
                i = j
                j = i + 1
            else:
                j += 1

    print(array[i:j] if len(array[i:j]) != 1 else '', end='')

# Input list of numbers
array = [int(i) for i in input().split()]
sub_arrays(array)
