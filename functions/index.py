## today the topic is Function in python 
## there are different types of function is therein python
## Example:

# def main():
#     print('helop world')
# main()

def main(a,b):
    result = a + b
    if result > 0:
        return "positive"
    elif result < 0:
        return "negative"
    else:
        return 'zero'

a = main(2,3);
print(a);


## positional argument and keyword argument
## positiomnal arguments are the arguments that need to be passed to a funcrion 
## in the correct order.

### example: a function with positional arguments except value to be passed in A specific order.


def main(a,b):
    result = a + b
    if result > 0:
        return 'posiver'
    elif result < 0:
        return 'negative'
    else:
        return 'zero'
main(2,3);


def main(name):
    return f'Hello my name is {name}'
main():