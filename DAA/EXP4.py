def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0

    if (wt[n - 1] > W):
        return knapSack(W, wt, val, n - 1)

    else:
        return max(val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
                   knapSack(W, wt, val, n - 1))


val = []
wt = []

x = int(input('Enter total number of items: '))
for x in range(0,x):
    a = int(input('Enter Value: '))
    val.append(a)
    b = int(input('Enter Weight: '))
    wt.append(b)

W = int(input('Enter Max Wieght: '))
n = len(val)
print(knapSack(W, wt, val, n))