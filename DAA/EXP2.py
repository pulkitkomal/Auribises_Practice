def mergeSort(nlist):
    # print("Splitting ",nlist)
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=j=k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1
    # print("Merging ",nlist)


list = []
TNE = int(input('Total Number of Elements: '))
for x in range(0,TNE):
    a = int(input('Enter {} Element: '.format(x)))
    list.append(a)
print('List before merge sort:',list)
mergeSort(list)
print('List after merge sort:',list)