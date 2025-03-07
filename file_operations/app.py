

## file operations
## fiel operartions in python involve various methods and funcitons to Read, write, append and delete 
## multipule files. 
## 'r' : Read (default). Opens a file for reading.
## 'w' : Write. Opens a file for writing (creates a new file or truncates the existing file).
## 'a' : Append. Opens a file for appending (writes to the end of the file if it exists).
## 'b' : Binary mode. Used with other modes for binary files (e.g., 'rb' or 'wb').
## 't' : Text mode (default). Used with other modes for text files (e.g., 'rt' or 'wt').


## Reading the file

Read = open('file.txt', 'r');
print(Read.tell());           ## tell the current position of the cursor

print(Read.read());           ## reading the file

print(Read.seek(5))           ## resetting the cursor to the begining of the file

print(Read.read())

##print(Read.close());        ## closeing the file
##Read.close();

## note: once you close the file hou can not read the the file again.......
## if you want you can read the file again you have to open the file again
## when you trying to writuing the existing file again the old content is gone!!!
## you have to open the file in append mode
## open file

w = open('file2.txt', 'w')
print(w.write('hello world'));
print(w.write('\nwriting the python file'))
w.close();

##  Appending the file :

w = open('file2.txt','a');
w.write('\n adding the new line i nthe file!!!!');
w.close();

## Note: if you wnat to read all the line of the file you have to open the file in read mode


w = open('file2.txt', 'r')

content  = w.readline()
while content:
    print(content);
    content = w.readline();


## file existing other operations

import os;

print(os.path.exists('file2.txt'));
print(os.path.isfile('file2.txt'));
print(os.path.isdir('file2.txt'));

## checking the file 

if os.path.exists('file2.txt'):
    print('file2 is exitsted!!!')
else:
    print('file2 is not existed@@@');


## Deleting the file

if os.path.exists('file2.txt'):
    os.remove('file2.txt');
    print('file2 is deleted successfully!!!!!!')
    

## hybrid modesin file operations

## Reading and writing (r+ and w+)

## r+ : open a file for both reading and writng. the file pointer is placed at the beginning of the file..

## w+: Opens a file for both reading and writing. If the file does not exist, it creates a new file. 
##     If the file exists, it truncates the file to zero length.
    

    
## example:    [Reading and writing]
    
second = open('file.txt', 'r+')
print(second.read());  
print(second.write('\nadding the new line r+ mode'))  
second.close();

## Appending and Reading :
## a+: Opens a file for both appending and reading. The file pointer is at the end of the file if it exists. 
##     The file is created if it does not exist. 

## example:

app = open('file2.txt', 'w')
app.write('welcome to the world!!!');
print(app);

## open file for appending Reading

app = open('file2.txt', 'a+')
app.write('\n adding the contect in to the file!!!')
print(app.read());
app.seek(5)
app.read()