# Write a Python script to concatenate following dictionaries to create a new one
# Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 2:40}
dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

dic = {**dic1, **dic2, **dic3}
print(dic)

dict1 = {'gfg': 'a', 'is': 'b'}
dict2 = {'gfg': 'c', 'is': 'd'}
    
concatenated_values_dict = {key: dict1[key] + dict2.get(key, '') for key in dict1.keys()}
print(concatenated_values_dict)
