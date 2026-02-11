'''
BSCIT-05-0133/2024
Masindano Masila
'''

# Function to get only even numbers from a list
def get_even_numbers(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:  # check if number is divisible by 2
            even_numbers.append(num)
    return even_numbers


nums = [1, 2, 3, 4, 5, 6, 7, 8]
even_nums = get_even_numbers(nums)
print("Even numbers:", even_nums)
