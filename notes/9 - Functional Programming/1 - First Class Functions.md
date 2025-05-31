# First Class Functions

What's a first class citizen?

Let us take "Numbers" as an example to understand the concept of First Class Citizens. Numbers are first class in all languages.

For something to classify as a first class citizen, it has to satisfy 3 conditions:

1. You should be able to assign it to a variable. Eg: `x = 20`
2. You should be able to pass it to a function. Eg: `foo(20)`
3. You should be able to return it from a function. Eg: `return 20`

We see that Numbers satisfy all these conditions, hence they are first class citizens.

In functional languages, functions are also first class. What does that mean?

Let us look at each condition separately:

# Assigning to variables

1. You can assign it to a variable. We will take the example of a language like Python just to explain the concept. You don't need prior understanding of Python to understand these concepts. We choose Python because it has very simple syntax and is functional.

In a language like Python, what does it mean to assign something to a variable? Example:

`x = y`

What this means is, x is a reference to the same location as what y is referencing.

Ok, so what happens when you define a function:

```
>>> def foo():
...   return 10
...

```

Defining a function creates an object in memory to hold the function definition. foo is then a variable that references this object. This is no different conceptually from what happens when you create any variable and initialize it with a value (eg: `x = 20`).

Now combining the above ideas, let us see what happens when we run the following piece of code:

```
>>> def foo():
...   return 10
...
>>> x = foo
>>> type(x)
<type 'function'>
>>> x()
10
>>>
```

A function object gets created. foo is a variable that points to this function definition. When we say x = foo, we are just saying, let x be a second reference to the same object as what foo is referencing. foo is referencing a function, so also happens to reference the same function. If a variable references a function, you can call it. That's what we are doing next.

Please note that this is very different from saying:

x = foo()

The above notion exists in all languages including non-functional languages. Here we are saying, "call foo" and the return value of foo should be assigned to x. This is very different from `x = foo`.

# Passing to functions

Once we get this basic idea of assigning functions to variables, the rest 2 conditions are easy to follow.

Consider this piece of code:

```
>>> def foo_caller(foo):
...   foo()
...
>>> def bar():
...   print('Bar')
...
>>> foo_caller(bar)
Bar
>>>
```

Let us understand this code, one step at a time. The first statement creates a function called foo_caller. In other words, it creates an object that holds the function definition, and then makes foo_caller a variable that references this function object.

Special note: Is foo created at this point in time? Remember that the function arguments don't get created unless the function is called, so no. foo is not created yet. foo is created only when foo_caller is called. foo is created as many times as foo_caller is called.

The next statement is similar. A function object gets created and bar is a variable that references it.

The next statement is magical: `foo_caller(bar)`. This means, execute the body of foo_caller by passing a reference of bar to it.

Let us understand this better. Examine this simple function:

```
>>> def sum(x, y):
...   return x + y
...
>>> a = 10
>>> b = 20
>>> sum(a, b)
30
>>>
```
What happens when we say sum(a, b). We are saying, execute the body of sum. Pass the references of a and b to it as arguments. The arguments are received as parameters x and y. It's as good as saying:

```
x = a
y = b
```

Isn't it?

And we know what that means! x = a means let x be a second reference to the object that a is referencing.

So now coming back to our foo_caller function: `foo_caller(bar)`. We are saying, execute the body of foo_caller and pass bar to it. This is received as the parameter foo. It's as good as saying:

`foo = bar`

Let foo be a second reference to what bar is referencing. We know what bar is referencing. It's a function. foo now becomes a second reference to the same function.

When we execute the body of foo_caller, we are just asking it to execute the body of foo. This is nothing but the body of bar.

# Returning functions from functions

This is the final case of first class functions.

Consider this piece of code:

```
>>> def foo():
...   def bar():
...     print('Bar')
...   return bar
...
>>> x = foo()
>>> x()
Bar
>>>
```

We already know most of it. But let's look at them one statement at a time.

After executing the first statement, the function object gets created and foo is a reference to it. Remember that bar is not yet created. bar is created only if foo is called. The next statement is saying, call foo. We execute the body of foo and the return value of foo is assigned to x. What happens when we execute the body of foo? A function object gets created and bar is a reference to it. This reference is then returned. This returned reference is received as x.

This is similar to the following:

```
>>> def get_x():
...   x = 10
...   return x
...
>>> y = get_x()
>>> y
10
>>>
```

See that? Return value of get_x is assigned to y. That's as good as saying:

`y = x`

Similarly, the above is doing:

`x = bar`

We know what that means! x becomes a second reference to the object that bar is referencing. bar is referencing a function, so x happens to reference the same function. So when x is called, it's just calling the same function as bar. That prints "Bar".

Read more about functions as first class objects here: [https://en.wikipedia.org/wiki/First-class_function](https://en.wikipedia.org/wiki/First-class_function)