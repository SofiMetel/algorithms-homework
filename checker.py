#3. Write an algorithm that checks whether an element occurs in an array.


element1 = int(input('enter your input:'))
#element = 8
arr1 = [1, 42, 2, 8, 10, 7]


def check(element, arr):
    i=0
    while i < len(arr):
        if arr[i]==element:
            return True
        else: 
            i=i+1
    return False


print(check(element1, arr1))