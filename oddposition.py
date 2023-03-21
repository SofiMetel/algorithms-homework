#4. Write an algorithm that returns the elements on odd positions in an array.

arr1 = [1, 42, 2, 8, 10, 7, 9, 99]

def oddposition(arr):
    i=0
    newarr = []
    while i<len(arr):
        if i%2!=1:
            i=i+1
        else:
            newarr.append(arr[i])
            i=i+1

    return newarr


print(oddposition(arr1))