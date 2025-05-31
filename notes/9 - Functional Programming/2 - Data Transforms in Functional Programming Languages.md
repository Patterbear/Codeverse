What's a data transform?

A data transform is something where data changes from one form to another.

Let's take some examples. Let us say we have a list of numbers and we want a list of the squares of the numbers. First let's create a list:

`>>> l = [1, 2, 3, 4, 5]`

Now we will write a function that helps us create a list of squares:

```
>>> def get_squares_list(l):
...   squares_list = []
...   for num in l:
...     squares_list.append(num * num)
...   return squares_list
...
```

We now call it on our list `l`:

```
>>> get_squares_list(l)
[1, 4, 9, 16, 25]
>>>
```

Ok, what if we want cubes?

```
>>> def get_cubes_list(l):
...   cubes_list = []
...   for num in l:
...     cubes_list.append(num * num * num)
...   return cubes_list
...
```

Let us call it on our list `l`:

```
>>> get_cubes_list(l)
[1, 8, 27, 64, 125]
>>>
```

Ok, what if we want square roots?

```
>>> def get_sqrt_list(l):
...   from math import sqrt
...   sqrt_list = []
...   for num in l:
...     sqrt_list.append(sqrt(num))
...   return sqrt_list
...
```

Let us call it on our list `l`:

```
>>> get_sqrt_list(l)
[1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979]
>>>
```

Is there anything that we are doing in common in all the above cases?

If you observe carefully, what we are doing is, we are passing an input list to the function. The function is then creating another list (let's call it output_list). It then takes each input element (say item) and runs some function, let's call it f on the item and then appends the result of f to the output_list. It then returns the output_list

In the case of squares, the function is square, in the case of cubes, it's the cube function and in the case of square roots, it's the square root function (sqrt).

Can we build a generic function to do this? We can! Introducing you to the first data transform function, the `map`.

# map

A map function takes a list as input and a function (say f) as input and applies the function f on each input item. The return value of the function f is added to the output list. This list is then returned. Remember map function if you see a requirement to convert n input items to corresponding n output items.

A map function that returns a list of squares of the input numbers:

```
.---.---.---.---.---.
| 1 | 2 | 3 | 4 | 5 |
'---'---'---'---'---'
  |   |   |   |   |
  v   v   v   v   v
  f   f   f   f   f
  |   |   |   |   |
  v   v   v   v   v
.---.---.---.---.----.
| 1 | 4 | 9 | 16| 25 |
'---'---'---'---'----'
```

# filter

A filter function takes a list as input and a function (say f) as input and applies the function f on each input item. If the function f returns True, the item is added to the output list. If the function returns False, it's ignored. Remember filter function if you see a requirement where you have n input items and you need a subset of the n items based on a condition.

A filter function which returns only the odd numbers in the list:

```
.---.---.---.---.---.
| 1 | 2 | 3 | 4 | 5 |
'---'---'---'---'---'
  |   |   |   |   |
  v   v   v   v   v
  f   f   f   f   f
  |       |       |
  v       v       v
.------.------.-----.
|  1   |  3   |  5  |
'------'------'-----'
```
# reduce

A reduce function takes a list as input and a function (say f) as input. It then takes 2 items at a time. Initially, it takes the first 2 items of the input list and applies the function f on it. Needless to say, the function passed to reduce should take accept 2 parameters. The next reduce application takes this value and the next value in the list. Remember reduce function if you see a requirement where you have n input items and need to reduce it to 1.

A reduce function which returns the sum of the numbers in the list:

```
.---.---.---.---.---.
| 1 | 2 | 3 | 4 | 5 |
'---'---'---'---'---'
  |   |   |   |   |
  |   |   |   |   |
  '>f<'   |   |   |
    |     |   |   |
    3->f<-'   |   |
       |      |   |
       6-->f<-'   |
           |      |
           10-->f<'
                |
                |
                v
                15
```