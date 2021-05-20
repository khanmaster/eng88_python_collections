# What are dictionaries?
# are structured as KEY = VALUE
# VALUE could be string, int, list
# Syntax {}

# student_1 = {
#     "name": " shahrukh",
#     "key": " value ",
#     "stream": "Cyber Security ", # string
#     "completed_lessons": 3, # int
#     "complete_lessons_names": ["variables", "operators", "data_collections"] # list
#
# }
# #print(student_1)
# print(student_1["name"])
# print(student_1["stream"])
# print(student_1["complete_lessons_names"][1]) # Name of the dict followed by the key then the index of the value you want to retrieve
# # display only OPERATORS FROM THE LIST INSIDE DICTIONARY -
# print(student_1.keys())
# print(student_1.values())


# Sets are data collection the difference is that they are UNORDERED
# Syntax name = {}

car_parts = {"wheels", "doors", "engine"}
print(car_parts)

# Can we add any new parts?
car_parts.add("windows")
print(car_parts)

# Can we remove an item
car_parts.discard("doors")
print(car_parts)

# Frozen sets they are like Tuples
frozen_set = ([1,3,5,6])
print(frozen_set)





