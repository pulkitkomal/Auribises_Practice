
def logic(i):
    if i[-3:] == 'ing':
        i = i + 'ly'
        print(i)

i = input ('Enter word with ing at the end: ')
logic(i)
