# Definition

A higher-order function is a function that does at least one of the following:

- takes one or more functions as arguments (i.e., procedural parameters),
- returns a function as its result.

[Source](https://en.wikipedia.org/wiki/Higher-order_function)

# Advantages

1. Improves code readability and re-usability.
2. Provides higher level of abstraction.
3. Helps in writing code using functional programming paradigm.

# Case study

Consider an example of a function which takes a list of numbers and returns a new list with the squares of each of the numbers given in the input list. Let us call the above function as square

```
function square (numbers[]) {
    result = [];
    foreach(number in numbers) {
        result.push(number * number);
    }
    return result;
}
square([1,2,3,4,5]);
```

Now let us say that given a list of numbers, we want a new list with cubes of each of the numbers given in the input list. This can be done as follows

```
function cube (numbers[]) {
    result = [];
    foreach(number in numbers) {
        result.push(number * number * number);
    }
    return result;
}
cube([1,2,3,4,5]);
```

This can be followed for fourth power, fifth power and so on.

A better approach could be followed by using a higher level of abstraction. Let us make use of higher order functions. Consider the following code snippet

```
function higher_order_function_demo (numbers[], function) {
    result = [];
    foreach(number in numbers) {
        result.push(function(number));
    }
    return result;
}
higher_order_function_demo([1,2,3,4,5], square);
higher_order_function_demo([1,2,3,4,5], cube);
```

The above function takes a list of numbers and a function as an input. It executes the input function for each number in the input list and constructs the result.

Thus, now we can pass any input function, i.e., power of 2,3,4 and so on and obtain the required result while maintaining the higher level of abstraction, code readability and re-usability.