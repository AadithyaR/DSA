N = int(input())
Arr = list(map(int,input().split()))
print("N: ",N," Arr: ",Arr)
F = -1
for i in range(N-1):
    for j in range(N-i-1):
        if Arr[j] > Arr[j+1]:
            temp = Arr[j]
            Arr[j] = Arr[j+1]
            Arr[j+1] = temp
            F = 0
    if F==-1:
        break
print(Arr)
