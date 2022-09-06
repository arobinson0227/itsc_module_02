# Take in a list data structure as an input
user_list = []
user = (input('Enter a list of numbers: '))
user_list.append(user)

# Write a function to get unique values
def get_unique_list(user_list):
    unique_list = []
    for i in user_list:
        if i not in unique_list:
            unique_list.append(i)
# print the unique list
    return unique_list


# Test code
my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list) # get_unique_list is the function being called
print(unique_list)