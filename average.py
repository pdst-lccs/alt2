# Program to demonstrate mean, median and mode

# A function to return the arithmetic mean of all the values in L
def get_mean(L):

    # set the initial value of total to zero
    total = 0 # running total of values in L

    # Now loop over the list
    for v in L:
        total = total + v # running total

    # Divide by the total by the number of values in L
    return total/5

# A function to return the median of all the values in L
def get_median(L):
    # To find the median we need to sort the list
    L.sort() # the values are sorted 'in place'

    # The next step is to find the index of the middle value
    num_values = len(L)
    mid = num_values//2

    median = L[mid] # the median is in the middle
    
    return median

# A function to return the mode of all the values in L
def get_mode(L):

    # Build up a list of unique values
    unique_values = []
    for value in L:
        if value not in unique_values:
            unique_values.append(value)

    # Build up a list of frequencies
    frequencies = []
    for value in unique_values:
        frequency = L.count(value)
        frequencies.append(frequency)

    # Find the mode
    max_frequency = max(frequencies)
    max_frequency_pos = frequencies.index(max_frequency)
    mode = unique_values[max_frequency_pos]

    return mode

# Test driver code ....
my_list = [18, 16, 17, 18, 19, 18, 17]

# Call the functions
mean_value = get_mean(my_list)
median_value = get_median(my_list)
mode_value = get_mode(my_list)

# Display the answers
print("The mean is:", mean_value)
print("The median %.2f is the middle value" %median_value)
print("The mode is:", mode_value)

# TASKS FOR BREAKOUT

# Tasks for get_mean
# Modify the function get_mean so that it works for any number of values (not just 5)
# Modify the function get_mean to use sum instead of a loop

# Tasks for get_median
# Modify the function get_median so that it works for an even number of values

# Tasks for get_mode
# The statement list(set(L)) returns a list of unique elements in L.
# Use this information to replace the loop that builds the list of unique values
# This version of get_mode works for lists that have a single mode.
# Modify the function get_mode so that it ....
# - works if there is no mode e.g. L = [18, 16, 17, 21, 19, 16, 22]
# - works if there are multiple modes e.g. L = [18, 16, 17, 18, 17, 18, 17]
# Modify the program so that it can display the frequency of the mode(s)
