"""
each key is unique and can be used to easily store or retrieve values 
(any data-type including string, int, float, list)

Dictionaries are indexed by keys 
(any immutable type - numbers, string, tuple)
as compared to lists which are indexed by a range of numbers
"""
# d = {1: "5"}
# d = {"a": 4}
# d = {(1, "hi"): 8}

# print(d.get(1))
# print(d.get(5))

# d[8] = 78
# d[1] = 7
# d["ky"] = 8

# print(d)

# d.update({1: 2})
# d.update([("name", 'Ed'), ('yr', 15)])
# d.update(unit="hit137", s=1)

# print(d)

"""
pop(key[, default]) method can be used to remove a key: value pair.
"""
# d.pop("name")
# print(d)

"""
popitem() can be used to destructively iterate over a dictionary 
removing and returning a (key, value) pair in LIFO (Last Item First Out) order
"""
# d = {"a": 4}
# d.update([("name", 'Ed'), ('yr', 15)])
# print(d)

# d.popitem()
# print(d)

# d.popitem()
# print(d)

# d.update({"name": "py"})
# print(d)

# d.popitem()
# print(d)

"""
The | (union) operator can be used to merge two dictionaries
"""
# d = {"yr": 20, 18: True}
# n = {"name": "Ed"}
# print(d | n)

# d |= n
# print(d)

"""
for loop can be used to directly iterate over the keys of a dict
"""
# d = {"yr": 20, "name": "Ed", 18: True}
# for key in d:
#     print(key,":", d[key])

# d["yr"] = 80
# print(d)

# d["trdf"] = "hi"
# print(d)

# d.keys()
# d.values()
# d.items()

# d = {"yr": 20, "name": "Ed", 18: True}
# for key, value in d.items():
#     print(key,":", value)




# def adder(f, s, t=None):
#     """
#     Returns the sum of f, s and t.
#     If t is not provided, 
#     return the sum of f and s. 
#     """
#     s = f + s
#     if t:
#         s += t
#     return s

# fst = 20
# snd = 10
# trd = 10
# # sm1 = adder(fst, snd, trd)
# sm2 = adder(fst, snd)
# print(sm2)


# local var
# def triple(a):
#     result = 3 * a
#     # variable result 
#     # is accessible locally
#     print("local:", result)

# Outputs value of result
# inside the function 
# triple(3)

# Throws an error as result is 
# not accessible outside the scope 
# of function triple()
# print("outside:", result)


# # golabl var
# n = 10

# def uno():
#   print(n)

# def tres():
#   print(n*3)

# uno()
# tres()


# ################
# n = 10

# # local n inside the
# # function
# def uno():
#   n = 5
#   print(n)

# # global n inside the
# # function
# def tres():
#   print(n*3)

# uno()
# tres()


# ##########

# n = 10

# # function modifies the 
# # value of global n
# def uno():
#   global n
#   n = 5
#   print(n)

# def tres():
#   print(n*3)

# uno()
# tres()


# """
# When mutable objects (list, dict) are provided as an argument to a function, 
# any modification made to the corresponding parameters in the body of the function 
# leads to the modification of the original object
# """
# def repeat(l):
#     for i in range(len(l)):
#         l[i] = l[i]*2

# l = [1, 2, 3]
# print(l)
# repeat(l)
# # l is modified
# print(l)


# Q1
def sum_list(data):
    total = 0
    for num in data:
        total += num
    return total

# print(sum_list([1, 8, 9]))

# Q2:
def sum_range(low, high):
    # res = 0

    # for i in range(low, high + 1):
    #     res += i
    # return res

    return sum(range(low, high + 1))

# print(sum_range(1, 5))  # Output: 15


# # # Q3
def modify_dict(data):
    # Replace value at key "b" with its negation
    data["b"] = -data["b"]
    
    # Add key-value pair "c": 40
    data["c"] = 40
    
    # Remove key "b"
    a = data.pop("b", None)
    
    # Print keys in alphabetical order
    print(sorted(data.keys()))

data = {"b":20, "a":35}

# # Q4
def find_smallest(numbers):
    min_num = numbers[0]

    for num in numbers:
       if min_num > num:
          min_num = num

    return min_num

# print(find_smallest([7, 2, 1, 4, 5]))
min([])

# # Q5
def concat_dictionaries(dict1, dict2, dict3):
    return dict1 | dict2 | dict3

dic1={1:10, 2:20}
dic2={3:30, 2:40}
dic3={5:50,6:60}

print(concat_dictionaries(dic1,dic2,dic3))