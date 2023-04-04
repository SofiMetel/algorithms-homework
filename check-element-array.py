def linear_search_recursion(arr, target, index):
    if index >= len(arr):
        return False
    if arr[index]==target:
        return True
    
    return linear_search_recursion(arr, target, index+1)
    



print(linear_search_recursion([0,3,4,2,8,1,9], 4, 0))
