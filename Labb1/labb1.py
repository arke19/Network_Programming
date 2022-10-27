import hello
import random

print(
"""1.3.1 Test questions on number
Question 1 and 2

You will always get a float from the /-operator unless you typecast to int.

How to get a int div? 
You could use floor division (//-operator) which will give you a int
""")
print("div 1.0/1 = " + str(type(1.0/1)))
print("div 1/1 = " + str(type(1/1)))
print("div int(1/1) = " + str(type(int(1/1))))
print("div (1//1) = " + str(type(1//1)))
print("")

print("Question 3")
print("2**-1 == " + str(2**-1)) 
print("")


print("1.3.2 Test questions on Strings")
print("""
Question 1
15*spam will print the word spam 15 times""")
print(15*"spam")
print()
print("""
Question 2
To get multiple lines put three double quotes""")
print("""
Question 3
To use citations you need to use a single 'quote' if you use double quotes to make your string
"""'''Same goes for double "quotes" if you use single quotes''')

print("""
Question 4
4a) == Hello
4b) == Hello
4c) == !
""")

print("""
Question 5
you use the len(string) function""")

print("""
Question 6
test='cow'
test[0] = 'chicken'
will give error
TypeError: 'str' object does not support item assignment

""")


print("1.3.3 Test questions on Lists")
print("""Question 1
r = a == [99, 1, 2, 3, 4, 5, 6, 7]
s = [100, 1, 2]
t = [100, 1, 2, 3, 4, 5, 6, 7]
If x = y is used the x variable will refer to the same object as y""")
print("""Question 2
You use the len(list) function""")

print("""Question 3
m[1][0] will call the second list and the first element of that list.
So if m = [[1, 2], [3, 4]]  ->   m[1][0] == 3
""")


print("1.3.4 Test questions on First steps")
print("""Question 1
a,b = b,a Will swap a and b pointers to each other
""")
print("Questions 2")
i = 1
while i < 10:
    print(i)
    i += 1


print("1.4 More Control Flow Tools")

print("""1.4.1 Test questions on the if-statements
Question 1
Python you elif instead of else if because they want a single word to present the statement, its for convienience i find it dumb.
It also makes it so there's less indentation""")

print("1.4.2 for-statement")
animals = ["dog","cat","elephant"]
for animal in animals:
    print(animal)


print("1.4.3 range() function")
print("Question 1")
for i in range(0,100):
    print(i)

print("question 2")
lista = [0] * 100
for i in range(100):
    lista[i] = i
    print(lista[i])

print("""1.4.4 break, continue, else
Question 1
The else-branch is executed when the for-loop isnt called or the if-statement part was met and no break was found""")
for i in range(10):
    print(i)
    if i > 4:
        break
else:
    print("else-called")

print("""1.4.5 Test Question empty statement
Question 1
Put a 'pass' call in the statement and it will be 'empty'""")


print("""1.4.6""")
def parrot_print(n):
    for i in n:
        print("Parrot")

animals.append('flea')
print(animals)

print("""1.4.7 More on defining functions""")

def print_all(self):
    print(self)
print("f = labmda a,b: a+b -> f(3,2) == 5")


print(hello.__doc__)
print(hello.hello_world.__doc__)


print("""
1.4.8 intermezzo: coding style
it doenst matter aslong as the indentation is concurrent, one tabulation == 4 spaces. I prefer tabs because im not a degenerate
It would count as 4 spaces in VSC""")

def sort_list():
    list = [2, 1, 5, 3, 4, 4]
    list.sort()
    print(list)

def pop_list():
    stack = [2, 1, 5, 3, 4, 4]
    stack.append(7)
    stack.pop(0)
    stack.pop(0)
    print(stack)
def power_of():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    b = [2**x for x in a]
    return b

def touple_test():
    t = 1111, 2222, 3333
    x, y, z = t
    return x, y, z

def set_test(n):
    correctAnsw = {"yes", "yeah", "jop", "ok"}
    answ = {"you answered yes" for x in correctAnsw if x is n} or {"you answered no" for x in correctAnsw if x is not n}
    print(answ)

#set_test("yes")

def convert_string_to_set(n):
    str = n
    print(str)
    s1 = {x for x in n}
    print(s1)

#convert_string_to_set("Tjabba")

def convert_list_to_set(n):
    lista = n
    print(lista)
    s1 = {x for x in n}
    print(s1)

#convertListToSet(["Hejsan", 12, 'Ja'])

def print_all_list_elements(n):
    for x in n:
        print(x)

#printAllListElements(["Hej", 345789, 123, [12, 32, "asdfg"]])

def print_all_dict_elements(n):
    for x, y in n.items():
        print(x, y)

#printAllDictElements({'a':12, 'b':62, 'c':"abc"})

def check_age(age):
    if 20 <= age <= 65:
        print("vad jobbar du med?")
        
#checkAge(20)

def get_lotto():
    s1 = {0, 0, 0, 0, 0, 0, 0}
    for x in range(7):
        s1.add(random.randint(1, 35))
    print(s1)

