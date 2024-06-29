## example of variable change

# Integer variable
age = 30
print(age)  # 30

# String variable
name = "Alice"
print(name)  # Alice

# Float variable
price = 19.99
print(price)  # 19.99

# Boolean variable
is_member = True
print(is_member)  # True

# List variable
colors = ["red", "green", "blue"]
print(colors)  # ['red', 'green', 'blue']

# Dictionary variable
person = {"name": "John", "age": 30}
print(person)  # {'name': 'John', 'age': 30}





### In Python, operators are special symbols or keywords that perform operations on values and variables. 
###Here is a breakdown of the different types of operators


# Arithmetic Operators  like +, -, *, /, %, **, //

## examples
## addition
x = 10;
y = 20;
Result = x + y;
print(Result);
print(type(Result));

## subtraction

x = 10;
y = 20;
Result = x - y;
print(Result);
print(type(Result));

## multiplication

x = 10;
y = 20;
Result = x * y;
print(Result);
print(type(Result));

## division

x = 10;
y = 20;
Result = x / y;
print(Result);
print(type(Result));

## modulus

x = 10;
y = 20;
Result = x % y;
print(Result);
print(type(Result));

## power

x = 10;
y = 20;
Result = x ** y;
print(Result);
print(type(Result));

## floor division

x = 10;
y = 20;
Result = x // y;
print(Result);
print(type(Result));

##Comparison Operators for comparing two values like ==, !=, >, <, >=, <=
## Equal to

x = 10;
y = 20;
Result = x == y;
print(Result);
print(type(Result));


## Not equal to

x =10;
y =20;
Result = x != y;
print(Result);
print(type(Result));

## Greater than

x = 10;
y = 20;
Result = x > y;
print(Result);
print(type(Result));

## Less than

x = 10;
y = 20;
Result = x < y;
print(Result);
print(type(Result));

## Greater than or equal to

x = 10;
y = 20;
Result = x >= y;
print(Result);
print(type(Result));

## Less than or equal to

x = 10;
y = 20;
Result = x <= y;
print(Result);
print(type(Result));

## Logical Operators for combining conditional statements like and, or, not

## Logical AND

x = True;
y = False;
Result = x and y;
print(Result);
print(type(Result));

## Logical OR

x = True;
y = False;
Result = x or y;
print(Result);
print(type(Result));

## Logical NOT

x = True;
y = False;
Result = not x;
print(Result);
print(type(Result));

## identity operaror
## identity operator is used to compare the memory location of two objects.
## IS  and is not

##example:  

x = 10;
y = 10;
print (x is y);  

### Example 2: Different objects in memory
x = [10,20,30];
y = [10,20,30];
print( x is y);     ### x and y point to different list objects with the same content


## IS NOT     

x = 20;
y = 30;
print( x is not y);


## Membership Operators for checking whether a value is present in a sequence like in, not in
## Using in Operator

fruits = ["apple", "banana", "cherry"];
print("apple" in fruits);
print ('orange' in fruits);


# Example with string
text = "hello world"
print("hello" in text)  # Output: True
print("world" in text)  # Output: True
print("Python" in text)  # Output: False

# Example with tuple
numbers = (1, 2, 3, 4, 5)
print(3 in numbers)  # Output: True
print(6 in numbers)  # Output: False

# Example with dictionary (checks keys)
person = {"name": "Alice", "age": 25}
print("name" in person)  # Output: True
print("address" in person)  # Output: False


## Using not in Operator

fruits = ["apple", "banana", "cherry"];
print("apple" not in fruits);     ## output : False
print ('orange' not in fruits);   ## output : True



# Practical Use Cases
# Checking Elements in a List

shopping_list = ["milk", "bread", "eggs"]
item = "bread"

if item in shopping_list:
    print(f"{item} is in the shopping list.")
else:
    print(f"{item} is not in the shopping list.")
