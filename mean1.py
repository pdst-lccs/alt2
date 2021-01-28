# Program to find the mean of a list of values
# Version 1
import statistics

# Calculate and return the mean of all the values in L
def arithmetic_mean(L):

    # set the initial value of total to zero
    total = 0 # running total of values in L

    # Now loop over the list
#    for v in L:
#        total = total + v # running total

    total = sum(L)
    
    # Divide by the total by the number of values in L
    return total/len(L)

# PYTHON STARTS EXECUTING FROM HERE ...

# Initialise a list of values
my_list = [18, 27, 15, 13, 22, 100, 200]
# Call the function
my_mean = arithmetic_mean(my_list)
my_mean2 = statistics.mean(my_list)

# Display the answer
print("The mean is ", my_mean)
print("The statistics package mean is ", my_mean2)

# TASKS FOR BREAKOUT
# Modify the code so that it works for any number of values (not just 5)
# Modify the code to use sum instead of a loop

# EXTENSIONS
# Ask can we get the mean of numbers entered by a user?
# Hint: You will need ask how many numbers the in advance or use a while loop and a sentinel.
# Ask can we get the mean of numbers from a text or csv file?

# EXPERIMENT ...
# Ask students how they know the program is working? (i.e. actual result vs. expected result)
# Change the values in the list and see what happens?
# What happens if there were more (or less) than 5 values in the list?
# Change the variable names as see what happens
# Does this program work for a list of strings (e.g. ["Mary", "Andy", "Pat"])? Why/why not?
