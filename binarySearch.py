N = int(input())
Arr = list(map(int,input().split()))
print("N: ",N," Arr: ",Arr)
n = int(input("Enter the element: "))
pos = -1
L = 0
H = N-1
while(L<=H):
    M = int((L+H)/2)
    if Arr[M] == n:
        pos = M+1
        break
    elif Arr[M]>n:
        H = M-1
    else:
        L = M+1
if pos != -1:
    print("Element "+str(n)+" found at position "+ str(pos))
else:
    print("Not Found")
