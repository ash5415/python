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

