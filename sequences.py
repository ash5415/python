## Sequences are ordered collections of items. 
## The most common sequence types are strings, lists, tuples, and ranges.

## strings

s = 'hello';

## acessing the elements in the string

print(s [0]);
print(s[1:4]);
print(s.upper());
print(s.lower());

## Lists are mutable sequences, typically used to store collections of homogeneous items.

x = [1, 2, 3, 4, 5];
print(x[0]);
print(x[0:2]);

## modifing theelementsi nthe list

x[0] = 10;
print(x[0]);
print(x);

## list methods

x.append(6);
print(x);
x.remove(6);
print(x);