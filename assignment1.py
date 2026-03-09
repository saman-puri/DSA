1
'''
word = input()
#print("".join(sorted(word)))
'''

2
'''
a = int(input())
b = int(input())
print(f"{a} + {b} is {a+b}")
print(f"{a} - {b} is {a-b}")
print(f"{a} * {b} is {a*b}")
print(f"{a} / {b} is {a/b}")
print(f"{a} % {b} is {a%b}")
print(f"{a} ^ {b} is {a**b}")
'''

3
'''
n = int(input())

square = {}

for num in range(1, n+1 ):
    square[num] = num * num 
print(square)
'''

4
'''
num = int(input())
print(f"The sum of the first {num} positive integers is {num*(num+1)//2}")
'''

5
'''
a = input().lower()
counter = 0
for ch in a:
    if ch in ("a","e","i","o","u"):
        counter += 1
print(f"Number of vowels: {counter}")
'''

6
'''
sum = 0
while True:
    try:
        num = input()
        num = float(num)
        if num == 0:
            print(f"The grand total is {sum}")
            break
        else:
            sum += num
            print(f"The total is now {sum}")
    except:
        print(f"That wasn’t a number.")
'''

7
'''
def custom_encoder(text):
    ref ="abcdefghijklmnopqrstuvwxyz"
    result = []
    
    for char in text:
        lower_char =char.lower()
        
        if lower_char in ref:
            position = ref.find(lower_char)
            result.append(position)
        else:
            result.append(-1)
    return result
'''

8
'''
class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, my name is {self.name}")
'''

9
'''
class Restaurant:
    def __init__(self,restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"{self.name} serves wonderful {self.cuisine_type}.")
        
    def open_restaurant(self):
        print(f"{self.name} is open. Come on in!")
'''

10
'''
class User:
    def __init__(self,first_name,last_name,username,email,location):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.location = location 
        
    def describe_user(self):
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}")
        
    def greet_user(self):
        print(f"Welcome back {self.username}!")
'''

11
'''
def combine_lists(list1, list2):
    result = []
    i = 0
    j = 0 
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i +=1
        else:
            result.append(list2[j])
            j+=1
            
    while i < len(list1):
        result.append(list1[i])
        i +=1
    
    while j < len(list2):
        result.append(list2[j])
        j +=1
    
    return result
'''