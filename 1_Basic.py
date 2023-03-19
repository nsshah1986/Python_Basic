from math import *
""""
# basic print cmd
#---------------------------------------------
print("Hello world")
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/    |")
print("-----")

character_name= "Nisarg"
character_age=36
print("theres is a man named "+character_name+",")
print("he is " + str(character_age)+ " years old")

# string basis
#---------------------------------------------------
phrase="python basic"
print(phrase +" is cool")
print(phrase.isupper())
print(phrase.upper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[3])
print(phrase.index("b"))
print(phrase.replace("basic","advance"))

#Number basis
#------------------------------------------------------
print(2+5)
print(2*(4+5))
mynum=10
print(mynum)
print("my number is " +str(mynum))
mynum=-10
print(mynum,abs(mynum))
print(pow(3,2))
print("max(3,6,4,8)=",max(3,6,4,8))
print("min(2,6,9,4)=",min(2,6,9,4))
print("round(4.5683)=",round(4.5683))

print("floor(3.7)=",floor(3.7))
print("ceil(3.7)=",ceil(3.7))
print("sqrt(81)=",sqrt(81))

# user inputs

name=input(" enter your name:")
AGE=input("enter our age:")
print( "Hello "+ name+"!  You are "+AGE)

#basic calculator"
#---------------------------------------
num1=input("enter num1:")
num2=input("enter num2:")
sum=num1+num2
print(sum)
sum=int(num1)+int(num2)
print(sum)

#list
#--------------------------------
friends=["tom","dick","herry","oscar","goldenglob","iifa"]
print(friends)
print(friends[2])
print(friends[-1])
print(friends[-3])
print(friends[2:])
print(friends[2:4])
friends[3]="sony"
print(friends)
lucky_number=[1,2,3,4,5]
friends.extend(lucky_number)
print(friends)
friends.append("zee")
print(friends)
friends.insert(1,"star")
print(friends)
friends.remove("dick")
print(friends)
friends.pop()
print(friends)
friends.sort()
print(friends)

#tuples
#----------------------------------------------------------
coordinate=(4,5)
print(coordinate[1])
coordinate[1]=3
print(coordinate[1])


#functions
#---------------------------------------------------------
def basic():
    print("hello world")
print("top")
basic()
print("bottom")

def greet(name,age):
    print("hello "+name, ": your age is "+ age)

greet("nisarg","36")
greet("Hirali","33")

def cube(num):
    return num*num*num
result=cube(4)
print(result)
print(cube2)

#if statements
#---------------------------------------------------------

is_male=True
is_tall=True

if is_male and is_tall:
    print(" you are  a tall male")
elif is_male and not (is_tall):
    print("you are a short male")
elif not (is_male) and is_tall:
    print(" you are not male but tall")
else:
    print( "you are not male and not tall")

def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(20,14,7))

num1 = float(input("enter  first number:"))
op=input(" enter operator:")
num2=float(input("enter 2nd number:"))

if op =="+":
    print("num1+num2 is:"+ str(num1+num2))
elif op=="-":
    print("num1-num2 is:"+ str(num1-num2))
else:
    print("invalid operator")


#dictionary
#---------------------------------------------------------

mathConversion= {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
}
print(mathConversion["Jan"])
print(mathConversion.get("Feb"))
print(mathConversion.get("June","June"))

#while
#---------------------------------------------------------

i=1
while i<=10:
    print(i)
    i+=1
print("done with loop")

secreat_word="Nisarg"
guess=""
guess_count=0
guess_limit=3
out_of_guess=False

while guess!=secreat_word and not(out_of_guess):
    if  guess_count<guess_limit:
        guess=input("enter guess:")
        guess_count+=1
    else:
      out_of_guess= True
if out_of_guess:
    print("you loss")
else:
    print("you win")

"""
# For Loop
#---------------------------------------------------------

for letter in "Nisarg":
    print(letter)
friends =["Jim","Niarg","Hirali"]
for name in friends:
    print(name)
for index in range(3,10):
    print(index)
for index in range (len(friends)):
    print(friends[index])

def raise_to_power (basenum,pownum):
    result=1
    for index in range (pownum):
        result=result*basenum
    return result
print(raise_to_power (4,3))