N = int(input())
Arr = list(map(int,input().split()))
print("N: ",N," Arr: ",Arr)
n = int(input("Enter the element: "))
pos = int(input("Enter the position:"))
Arr.append(0)
while(N>pos-1):
    Arr[N] = Arr[N-1]
    N = N-1
Arr[pos-1] = n
print("Modified: ", Arr)
