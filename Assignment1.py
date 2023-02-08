# Question 1
# Write a function to print "hello_USERNAME!"
def hello_name():
    print("hello_USERNAME")

hello_name()

# Question 2
# Write a python function that prints odd numbers from 1-100 but returns nothing
def first_odds():
    for number in range(100):
        if number % 2 == 1:
            print(number)

first_odds()
print(first_odds())

# Question 3
# Please write a Python function, 
# max_num_in_list to return the max number of a given list. 
def max_num_in_list(list):
    max_num = max(list)
    return(max_num)

list1 = [1,2,3,7652,2,5467,23243,3,442452,3]
print(max_num_in_list(list1))   

# Question 4
# Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(1997))

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    a_list=sorted(a_list)
    next=a_list[0]
    for number in a_list:
        if number == next:
            next+=1
            value = True
        else:
            value = False
            break
    return value

list0 = [4,5,6,7,8]
list1 = [3,4,5,3,8]
print(is_consecutive(list0))
print(is_consecutive(list1))
