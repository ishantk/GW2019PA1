# Passing Reference
def squareOfNumbers(nums):

    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]

    print("nums:", nums)

numbers = [10, 20, 30, 40, 50]
squareOfNumbers(numbers)
print("numbers:",numbers)