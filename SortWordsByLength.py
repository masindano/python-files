'''
BSCIT-05-0133/2024
Masindano Masila
'''
#function for sorting
def sort_by_length(words):
    # sort the list using the length of each word
    return sorted(words, key=len)

# list to be sorted 
words_list = ["apple", "dog", "banana", "cat", "kiwi"]
sorted_list = sort_by_length(words_list)
print("Words sorted by length:", sorted_list)
