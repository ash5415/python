def main():
    print('enter a number?')
    num = eval(input())
    if num > 0:
        print('+ve number')
    elif num < 0:
        print('-ve number')
    else:
        print('zero')
main()
 

def main(a,b):
    return a + b;
print(main(2,4))


def greet(name, message = 'good moring'):
    return f"{name}, {message}"
result = greet('anil') 
print(result)

def greeting(name, message = 'good evening'):
    return f'{name}, {message}'
result = greeting('Ashok')
print(result)


def main(x):
    print('please enter the numbers')
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"
##main(-4)
    
def check_number(num):
    if num > 0:
       return "Positive"
    elif num < 0:
        return "Negative"
    else:
      return "Zero"

# # Test the function
# print(check_number(10))  # Output: Positive
# print(check_number(-5))  # Output: Negative
# print(check_number(0))   # Output: Zero


def main(score):
    print('enter your score')
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