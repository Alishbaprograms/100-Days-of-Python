# Write your code here :-)
def BinarySearchRec(arr,lb,ub, data):

    mid = (ub+lb)//2
    if lb > ub:
        return -1
    elif arr[mid] == data:
        return mid
    elif arr[mid] > data:
        return BinarySearchRec(arr, lb, mid-1, data)
    else:
        return BinarySearchRec(arr, mid+1, ub, data)

arr = ["a", "b", "c", "d", "e", "f", "g", "h"]
x = BinarySearchRec(arr,0,7,"h")
if x == -1:
    print("element not found")
else:
    print("element found at :" , x+1)
