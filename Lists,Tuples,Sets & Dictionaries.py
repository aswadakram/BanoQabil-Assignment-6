#Sum of all the numbers in the list
my_list = [10, 20, 30, 40, 55]
def sum_of_list(numbers):
    return sum(numbers) #The sum function is a predefined function that returns the sum of all elements.

result = sum_of_list(my_list)
print("Sum of all the numbers in the list is:",result) #Output: 155



#Smallest Number in Tuple
tuple = (9, 7, 9, 2, 6)
def smallest_in_tuple(numbers):
    return min(numbers) #The min function is a predefined function that returns the smallest element.

result = smallest_in_tuple(tuple)
print("Smallest number in the tuple is:",result) #Output: 2



#Square of the Set
set = {2, 3, 4, 5, 6}
def square_of_set(numbers):
    return {x*x for x in numbers}

result = square_of_set(set)  
print("Square of the set is:", result) #Output: {4, 36, 9, 16, 25}



#List of all the Keys in the dictionary
dict = {
    "name": "introvert",
    "psychopath": True,
    "age": 18
}
def keys_of_dictionary(dictionary):
    return list(dictionary.keys())

result = keys_of_dictionary(dict)
print("List of the keys in the dictionary is:", result) #Output: ['name', 'psychopath', 'age']