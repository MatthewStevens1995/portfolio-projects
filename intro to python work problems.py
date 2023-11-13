from math import pi

from math import sqrt
from math import sin

pie = pi

#verifying pie is what we expect
print(pie)

#radius = float(input("whats the radius of the sphere?: ")

#Area = 4*pie*radius**2
#Volume = (4/3)*pie*radius**2

def radius_and_volume(radius:float):
   ## radius = float(input("whats the radius of the sphere?: ")
    Area = 4*pie*radius**2
    Volume = (4/3)*pie*radius**2
    print('the area of a sphere is: ', round(Area,3),
        'the volume of the sphere is ', round(Volume,3))
    
radius_and_volume(7)


# writing a program that calculates the cost per square inch for a circular pizza, given
# diameter and price. circle area = pi*R**2

def cost_per_square_inch(diameter:float,price:float):
    radius = diameter/2
    Area = pie*radius**2
    price_per_square_inch = price*((1/Area))
    print('the cost per square inch is: ',price_per_square_inch)

cost_per_square_inch(12,18) # not sure if this is missing a **2 to square or not.



## a program that determines the molecular weight of a molecule
def molecular_weight():

    # asking user for number of each atom in molecule
    C,H,O = eval(input("How many carbon atoms, How many Hydrogen atoms, and How many Oxygen atoms , in the molecule? :"))

# establishing molecular weights
    carbon_weight = C*12.0107
    Hydrogen_weight = H*1.00794
    Oxygen_weight = O*15.9994

#adding up all the weights
    net_molecule_weight = carbon_weight + Hydrogen_weight + Oxygen_weight

    # printing output
    print('the molecular weight of the molecule is:',net_molecule_weight,"g/mole")

molecular_weight()


# a program that determines the distance to a lightening strike based on time elapsed between flash and 
# the speed of sound
def distance_from_lightening():

    #establishing constants
    speed_of_sound = 1100
    mile_dist = 5280

    #getting the time elapsed since seeing lightening
    time_elapsed = float(input("how much time elapsed between when you saw and when you heard it? : "))
    
    # telling user how far the lightening stike was from user
    print('the lightening strike was',time_elapsed*speed_of_sound,"feet away")

distance_from_lightening()


#Heres a program that determines cost of an order
def cost_of_order():
    shipping = .86 + 1.5
    cost_of_coffee = 10.5 + shipping
    print("the cost of an order is ",cost_of_coffee, "dollars")

cost_of_order()


# writng a program that determines the slope between two points in a plane given the inputs
def slope():
    x1,y1,x2,y2 = eval(input("what are the coordinates of the two points in question? "))
    slope_bby = (y2-y1)/(x2-x1)
    print("the slope is: ",slope_bby)

slope()

# writing a program that determines the distance between two points
def distance_between_points():
    x1,y1,x2,y2 = eval(input("what are the coordinates of the two points in question? "))
    distance_bby = sqrt(((x2-x1)**2)+((y2-y1)**2))
    print('the distance between two points is: ',distance_bby)

distance_between_points()

#writing a program to determine area of triangle by length of sides
def area_of_triangle(a:float,b:float,c:float):

    #write out known formulas
    s = (a+b+c)/2
    Area = sqrt(s*(s-a)*(s-b)*(s-c))
    
    # print out result
    print('the area of the triangle is: ',Area)

area_of_triangle(20,20,20)

#writing a program to determine the length of a ladder required to reach a 
#given height when leaned aganist a house. the height and angle of ladder
# are given as inputs
def len_of_ladder(height:float):
    # getting user input to determine angle
    radians = float(input("what is the angle of the ladder to the house, in degrees: "))
    radians = (pi/180)*radians
    #writing down constants
    length = height/sin(radians)
    print('the length of the ladder required is :',length)
    
len_of_ladder(10)


# writing a program that accepts a quiz score and prints out the corrosponding grade.
# 0:F,1:5,2:D,3:C,4:B,5:A

def quiz_score(grade):
    grades = ['F','F','D','C','B','A']
    print('your grade is an: ',grades[grade])

quiz_score(2)


## inputting some words and outputting the 
# acroynm of those words

words = input('input some words to make an acronym of: ')
words = words.upper().split(' ')
acronym =[]
for i in words:
    acronym.append(i[0])
print("".join(acronym))


# be able to sum up the value of someones name such that
# they provide an input (their name) and an output is
# returned. a=1,b=2, etc. 'zelle'=60 for example

