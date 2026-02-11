'''
BSCIT-05-0133/2024
Masindanoo Masila
'''

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase for accurate checking
    s = s.replace(" ", "").lower()
    # Check if string is the same forwards and backwards
    return s == s[::-1]

# Example usage:
word = "Madam"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
