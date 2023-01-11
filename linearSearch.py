N = int(input())
Arr = list(map(int,input().split()))
print("N: ",N," Arr: ",Arr)
n = int(input("Enter the element: "))
pos = -1
for i in range(N):
    if Arr[i] == n:
        pos = i+1
        break
if pos != -1:
    print("Element "+str(n)+" found at position "+ str(pos))
else:
    print("Not Found")
