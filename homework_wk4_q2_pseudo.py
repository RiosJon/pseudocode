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

hour1 = int(input('Give me hours only in military time ' ))
minute1 = int(input('give minutes for first time ' ))
full_hour1 = str(hour1) + str(minute1)
hour2 = int(input('Give me hours only in military time for the 2nd one ' ))
minute2 = int(input('give me minutes for the second hour ' ))
full_hour2 = str(hour2) + str(minute2)
if hour1 < hour2:
    print(full_hour1, 'comes before', full_hour2)
elif hour1 > hour2:
    print(full_hour1 ,"comes before", full_hour2)
elif hour1 >23 or hour2 >23:
    print("That's not a correct hour in military time")
else:
    if minute1 < minute2:
        print(full_hour1, 'comes before', full_hour2)
    elif minute1 > minute2:
        print(full_hour2, "comes before", full_hour1)
    else:
        print('both times are the same')

