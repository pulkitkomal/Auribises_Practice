def binary_search(item_list,item):

    first = 0
    last = len(item_list)-1
    found = False
    while( first<=last and not found):
        mid = (first + last)//2
        if item_list[mid] == item :
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

list = []
TNE = int(input('Total Number of Elements: '))
for x in range(0,TNE):
    a = int(input('Enter {} Element :'.format(x)))
    list.append(a)


inp = int(input('Enter Element you want to find: '))

print(binary_search(list, inp))