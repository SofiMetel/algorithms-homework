4#. computes the sum of an array of numbers.


def sum(nums):
    return sum_r(nums, 0)

def sum_r(nums, index):
    if index == len(nums)-1:
        return nums[index]
    return nums[index] + sum_r(nums, index+1)

print(sum([1,2,3,4]))