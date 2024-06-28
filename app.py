## Advanced Data types
## Lists are ordered, mutable collections that can contain elements of different types.
x =[1,2,3,4,5,6,7,8,9,10];

print(x);
print(type(x));
print(x[0])
print(x[-1])
print(x[0:4]);

# modifing the list

x[0] =100;
print(x);

### list[start:stop:step]

my_list = [0, 1, 2, 3, 4, 5, 6]
slice_1 = my_list[1:4]
print(slice_1)  # Output: [1, 2, 3, 4]

## Tuples are ordered, immutable collections that can contain elements of different types.

set = (1,2,3,4,5,6,7,8,9,10);
print(set);
print(type(set));

## Dictionaries are unordered, mutable collections of key-value pairs, where keys are unique and immutable,

set = {'name': 'Ashok', 'age': 25, 'city': 'Bangal'};
print(set);
print(type(set))         ##  what type it is
print(set['name']);      ## accessing the individual elements
print(set['age']);
set['country'] = 'india'    ## adding a value 
print(set);

