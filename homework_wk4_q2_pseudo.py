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

# WL: You were missing a ")" at the end of the input() for both this:
hour1 = input(int('---figure out an input-----'))
# WL: ...and this one, too.
hour2 = input(int('Give me one more'))
# might have to possibly input minute inputs here
# minute1 = input(int('')
# minute2 = input(int('')

if hour1 < hour2:
    # WL: hour1 comes before hour2
elif hour1 > hour2:
    # WL: hour2 comes before hour1
else:
    if minute1 < minute2:
        # WL: hour1 comes before hour2
    elif minute1 > minute2:
        # WL: hour2 comes before hour1
    else:
        # WL: both times are the same
