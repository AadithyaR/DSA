N = int(input())
Arr = list(map(int,input().split()))
print("N: ",N," Arr: ",Arr)
pos = int(input("Enter the position to be deletion:"))
for i in range(pos-1,N-1):
    Arr[i] = Arr[i+1]
print("Modified: ", Arr[:-1])
