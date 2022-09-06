# initialize the sum of inputs the user will enter
sum = 0
for i in range(1,6):  # Allows for the user to input 5 integers
    while True: # the while loop will test if the inputs provided are true
        try: # try will test the inputs entered to allow an exception to be thrown if an invalid input is entered
            user_input = int(input('Enter int #{}: '.format(i)))
            sum += user_input # sum is the total of the user inputs added together
            break
        # you cannot assume that what the user enters is a valid input
        # throw an except ValueError to catch when a value that is not of the int type is inputted
        except ValueError: 
            print('Invalid input. Please enter an int.')
            continue # continue the loop and ask the user to enter a new int again

print('Your sum is ', sum)