## using 'if-esle' statements with in functions allow you to control the flow of logic based on
## the conditoins.

## Example:

def main(num):
    if num > 0 :
        return 'positive'
    elif num < 0 :
        return 'negative'
    else:
        return 'zero'
print(main(5));
print(main(-5));
print(main(0));

## if-else with multipule conditions

def main(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
print(main(99));


## if-else woith logical operators like and, or, not

def get_age(age):
    if age < 0:
        return 'Invalid age'
    elif age <= 12:
        return "Child"
    elif age <= 18:
        return 'Teenager'
    elif age <= 65:
        return "Adult"
    else:
        return "Senire Citizen"
print(get_age(15))
print(get_age(20))


## Positional arguments:

## positonal arguments are the most common and straightforward way to pass arguments to a function.

def main(a,b):
    return a + b
Result = main(2,4);
print(Result)


## multi positional arguments:

## you can pass multiple arguments to a function by separating them with commas.

def Details(name,age,city):
    return f"mt name is {name}, my age is {age} and my city is {city}"

Person_Details= Details('Ashok',25,'Melbourne');
print(Person_Details);


## positonal arguments combine with default arguments:

## you can combine positional arguments with default arguments in function.

def wishes(name, message = 'good moring'):
    return f'{message}, my name is {name}'
greeting = wishes('Ashok','good afternoon')
print(greeting)


## note : in this case the default is good moring. 
## if we are not passing any value to the message parameter, it will use the default value.
## in this case we are passing 'good afternoon' as the second argument.