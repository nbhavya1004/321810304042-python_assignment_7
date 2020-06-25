# 321810304042-python_assignment_7 :


# Bhavyasree N - 321810304042


#     1.     Generate first N number of Fibonacci numbers.Take N value from user...

# METHOD_1 :

n = int(input("Enter the number : "))
def printFibonacciNumbers(n) :
	f1 = 0
	f2 = 1
	if (n<1) :
		return
	for x in range(0,n) :
		print(f2,end=" ")
		next = f1 + f2
		f1 = f2
		f2 = next
printFibonacciNumbers(n)

# METHOD_2 :

n=int(input("enter the number"))
a=0
b=1
count=0
if n<0:
	print("enter the positive number")
elif n==1:
	print("fibonacci series upto ",n)
	print(a)
else:
	print("fibonacci series are:")
	while count<n:
		print(a)
		sum=a+b
		a=b
		b=sum
		count=count+1





#     2.     Take 10 integers from keyboard using loop and print their average value on the screen Print the following patterns using loop : 
#    * 
#    ** 
#    *** 
#    **** 

def star(n):
	for i in range (0,n):
		for j in range(0,i+1):
			print("*",end=" ")
		print("\r")
n=4
star(n)

n=input("enter any numbers:")
num=n.split()
print("\n")
print("enter all numbers",num)
sum=0
for i in num:
	sum+=int(i)
print("sum of numbers",sum)
avg=sum/len(num)
print(avg)





#     3.     Write a program to find the length of the string "refrigerator" without using len( ) function...

a = "refrigerator"
count = 0
for i in a :
	count = count + 1
print(count)





#     4.     Write a Python program to count the number of characters (character frequency) in a string...

# METHOD_1 :

def char_frequency(str1) :
	dict = { }           # dictionary
	for n in str1 :
		keys = dict.keys()
		if n in keys :
			dict[n] += 1
		else :
			dict[n] = 1
	return dict
print(char_frequency('python'))	
			
# METHOD_2 :			

str1= input('Enter the string:')
freq = {}        # character frequency
for i in str1: 
     if i in freq: 
        freq[i] += 1
     else: 
        freq[i] = 1
print ("Count of all characters in string is :\n",
str(freq))						
			




#     5.    Write a Python script that takes input from the user and displays that input back in upper and lower cases...

# METHOD_1 :

txt = "HelloWorld" [::-1]
print(txt.upper())
print(txt.lower())

# METHOD_2 :

user_input = input("Who is The Father of Python?")
print("The Father of Python is : ",user_input.upper())
print("The Father of Python is : ",user_input.lower())





#     6.     Write a Python program to count occurrences of a substring in a string...

# METHOD_1 :

str1 = 'Python is a general-purpose interpreted and interactive language!!!'
print()
print(str1.count("interpreted"))
print()

# METHOD_2 :

s="python is easy to learn"
print(s.count("python"))