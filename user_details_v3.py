# In this version I will be using if and else to fix errors found from program planner.

#asking the user to enter their name.


try:
    name=str(input("enter your name:   "))
    if name == "1234":
        raise Exception
except: 
    input("Please enter your name \n")
    

#asking the user to enter their age by using try and except.


try:
    age=int(input("How old are you?:"))
except:
    print("This is not a valid data type")
if age<=8:
    print("Please try again next time, when you are over 8 years of age.")
else:
    print("Please carry on")


#asking if the user they are ready for the quiz

    
ready=input("are you ready for the quiz?: press y to continue or x to exit:")


if ready== "y" or "Y" or "yes" or "Yes" 
    print("lets begin")
    
elif ready== "x" or ready=="no" or "No" or "X":
    print("consider playing later")