# logic, we want to be able to, given a name,
# split it up to its component letters, match
# each letter to a number, then add all the numbers
# of the name together and print that sum.

name = input('what is your first name?: ')
name=name.lower().split()
accumulator = 0
for i in name:
    for j in i:
        new_num=ord(j)-96
        accumulator = accumulator + new_num

print(accumulator)

## do the same thing but expand to take into
# account a full name like "matthew stevens"

name = input('what is your first name?: ')
name=name.lower().split(' ')
accumulator = 0
for i in name:
    for j in i:
        new_num=ord(j)-96
        accumulator = accumulator + new_num
print(accumulator)


## create a 'caesar cipher'. this incodes a text
# and shifts each letter in the text some
# amount given by a key, using the unicode as
# encoding default scheme. 
key = 2
thing_to_encode = input('What do you what to encode?: ')
encoded = ''
for word in thing_to_encode:
    for character in word:
        new_char = chr(int(ord(character))+key)
        encoded = encoded + new_char
print(encoded)

decoded = ''
for word in encoded:
    for char in word:
        new_char = chr(int(ord(char))-key)
        decoded = decoded + new_char
print(decoded)

## do same thing as above, except make it circular
# so that the next number after 'z' is A. this
# means that its a alphabet only character pickup

strng = 'abcdefghijklmnopqrstuvwxyz'

key = 2
thing_to_encode = input('What do you what to encode?: ')
thing_to_encode = thing_to_encode.lower()
encoded = ''
for word in thing_to_encode:
    for character in word:
        new_char = strng[int(ord(character))-96+key]
        encoded = encoded + new_char
print(encoded)

decoded = ''
for word in encoded:
    for char in word:
        new_char = strng[int(ord(char)-key)]
        #new_char = chr(new_char)
        decoded = decoded + new_char
print(decoded)


# write a program that counts the number of words
# in a sentance entered by a user

user_input = input('tell me your words brother').split( )
num_of_words = len(user_input)
print('the number of words is {0}'.format(num_of_words))

# write a program that calculates the average word
# length in a sentance entered by user
letter_count = 0
word_count = 0

user_input = input('share your words brother').split(' ')
word_count = len(user_input)
for word in user_input:
    for letter in word:
        letter_count = letter_count + 1
avg_word_length = letter_count/word_count
print(avg_word_length)


# chapter 6 programming exercises, topic is functions

#print a program to the lyrics of the song 'old mcdonal had a farm'.
# the program should print the lyrics for the five different animals,
#similar to the example verse (see book)

pets = ['cat','dog','ferret','hamster','chinchilla']


def eio():
    print('old mcdonal had a farm, ee-igh,ee-igh,oh!')
def animal(animal):
    print('and on that farm he had a '+ animal,' ee-eigh, ee-igh, oh!')
def addem_up():
    for pet in pets:
        eio()
        animal(pet)
        eio

addem_up()


## write a program that prints the first ten verses of "the ants go marching"
# this exercise sucks
lis = ['one','two','three','four','five','six','seven','eight','nine','ten']
def ants_go_marching(number):
    print('the ants go marching '+number+ ' by '+number+', hurrah! hurrah!')
def ants_go_marching_number(number):
    print('the ants go marching '+number+ ' by '+number+',')
    print('the little one sucks his thumb')
def rest_of_song():
    print('and they all go marching down...')
    print('in the grond...')
    print('to get out...')
    print('of the rain.')
    print('Boom! Boom! Boom!')

def addem_boys():
    for num in lis:
        ants_go_marching(num)
        ants_go_marching(num)
        ants_go_marching_number(num)
        rest_of_song()

addem_boys()


# sphereArea(radius) returns the surface area of a sphere having
# a given radius.
# sphereVolume(radius) returns thr volume of a sphere having given
#radius
## use functions to solve exercise 1 from chapter 3

def sphereArea(radius):
    return 4*pi*(radius**2)

def sphereVolume(radius):
    return 4/3*pi*(radius**2)

def sphereA_and_sphereV(user):
    return 'with a radius of '+str(user)+' the sphere area is '+str(round(sphereArea(user),2))+ ' and the sphere volume is '+str(round(sphereVolume(user),2))

sphereA_and_sphereV(4)

# write definitions for the following two functions:
# 1) sumN(n) returns the sum of the first n natural numbers
# 2) sumNCubes(n) returns the sum of the cubes of the first n natural numbers

# then use these functions in a program that prompts the user for
# an input, n, and prints out what the output would be for the 2 functions
# with the user input

