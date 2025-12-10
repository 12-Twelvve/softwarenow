# Assume that the variable data refers to the dictionary {“b”:20, “a”:35}. Write the
# expressions that perform the following tasks:
# a. Replace the value at the key “b” in data with that value’s negation.
# b. Add the key/value pair “c”:40 to data.
# c. Remove the value at key “b” in data, safely.
# d. Print the keys in data in alphabetical order

data = {"b":20, "a":35}

# a
data['b'] = - data['b']
# b
data['c'] = 40
# c
data.pop('b', "NA")
# d
print(sorted(data.keys()))