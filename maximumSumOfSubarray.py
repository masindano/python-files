'''
Bscit-05-0133/2024
Masindano Masila
'''
#function of the subarray
def max_subarray_sum(nums):
    if not nums:  # check if the list is empty
        return 0

    max_sum = current_sum = nums[0]  # start with the first element

    for num in nums[1:]:
        # Either start a new subarray or continue the current one
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example usage:
numbers = [1, -2, 3, 4, -1, 2, -5, 6]
print("Maximum subarray sum is:", max_subarray_sum(numbers))
