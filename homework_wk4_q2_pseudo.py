# purpose: Follow the pseudo code
# when two points in time are compared each given as hours
# (in military time, ranging from 0-23)
# and minutes, the following pseudocode determines which comes first
# write a program that prompts the user for 2 points in time and prints the
# time that comes first, then the other time
# ********************************************
# inputs will be times
# outputs will be times + which comes first
# ********************************************

hour1 = int(input('Give me hours in military time' ))
hour2 = int(input('Give me one more' ))
minute1 = int(input('give minutes for first time' ))
minute2 = int(input('give minutes for second time' ))
if hour1 < hour2:
    print(print(hour1, 'comes before', hour2)
elif hour1 > hour2:
    print(hour2, 'comes before', hour1)
else:
    if minute1 < minute2:
        print(hour1, 'comes before', hour2)
    elif minute1 > minute2:
        print(hour2, "comes before", hour1)
    else:
        print('both times are the same')
