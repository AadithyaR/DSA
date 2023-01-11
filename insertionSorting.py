N = int(input())
Arr = list(map(int,input().split()))
print("N: ",N," Arr: ",Arr)
for i in range(1,len(Arr)):
    key = Arr[i]
    j = i - 1
    while j>=0 and key < Arr[j]:
        Arr[j+1] = Arr[j]
        j -=1
    Arr[j+1] = key
print(Arr)
