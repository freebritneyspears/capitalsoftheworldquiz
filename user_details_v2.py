# in this version i will use try and except to handle some errors.

#asking user to enter their name.
try:
    name = str(input("enter your name:   "))
    if name == "1234":
        raise Exception

except:
    input("please enter your name \n")

#asking the user to enter their age using try and except.
    
try:
    age = int(input("How old are you?:   "))
except:
    print("this is not a valid data type")


#asking the user if they are ready for the quiz

ready=input("are you ready for the quiz?: press y to continue or x to exit:   ")

 
if ready == "y" or "Y" or "Yes" or "yes":
    print("lets begin")

else:
    print("consider playing later")

