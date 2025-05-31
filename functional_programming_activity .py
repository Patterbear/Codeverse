def my_map(items, function):
    output = []
    
    for item in items:
        output.append(function(item))
    
    return output

def square(number):
    return number * number

def cube(number):
    return number * number * number

items = [1, 2, 3]

print(my_map(items, square))
print(my_map(items, cube))
