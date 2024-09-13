# userName= "chaicode"

# def func():
#     # userName="chai"
#     print(userName)

# print(userName)

# func()

# x=10
# def func2(y):
#     z=x+y
#     return z
# print(func2(1))

# x=10
# def func3():
#     global x //you should avoid practice. you can use global value but never modified it for best level
#     print("global",x)
#     x = 12
#     print("after updating",x)
# func3()
# print(x)



# Closures : A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
'https://www.learnpython.org/en/Closures#:~:text=A%20Closure%20is%20a%20function,are%20not%20present%20in%20memory.'

# [here, we in myResult declare f1 and call it line.40]
# [it is starting execute from line.34, line.35 and return f2's whole defination(means line.36 to line.38)]
x=100 #global 
def f1():
    x=200 #inner
    def f2():
        print(x)
        return "Akash"
    return f2       #here if we write "f2()" like this, then f2 will execute here
myResult = f1() #in myResult f2's whole defination is stored
# myResult()   #myResult is like myResult()==f2() // and we are calling here
print(myResult()) #here i ma chekcing by returning my name. and it works same as we call f2()

'same result'
# def transmit_to_space(message):
#   "This is the enclosing function"
#   def data_transmitter():
#       "The nested function"
#       print(message)
#   return data_transmitter

# fun2 = transmit_to_space("Burn the Sun!")
# fun2()

# ------------------------------------------
'leaving space so maintain line numbers in following code'

###line.67 declare f and called chaiCoder function with "2" and return whole "actual function defination line.65" //make sure not use parentheses (❌ actual())
##here, line.64 num value is what passed while calling line.67. means num=2 and that will inclues while returning line.65
#now f hold actual functions definiatio with references passed while returning

def chaiCoder(num):
    def actual(x):
        return x**num #'f 3**2' 'g 3**3'

f = chaiCoder(2) 
print(f) ###line.68 give whole addresses with refernece numer //<function chaiCoder.<locals>.actual at 0x7f6352b6d048>
print(f(3)) ## here, f holding actual function defination, so react like that so, we are giving argument and this will call line.63 and take parameter at its placeholder as "3"

g = chaiCoder(3)
print(g)
print(g(3))

# ----------------Above code
def chaiCoder(num):
    def actual(x):
        return x**num  # Raises x to the power of num
    return actual  # Return the inner function

f = chaiCoder(2)  # f now holds the actual function where num is 2
print(f)  # This will print the function's memory address
print(f(3))  # This will compute 3**2 and return 9

g = chaiCoder(3)  # g now holds the actual function where num is 3
print(g)  # This will print the function's memory address
print(g(3))  # This will compute 3**3 and return 27
