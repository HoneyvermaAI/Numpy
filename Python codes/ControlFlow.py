"""
     Using if , elif , else for the control flow of the program.



    Voting Eligibility Check.
"""

# Age = int(input("Enter your Age : "))

"""if (Age >= 18):
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")"""



"""
Start , Stop and Skip range and Taking user input

"""
start = int(input("Enter the start Number : "))
stop = int(input("Enter the Stop Number : "))
skip = int(input("Enter the Number you want to skip : "))


if start < stop and start < skip < stop:
    for i in range(start, stop):
        if i == skip:
            continue
        print(i)
else:
    print("The Number is Out of Range! Please check again.")
