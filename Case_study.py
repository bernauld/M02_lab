# name: Mahougnon Djihouessi   
# M02 Lab - Case Study: if...else and while
# test if the student qualifies for either the Dean's List or the Honor Roll

# Entre the student last name
last_name = input("Please enter your last name: ")

# control of the last name entered in the programme
while last_name != "ZZZ":

# enter the student last name
    first_name = input("Please enter your first name: ")

# enter the student gpa
    gpa = float(input("Please enter your GPA: "))

# verification of the gpa entered in the programme
    if gpa >= 3.5:
        print("{} {} has made the Dean's list.".format(first_name, last_name))

# other verification of the gpa
    else:
        if gpa >= 3.25:
            print("{} {} has made the Honor Roll.".format(first_name, last_name))

# repeating of the process until the user enter "ZZZ"
    last_name = input("Please enter your last name or ZZZ to exit the loop: ")