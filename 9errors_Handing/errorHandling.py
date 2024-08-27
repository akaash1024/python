# x= ('masala','lemon', 'ginger')
# y=enumerate(x)
# print(list(y)) #[(0, 'masala'), (1, 'lemon'), (2, 'ginger')]

#----------------------------------------

# file = open('test.py') #open
# file2 = open("akash.py", "w") # i just wrote and run temp.py and boom akash.py created with edition mode.

#----------------------------------------
# method1

file =  open ('youtube.txt', 'w') #as it compile, it created youtube.txt

try:
    file.write("Akash") #on running, create youtube.txt and and write "Akash"
finally:
    file.close()

# method2
with open('youtube2.txt','w') as file:
    file.write("Akash Kevat") #on running, create youtube.txt and and write "Akash Kevat"
