import time
current=time.time()
print(current)
arr=[]
u=int(input("enter the no of elements you want in array"))
for i in arr:
    if len(arr)< u:
        n=int(input("enter a no in array"))
        arr.append(n)
    else:
        print("array is full")
current1=time.time()
print(current1-current)
search=int(input("enter the number you want to search"))
for j in arr:
    if search == arr[j]:
        print(" element is found",j)

    else:
        print("element is not in the array")

current2=time.time()
print(current2-current1)
