
# Serialization
# Python provides built-in JSON libraries to encode and decode JSON.
# In order to use the json module, it must first be imported:
# import json

# there are two basic formats for JSON data. Either in a string or the object datastructure. 
# The object datastructure, in Python, consists of lists and dictionaries nested inside each other. 
# The object datastructure allows one to use python methods (for lists and dictionaries) to add, list, 
# search and remove elements from the datastructure. 
# The String format is mainly used to pass the data into another program or load into a datastructure.

# To load JSON back to a data structure, use the "loads" method. 
# import json 
# print(json.loads(json_string))

# To encode a data structure to JSON, use the "dumps" method. This method takes an object and returns a String:
# import json
# json_string = json.dumps([1, 2, 3, "a", "b", "c"])
# print(json_string)

# Python supports a Python proprietary data serialization method called pickle (and a faster alternative called cPickle).
# You can use it exactly the same way.
# import pickle
# pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
# print(pickle.loads(pickled_string))

# exercise
# The aim of this exercise is to print out the JSON string with key-value pair "Me" : 800 added to it.
import json
def add_employee(salaries_json, name, salary):
    salaries_object = json.loads(salaries_json)    
    salaries_object[name] = salary
    return  json.dumps(salaries_object)
# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries_json=salaries, name="Me", salary=800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])
