set = {"apple", "banana", "cherry"}
print(set)

set1 = {"apple", "banana", "cherry", "apple"}
print(set1)

thisset = {"apple", True, 1, 2}
print(thisset)

thisset = {"banana", "cherry", False, True, 0}
print(thisset)

set2 = {"apple", "banana", "cherry", 1,2,3,4,5,6,7,8}
print(len(set2))

set3 = {"abcdefghi", 76, True, 99, "female"}
print(set3)

myset = {"apple", "banana", "cherry"}
print(type(myset))

thisdict = {
  "brand": "Tesla",
  "model": "Roadster",
  "year": 2008
}
print(thisdict)

thisdict = {
  "brand": "Tesla",
  "model": "Roadster",
  "year": 2008
}
print(thisdict["brand"])

thisdict = {
  "brand": "Tesla",
  "model": "Roadster",
  "year": 2008,
  "year": 2012
}
print(thisdict)

thisdict = {
  "brand": "Tesla",
  "model": "Roadster",
  "year": 2008
}
print(len(thisdict))

thisdict = {
  "brand": "Tesla",
  "electric": True,
  "year": 2008,
  "colors": ["black","red", "white", "blue","grey"]
}
print(thisdict)

# '''
# key value pairs
# unordered unchangeable duplicates not allowed SETS
# ordered changeable duplicates are not allowed DICT
# '''

input_dict = {'a': 100, 'b': 200, 'c': 300}
total_sum = sum(input_dict.values())
print("Sum of all items in the dictionary:", total_sum)

input_dict = {'a': 100, 'b': 200, 'c': 300}
dict_size = len(input_dict)
print("Size of the dictionary:", dict_size)

