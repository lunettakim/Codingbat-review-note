# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(nums):
    #you need to find a sum of value / also should know index
    #therefore, you could you enumerate(get both index, value of list)
    for i num in enumerate(nums):
        if num == 13:
            nums[i] = 0
            if num[i+1] < len(nums): #to avoid an error if you assign num[i+1] which doesn't exist
                nums[i+1] = 0

    return sum(num)


def sum13_2(nums):         #without using enumerate
    sum_nums = 0
    for i in range(len(nums)):
        if nums[i] == 13:
            nums[i] = 0
            if i + 1 < len(nums):
                nums[i + 1] = 0

        else:
            sum_nums += nums[i]

    return sum_nums