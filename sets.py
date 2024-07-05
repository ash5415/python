## sets
## A set is a collection which is unordered and unindexed. they are written with curly brackets.
## the elements in the set are unordered, unchangeable, and do not allow duplicate values.
## the elements in the set are unordered, unchangeable, and do not allow duplicate values.

## examples:

store1 = {'apple', 'orange', 'banana', 'grapes'};
store2 = {'apple', 'orange', 'banana', 'grapes','rockmelon'};

store1.add('mango')   ## adding an elements to the set 

store1.remove('mango')  ## removing an elements from the set

total = store1.union(store2);           ##  what are all the products in the sotres

common = store1.intersection(store2);   ## what are the common producuts in the stores

dif= store2.difference(store1);      ## what are the different products in the stores

print(dif)
print(common);
print(total)
print(store1);
print(store2); 
print(type(store1));


x = input()    ## the input function is used to take input from the user that inputs a string.
10             ## the value 10 is nothing but input by the user
print(x);      ## the value is convert into string.
print(type(x));


x = int(input());    ## here the input value convert into integer
10
print(x);
print(type(x));

x = float(input());    ## here the input value convert into float.
10
print(x);
print(type(x));

## eval is function that is only works for numbers


x = eval(input());    ## here the input value convert into float. here the input is a string. that is a number.
10                    ## here the input value convert into integer with the help of eval function.
print(x);
print(type(x));


## Note: eval only works for numbers like int,flot and complex numbers not work for strings. when you pass
## a string value to the eval function it will give you an error.


