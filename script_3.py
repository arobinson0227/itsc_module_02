# Allow the user to input a string
user_input = input('Enter a string: ')
# Create a function that returns a dict and keeps track of each letter in the string
# https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php
def char_count(user_input): 
    dict = {} # Initializes the dict, which will store associations of key/value pairs (Lectue_02 from class, 08/29/22, Slide: Data Structures - Dictionaries(dicts))
    for i in user_input: # This iterates through each character in the inputted string
        keys = dict.keys() # Stores the characters in the string to values of the dict. 
        # Keys are most frequently used for strings (Lectue_02 from class, 08/29/22, Slide: Data Structures - Dictionaries(dicts))
        # Count the frequency of each letter as it appears in the string
        if i in keys: 
            dict[i] += 1 # Add one to the count as the value's frequency increases
        else:
            dict[i] = 1 # If the character value only appears once, the character's count equals 1
    return dict 

print(char_count(user_input)) # Prints the funtion created
