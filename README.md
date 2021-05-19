# Python Data Collection
## What are Data collections

- Lists
- Tuples
- Dictionaries
- sets

### Lists are MUTABLE

```python
shopping_list = ["juice", "strawberries", "yogurt", "chicken", "rasberries", "butter"]
            #      0           1             2           3          4           5
print(shopping_list)
print(type(shopping_list))

print(shopping_list[2])
print(shopping_list[4])
print(shopping_list[-1])

# if we needed to replace something from the list
shopping_list[5] = "Oats"
print(shopping_list)

shopping_list.append("Mango") # append adds the item at the end of the list
print(shopping_list)

# To remove something from our shopping list we have method called remove
shopping_list.remove("Oats")
print(shopping_list)

shopping_list.pop() # pop() removes the last item from the list
print(shopping_list)

### Tuples?

```

- 

```python
# Tuples are IMMUTABLE
# Syntax name = ()
# use cases

essentials = ("eggs", "milk", "bread")
             #  0      1        2
print(essentials)

```
#### What are dictionaries?
- structured as KEY = VALUE
- VALUE could be string, int, list
- Syntax {}
```python
student_1 = {
    "name": " shahrukh",
    "key": " value ",
    "stream": "Cyber Security ", # string
    "completed_lessons": 3, # int
    "complete_lessons_names": ["variables", "operators", "data_collections"] # list

}
#print(student_1)
print(student_1["name"])
print(student_1["stream"])
print(student_1["complete_lessons_names"])
# display only OPERATORS FROM THE LIST INSIDE DICTIONARY -
print(student_1.keys())
print(student_1.values())

```