#Question 1; Write a funtion to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as false.

def hello_name(username):
    print("Hello " + username + "!")
    hello_name("Alice")
    output: Hello Alice!

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing
def first_odds(n): 
    return[x for x in range(1, n+1, 2)
            if x % 1=0] , def odd_numbers(n): return [x for x in range(0,n+1)if x % 2==1]
   def first_odds():
    for num in range(1, 101, 2):
        print(num)
first_odds()
#output: [1, 3 , 5, 7,9,97,99]
def odd_numbers(n):
    return [x for x in range(1, n+1) if x % 2 != 0]
odd_nums = odd_numbers(10)
print(odd_nums) # Output: [1, 3, 5, 7, 9]
def odd_numbers(n):
    return [x for x in range(1, n+1) if x % 2 != 0]
odd_nums = odd_numbers(10)
print(odd_nums) # Output: [1, 3, 5, 7, 9]



def first_odds():
    for i in range(1, 101, 2):
        print(i)
first_odds()

#Question 3: Please Write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined def max_num_in_list)a_list);
def max_num_inlist (a_list):[2,4,6,8.3],max(lst),Out[2]:8;in[]=1 sorted(list) 

def max_num_in_list(a_list):
    if not a_list:  
        return None  
    max_num = a_list[0]  
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num
my_list = [3, 5, 1, 9, 2]
max_num = max_num_in_list(my_list)
print(max_num)  # Output: 9

#Question 4: Write a function to return if the given year is a leap year, A leap year is divisible by 4, but not dividible by 100, unless it is also dividible by 400. The return should be boolean Type (true/false).
def is_leap_year (a year): leap= def is_leap(year),Leap=False, if (year% 100 !=0):elif (year % 100==0)and (year %400!=0): leap=False,elif (year % 400==0): leap= True else: leap=False return leap

def is_leap_year(a_year):
    if a_year % 4 == 0:  # if the year is divisible by 4
        if a_year % 100 == 0:  # if the year is divisible by 100
            if a_year % 400 == 0:  # if the year is divisible by 400
                return True  # it's a leap year
            else:
                return False  # it's not a leap year
        else:
            return True  # it's a leap year
    else:
        return False  # it's not a leap year
    
my_year = 2000
is_leap = is_leap_year(my_year)
print(is_leap)  # Output: True


#Question 5: Write a functiont to check to see if all the numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but {1,2,4,5} are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
def is_consecutivela_list: = [2,3,1,4,5],sorte (list) is_consecutive) # Prints True 


def is_consecutive(a_list):
    if len(a_list) <= 1:
        return True
    
    min_num = min(a_list)
    max_num = max(a_list)
    
    return max_num - min_num == len(a_list) - 1

numbers1 = [2, 3, 4, 5, 6, 7]
result1 = is_consecutive(numbers1)
print(result1) # Output: True

numbers2 = [1, 2, 4, 5]
result2 = is_consecutive(numbers2)
print(result2) # Output: False

