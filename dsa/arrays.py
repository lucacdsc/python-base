

arr = [12,34,10,6,40]
key = 10
n = len(arr)

def findElement(arr,n,key):
    for i in range(n):
        if arr[i] == key:
            return i
    return -1
        
print(findElement([12,34,10,6,40],len(arr),10))

index = findElement(arr,n,key)
if index != -1:
    print(f"Element found at position {index + 1}")
else:
    print("Element not found")

