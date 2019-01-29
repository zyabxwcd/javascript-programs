def sub_arrays(array, inc=True):
    i = 0
    j = 1
    length = len(array)
    if inc:
        while j < length:
            if array[j] < array[j-1]:
                if len(array[i:j]) == 1:
                    i = j
                    j = i + 1
                else:
                    print(array[i:j])
                    i = j
                    j = i + 1
            else:
                j += 1
    else:
        while j < length:
            if array[j] > array[j-1]:
                if len(array[i:j]) == 1:
                    i = j
                    j = i + 1
                else:
                    print(array[i:j])
                    i = j
                    j = i + 1
            else:
                j += 1
                
    print(array[i:j] if len(array[i:j]) != 1 else '', end='')


array = [int(i) for i in input().split()]
sub_arrays(array, inc=False)