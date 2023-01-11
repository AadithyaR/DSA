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
    if (min != i):
        temp = Arr[i]
        Arr[i] = Arr[min]
        Arr[min] = temp
    i = i+1
print(Arr)
