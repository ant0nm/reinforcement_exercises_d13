# input: list of numnbers
# output: sum of odd numbers (num % 2 != 0) ONLY
def sum_odd(nums):
    sum = 0
    for num in nums:
        if num % 2 != 0:
            sum += num
    return sum

# test out the function
# odd numbers: -1, 1, 3, 5, 7, 9, 11, 13, 15
# expected sum: 63
numbers = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print("The sum of odd numbers in the list is:")
print(sum_odd(numbers))
