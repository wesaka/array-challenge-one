# Take the raw input and remove all whitespace immediately
raw = input().replace(' ', '')

# Split at the last comma, that denominates where the array ends and where the number to be added starts
# I tought about doing this in multiple lines, but felt that this one liner wasn't too complex to understand,
# As I am just getting the array from before the last comma in the input,
# Joining the iterator returned with the digits into a string to be converted into an int
number = int(''.join(filter(str.isdigit, raw[:raw.rfind(',')])))
add = int(raw[raw.rfind(',') + 1:])

# For this first part, we don't care about the first array being a proper array;
# We care only for the number, so we just add both
final_number = number + add

# Then, split and output as array
print([int(i) for i in str(number + add)])