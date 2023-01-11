N = int(input())
Arr = list(map(int,input().split()))
print("N: ",N," Arr: ",Arr)
i = 0
while(i<N-1):
    min = i
    j = i+1
    while(j<N):
        if(Arr[j]<Arr[min]):
            min = j
        j = j+1
    key = Arr[min]
    while(min>i):
        Arr[min] = Arr[min-1]
        min -= 1
    Arr[i] = key
    i = i+1
print(Arr)