def sumN(n):
    accumulator = 0
    for num in range(0,n+1):
        accumulator = accumulator+num
    return accumulator

def sumNcubes(n):
    accumulator = 0
    for num in range(0,n+1):
        accumulator = accumulator + num**3
    return accumulator

def show_time():
    num = int(input('what integer number do you want to sum natural numbers to and sum of cubes?'))
    return 'the sum of the first natural numbers is '+str(sumN(num))+ '.The sum of cubes is '+str(sumNcubes(num))+'.'

show_time()


# redo programming exercise 2 from chapter 3. use two functions-
# - one to compute area of a pizza, and the one to compute cost per
# square inch

def piza_area(diameter):
    radius = 1/2*diameter
    area = pi*(radius**2)
    return area
def cost_per_inch(diameter,cost):

    return (1/piza_area(diameter)) * cost

def addem_boys(user_diameter,costt):
    return 'the area of the pizza is '+str(round(piza_area(user_diameter),2)),'and the cost per square inch is '+ str(round(cost_per_inch(user_diameter,costt),2))

addem_boys(7,12)

# area of triangle using side lengths as input

def total_length(a,b,c):
    s = (a+b+c)/2
    area = sqrt(s*((s-a)*(s-b)*(s-c)))
    return 'the area is ',round(area,2)

total_length(1,2,3)
# couldnt find something required in this exercise


# write a function to compute the nth fibonachi number.
# use your function to solve programming exercise 16 from chapter 3

