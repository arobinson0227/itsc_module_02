# https://www.geeksforgeeks.org/python-combine-two-dictionary-adding-values-for-common-keys/

# Allow the user to input two strings as dicts
dict_1 = input('Enter a string: ')
dict_2 = input('Enter a string: ')

# Create a function that takes in the two dicts and compute a new dict which combines the two dicts by summing the values for the common keys
def get_combined_dict(dict_1, dict_2):
    combined_dict = {} # new dict
    # identify common keys between the two dicts
    for key in dict_2:
        if key in dict_1:
            # Add the common keys of the two dicts
            combined_dict[key] = dict_2[key] + dict_1[key] 
        else:
            pass # Skips over the uncommon dicts
    return combined_dict

# Test code:
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2) # get_combined_dict function is being called
print(combined_dict)
