'''
Masindano Masila
BSCIT-05-0133/2024
'''

#program takes multiple names as input
names = input("Enter names separated by commas: ").split(",")
total = len(names)

#program removes duplicates using set()and sort names alphabetically using sorted()
names = sorted(set(name.strip() for name in names))

#program noww displays the total number of names entered
print("Sorted names without duplicates: ", names)
print("Total number of names entered: ", total)
