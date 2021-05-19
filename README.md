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


```
### Tuples?
- Tuples are IMMUTABLE
 
