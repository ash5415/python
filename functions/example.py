## function in python are defined using keyword 'def'
## Example:
def message(name):
    return f"hell my name is {name}"

messaage = message('anil')
print(messaage);

## functional arguments:
## functions can take positional arguments, keyword arguments, and default arguments and 
## variable-length arguments.

## positional arguments:
## these afre the most common and straightforward way to pass arguments to a function.

## exampple:
  
def add(a,b):
    return a + b
result = add(2,4);
print(result);

## keyword arguments:
## you can specify the arguments by their names in the function call.

def main(name,age):
    return f"hello my name is {name} and my age is {age}"

result =main(name = 'ashok',age = 25)
print(result);

## Default arguments:
## you can specify default values for function arguments.

def main(name, message = 'hello'):
    return f'{message} my name is {name}'

Result = main('ashok')
print(Result);

result = main('Ashok', 'hello good evening')
print(result);


## lopcal variable vs global variable:

## local variables: local variables are defined inside a function and 
## can only be accessed within that function.

## Example

def main():
    x = 10;
    print(x)
main()

##print(x)  # this will give an error as x is local variable and can't be accessed outside the


## global variables: global variables are defined outside a function and can be accessed from anywhere in the program.
## example:
 
msg = 'good moring'
def main(a,b):
    result = a + b
    print(result,msg)
main(20,20)

## Lambda functions:
def squre(x):
    return x ** 2
main(squre,4)