def fibonacci(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    fibArray = [0, 1]
    for num in range(2,n+1):
        fibArray.append(fibArray[num-1] + fibArray[num-2])
    return fibArray[n]
print(fibonacci(6))

# use a funcion to return the acronym of a phrase entred as a string

def acrnoym1():
    words = input('input some words to make an acronym of: ')
    words = words.upper().split(' ')
    acronym =[]
    for word in words:
        acronym.append(word[0])
    print("".join(acronym))
acrnoym1()            
            


# squareEach(nums) nums is a list of number, make the function square each number in the list of numbers
li = [15,23,33,44,54]
def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    return nums
print(squareEach(li))

# sumList(nums) nums is a list of numbers. returns the sum of numbers in the list.  make this function

l = [1,2,3,4,5]
def sumList(nums):
    accumulator = 0
    for num in range(len(nums)):
        accumulator = accumulator + nums[num]
    print(accumulator)

sumList(l)


# toNumbers(strlist) is a list of  strings, each of which represents a number. modifies each
# entry in the list by converting it into a number

l=['hell','ya','brahhh']
def toNumbers(strlist):
    num = 15
    for word in range(len(strlist)):
        strlist[word] = num
    print(strlist)
toNumbers(l)


#-------------------------------------chapter 7 exercises:

# many companies pay 1.5x for any hours worked above 40 in a week. write a program to input the number
# of hours worked and hourly rate and calculate the total wages for the week

def wages(rate,hours):
    wage=0
    if hours <= 40:
        wage=rate*hours
    else:
        wage = (1.5*rate*(hours-40)) + (rate*40)
    print(wage)

wages(40,40)


# a certain CS professor gives gives a 5 point quiz. write a program that accepts a quiz score as 
# an input and uses a decision tree structure to calculate the corrosponding grade. 

def quiz_grade(score):
    if score == 0 or score==1:
        grade = 'F'
    elif score == 2:
        grade = 'D'
    elif score == 3:
        grade = 'C'
    elif score == 4:
        grade ='B'
    else:
        grade = 'A'
    print(grade)
quiz_grade(4)

## this time do same thing but with scores 1-100, 90-100 being an 'A'. 

def test_grade(score):
    if score <=59:
        grade = 'F'
    elif score >=60 and score<= 69:
        grade = 'D'
    elif score >=70 and score<=79:
        grade = 'C'
    elif score >=80 and score<=89:
        grade ='B'
    else:
        grade = 'A'
    print(grade)
test_grade(89)


# a certain college classifies students according to credits earned. a student with less than 7 is a freshman
# at least 7 to be sophmore. 16 to be junior and 27 to be senior. write a program that calculates class
# standing from number of credits earned

def class_standn(credits):
    if credits < 7:
        standing = 'Freshman'
    elif credits >= 7 and credits < 16:
        standing = 'Sophmore'
    elif credits >=16 and credits <27:
        standing = 'Junior'
    else:
        standing = 'Senior'
    print(standing)
class_standn(50)


# exercise 5, chapter 7: BMI problem. to much instructions to write. will just do solution.

def BMI_calc(weight,height):
    bmi =(weight*720)/(height**2)
    if bmi >=19 and bmi <=25:
        person = 'you have a healthy bmi'
    else:
        person = 'you have a unhealthy bmi'
    print(person)

BMI_calc(180,72)

# exercise 6 chapter 7 exercise. instructions too much to write
def speedin_fine(speedLimit,clocked_speed):
    if clocked_speed < speedLimit:
        message = 'The speed was legal'
    elif clocked_speed > speedLimit and clocked_speed <=90:
        extra_bucks = 5*(clocked_speed - speedLimit)+50
        fine = 50+ extra_bucks
        message='your driving illegal and your fine is: ',fine
    else:
        extra_bucks = 5*(clocked_speed - speedLimit)+50
        fine = 50+ extra_bucks+200
        message='your driving illegal and your fine is: ',fine
    print(message)
speedin_fine(40,75)
        

# exercise 7, chapter 7

def baby_sitr_cost(StartTime,EndTime):
    if EndTime > 18:
        extra_rate = 1.75*(EndTime-18)
        normal_rate = 2.5* (18-StartTime)
        cost = extra_rate+normal_rate
    else:
        normal_rate = 2.5 * (EndTime-StartTime)
        cost = normal_rate
    print(cost)
baby_sitr_cost(13,19)


# exercise 8, chapter 7
def house_and_senate_eligability(years_citizen,age):
    if years_citizen >=7 and years_citizen < 9 and age >=25 and age < 30:
        message = 'your just eligable for US REP'
    elif  years_citizen >= 9 and age >=30:
        message = 'your eligable to be a US senator'
    else:
        message = 'your not eligable for shit'
    print(message)
house_and_senate_eligability(10,20)

# exercise 9, chapter 7
def day_of_easter(year):
    if year >= 1982 and year <= 2048:
        a = year%19
        b = year%4
        c = year%7
        d = ((19*a)+24)%30
        e = (2*b + 4*c + 6*d + 5)%7
        message='the day of easter in march is March '+str(22+d+e)+'th'
    else:
        message = 'date is not valid'
    print(message)

day_of_easter(1995)


# exercise 10 is just like exercise 9, so skippping to problem 11. 

def is_it_a_leap_year(year):
    if year % 4 ==0 and year % 400 != 0:
        message = 'not leap year'
    elif  year % 4 ==0: 
        message = 'The year '+str(year)+' is a leap year.'
    else:
        message = 'not a yeap year'
    print(message)
is_it_a_leap_year(1900)


#  exercise 12 chapter 7

def valid_date(date):
    date = date.split('/')
    for i in range(len(date)):
        date[i] = int(date[i])
    year = int(date[2])
    day = int(date[1])
    month = int(date[0])

    
    # testing if a date is valid
    if month <0 or month >12 or day<0 or day>31 or year <0:
        message = 'date is NOT invalid'
    elif month == 1 and day <= 31:
         message = 'this is a valid date'
    elif month == 2 and day <= 28:
            message = 'this is a valid date'
    elif month == 3 and day <= 31:
            message = 'this is a valid date'
    elif month == 4 and day <= 30:
            message = 'this is a valid date'
    elif month == 5 and day <= 31:
            message = 'this is a valid date'
    elif month == 6 and day <= 30:
            message = 'this is a valid date'
    elif month == 7 and day <= 31:
            message = 'this is a valid date'
    elif month == 8 and day <= 31:
            message = 'this is a valid date'
    elif month == 9 and day <= 30:
            message = 'this is a valid date'
    elif month == 10 and day <= 31:
            message = 'this is a valid date'
    elif month == 11 and day <= 30:
            message = 'this is a valid date'
    elif month == 12 and day <= 31:
            message = 'this is a valid date'
    else:
        message = 'not a valid date'
    print(message)
valid_date('9/31/2000')
    


# exercise 13 chapter 7:

def day_of_year(date):
    date = date.split('/')
    for i in range(len(date)):
        date[i] = int(date[i])
    year = int(date[2])
    day = int(date[1])
    month = int(date[0])
    
# testing if leap year
    if year % 4 ==0 and year % 400 != 0:
        leap = 'not leap year'
    elif  year % 4 ==0: 
        leap = 'The year '+str(year)+' is a leap year.'
    else:
        leap = 'not a yeap year'
    

    # testing if a date is valid
    if month <0 or month >12 or day<0 or day>31 or year <0:
        message = 'date is NOT invalid'
    elif month == 1 and day <= 31:
         message = 'this is a valid date'
    elif month == 2 and day <= 28:
            message = 'this is a valid date'
    elif month == 3 and day <= 31:
            message = 'this is a valid date'
    elif month == 4 and day <= 30:
            message = 'this is a valid date'
    elif month == 5 and day <= 31:
            message = 'this is a valid date'
    elif month == 6 and day <= 30:
            message = 'this is a valid date'
    elif month == 7 and day <= 31:
            message = 'this is a valid date'
    elif month == 8 and day <= 31:
            message = 'this is a valid date'
    elif month == 9 and day <= 30:
            message = 'this is a valid date'
    elif month == 10 and day <= 31:
            message = 'this is a valid date'
    elif month == 11 and day <= 30:
            message = 'this is a valid date'
    elif month == 12 and day <= 31:
            message = 'this is a valid date'
    else:
        message = 'not a valid date'

# daynum calc
    daynum = 31*(month-1)+day
    if month > 2:
         daynum = daynum - (4*month+23)//10
    if  leap == 'The year '+str(year)+' is a leap year.':
         daynum = daynum+1
    
    # printing time
    if message == 'date is NOT invalid' or message == 'not a valid date':
         return print(message)
    elif message == 'this is a valid date':
         return 'the day number of the year is: ',daynum
    
day_of_year('9/30/2000')

# exception practice

def exception_practice(num:int)->str:
    try:
        num/0
    except ZeroDivisionError as e:
        if str(e) == 'division by zero':
            message ='your dividing by zero moron'
        else:
            message = 'wassup'
    return message

exception_practice(1)




## exercise 1 chapter 8
# creating a program that outputs the fibinachi sequence 
# up to and including the number supplied by the user

def fib(num)->list:
     seq = [1,1]
     number= 0 
     for i in range(2,num):
        number = seq[i-1]+seq[i-2]
        seq.append(number)
     print(seq)

fib(100)
     
#exercise 2 chapter 8
## making a list that shows the windshill index in,
# where each attribute increments the wind speed by 5

def wind_chill(tempature:int)->list:
     windspeed = 0
     windchill_values =[]
     while windspeed <=50:
        ind = 35.74 + (.6215*tempature) - (35.75*(windspeed**.16))+.4275*(windspeed**.16)
        windspeed = windspeed +5
        windchill_values.append(ind)
     print(windchill_values)

wind_chill(100)

# exercise 3 chapter 8
#write a program that uses a while loop to determine how long
# it takes for an investment to double at a given interest rate. 
# the input will be an annualized rate and the output will be
#number of year it takes an investment to double.

def double_money(annual_rate:float)->float:
     initial_investment = 1000
     initial_investment_doubled =2000
     years=0
     while initial_investment < initial_investment_doubled:
          initial_investment = initial_investment*(1+annual_rate)
          years = years + 1
     print(years)

double_money(.06)


#exercise 4 chapter 8
# this is a syracuse sequence exercise.
def syr(num:int)->list:
     seq=[num]
     while num != 1:
          if num%2 == 0:
               num=num/2
          else:
               num=3*num+1
          seq.append(num)
     print(seq)

syr(5)

# exercise 5, chapter 8
# a positive whole number n>2 is prime if no number between
#2 and sqrt(n) inclusive evenly divides n. write a program
# that accepts a value of n as input and determines if the value
# is prime. if n is not prime, your program should quit
# as soon as it finds a value that evenly divides n. 

def is_prime(num:int)->str:
     # first part is to determine if prime or not
    accumulator = 2
    while True:
        if accumulator <= sqrt(num):
            if  num%accumulator!=0:
                accumulator=accumulator+1
            else:
                 break
        else:
             break
        
    if  num%accumulator!=0:
            return(num)
             
    #else:
            # print('the number is not prime')

# the above code could forsure be optimized. 
is_prime(25)
          


# exercise 6 chapter 8:
# modify the previous program to find every prime number less
# than or equal to n.


# come back to this problem

def primes_less_than_nums(num:int)->list:
     # first part is to determine if prime or not
    primes_less_than_num = []
    for i in range(2,num+1):
         is_it = is_prime(i)
         if is_it != None:
            primes_less_than_num.append(is_it)
    return primes_less_than_num
primes_less_than_nums(29)

# the Goldbach conjecture asserts that every even number is the
# sum of two prime numbers.write a program that gets a number
# from the user, checks to make sure is is even, then finds
# two prime numbers that add up to the number.

def goldbach_conjecture(num):
    if num%2==0:
        li1 = primes_less_than_nums(num)
        li2 = primes_less_than_nums(num)
        for i in range(len(li1)):
             for j in range(len(li2)):
                  if li1[i]+li2[j] == num:
                       message = print( 'the two primes are: ',li1[i], 'and ',li2[j])
                       break
    else:
         message = 'the inputted number isnt even'
    print(message)

goldbach_conjecture(12)      
    
                
# excercise 8 chapter 8

# dont actually understand this question. skipping to next. 


#exercise 9 chapter 8

x=int(input('x,y'))
print(x)

def muli_leg_trip()-> str: 
    odometer= int(input('whats the odometer say?'))
    gas = int(input('whats the gas say?'))
    odometer_total = 0
    gas_total = 0
    trip_mpg = 0
    while gas != '' or odometer !='':
        try:
            odometer= int(input('whats the odometer say?'))
            gas = int(input('whats the gas say?'))
        except ValueError as e:
            if str(e) == "invalid literal for int() with base 10: ''":
                break
        odometer_total = odometer_total+odometer
        gas_total = gas_total + gas
        trip_mpg = odometer_total/gas_total
        mpg_this_leg = odometer/gas
        print('the trip MPG so far is: ',trip_mpg,'. The MPG this leg is :',mpg_this_leg)
    
muli_leg_trip()
         

#exercise 11 chapter 8

def heating_and_cooling_degree_days()->str:
    heating_degree_day = 0
    cooling_degree_day = 0

    while True:
        daily_forcast = input('whats the forcasted temp for the days').split(',')
        for day in range(len(daily_forcast)):
            daily_forcast[day] = int(daily_forcast[day])
            if daily_forcast[day] <60:
                heating_degree_day = heating_degree_day + (60 - daily_forcast[day])
            if int(daily_forcast[day]) > 80:
                cooling_degree_day = cooling_degree_day + (daily_forcast[day] - 80)
        print(' The total number of heating degree days are: ',heating_degree_day,' and the total number of cooling degree days are ',cooling_degree_day)
        break     

heating_and_cooling_degree_days()
         



#chapter 9, exercise 1
# the code immediatly below is the raquetball game that
# serves as a reference for the programming exercises
# in the chapter.

from random import random

def main():
     printIntro()
     probA,probB,n = getInputs()
     winsA,winsB = simNGames(n,probA,probB)
     printSummary(winsA,winsB)

def printIntro():
     print('This Program simulates a game of raquetball between two')
     print('players called "A" and "B". The ability of each player')
     print('indicated by the probability(a number between o and 1)')
     print('that the player wins the point when serving.')
     print('player A always has the first serve')

def getInputs():
     # Returns the simulation parameters
     a = float(input('What is the prob. player A wins the serve? '))
     b = float(input('What is the prob. player B wins the serve? '))
     n = int(input('How many games to simulate? '))
     return a,b,n

def simNGames(n,probA,probB):
     #simulates n games of raquetball between players whose
     # abilities are represented by the probability of winning a serve.
     # returns number of wins for A and B
     winsA=winsB=0
     for i in range(n):
          scoreA,scoreB = simOneGame(probA,probB)
          if scoreA > scoreB:
               winsA = winsA + 1
          else:
               winsB = winsB + 1
     return winsA,winsB

def simOneGame(probA, probB):
     # simulates a single game of raquetball between players
     # whose abilites are represented by the probability of
     # winning a serve.
     # returns finals scores for A and B
     serving = 'A'
     scoreA = 0
     scoreB = 0
     while not gameOver(scoreA,scoreB):
          if serving == 'A':
               if random() < probA:
                    scoreA = scoreA + 1
               else:
                    serving = 'B'
          else:
               if random() < probB:
                    scoreB = scoreB + 1
               else:
                    serving = 'A'
     return scoreA,scoreB

def gameOver(a,b):
     #a and b represent scores for a raquetball game
     # returns true if the game is over, false otherwise
     return a==15 or b==15

def printSummary(winsA,winsB):
     #prints a summary of wins for each player.
     n = winsA + winsB
     print("\nGames simulated:", n)
     print('Wins for A: {0} ({1:0.1%})'.format(winsA,winsA/n))
     print('Wins for B: {0} ({1:0.1%})'.format(winsB,winsB/n))

         
         
            
        
         
         
         

