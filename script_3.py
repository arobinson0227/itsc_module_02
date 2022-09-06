# Allow the user to input a string
user_input = input('Enter a string: ')
# Create a function that returns a dict and keeps track of each letter in the string
def char_count(user_input):
    dict = {}
    for i in user_input:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict

print(char_count(user_input))
