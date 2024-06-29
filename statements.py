## if statement  is ony works for one condition.

def main():
    x = eval(input())
    y = eval(input())

    if x > y :
       print('x is bigger')
main()

## if else statement is works for multipule condition.

def main():
    x = eval(input());
    y = eval(input());
    
    if x > y :
        print('x is bigger')
    else:
        print('y is bigger')
main()

## while loop is used to execute a block of code as long as the condition is true.

    ## whileloop is always following 3 things 
    ## 1. initialization
    ## 2. condition
    ## 3. increment or decrement
## example:
def main():
    x = 10;                 ## initinal value
    while x <= 20:           ## termaniation condition
        print(x);
        x = x +1;           ## step value
main()


## for loop is used to execute a block of code a fixed number of times.
## In Python, a for loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) or any other iterable object. 
## The basic syntax of a for loop is:

## example:

def main():
    x = [1,2,3,4,5,6,7,8,9];
    for i in x:
        print(i);
main()