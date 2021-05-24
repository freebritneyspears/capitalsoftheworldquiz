# in this version i will use dictionary and i will be writing my 10 questions of the quiz with their answers.


#asking the user to enter their name.
'''I used if and try and exception to fix errors where
you canb only put your name and not leave it blank or add numbers.'''


try:
    name=str(input("enter your name: "))
    if name == "1234":
        raise Exception
except: 
    input("Please enter your name \n")
    

#asking the user to enter their age by using try and except.
'''Used if and else to fix an error where you can only put the
age more than 8.'''


try:
    age=int(input("How old are you?: "))
except:
    print("This is not a valid data type")
if age<=8:
    print("Please try again next time,when you are over 8 years of age.")



#asking the user if they are ready for the quiz
''' I used elif as well to fix an error so the user only has two options either
to write yes or no'''

    
ready=input("are you ready for the quiz?: press y to continue or x to exit:")


if ready=="y" :
    print("lets continue")
    print("---------------------------------------------")
    print("Please answer the questions with the options, exactly how it is written is important :)")
    print("---------------------------------------------")
    
elif ready== "x" or "no":
    print("consider playing later") 


#Preparing the dictionary for my multichoice.
   
capitalsquiz={
'1.What is the capital of New Zealand?': 'Wellington',
'2.What country houses the capital Jakarta?': 'Indonesia',
'3.What is the capital of Iraq?': 'Baghdad',
'4.What country houses the capital Berlin?': 'Germany',
'5.What is the capital of Italy?': 'Rome',
'6.What country houses the capital New Delhi?': 'India',
'7.What is the capital of Australia?': 'Canberra',
'8.What country houses the capital Cairo?':'Egypt',
'9.What is the capital of Fiji?': 'Suva',
'10. What country houses the capital Paris?':'France',


}

#preparing the multi choice

optlist=['10:11:12:13',
         '11:12:18:20',
         'Wellington:Auckland:Christchurch:Banjul',
         'Indonesia:France:Grenada:Hungary',
         'Berlin: Ethiopia:Helsinki:Baghdad',
         'Germany:Guatemala:Honduras:Ecuador',
         'Athens:Bissau:Greece:Rome',
         'India:Costa Rica:Chile:Bangui',
         'Denmark:Gold Coast:Canberra:El Salvador',
         'Egypt:Sofia:Micronesia:Chad',
         'Suva:Tonga:Czechia:Colombia'
         'Dominican Republic:Italy:France:Eiffel']
         

score=0
optnum=0

for answer in capitalsquiz.keys():
    print("")
    capitals=capitalsquiz[answer]
    print("Question",[answer])
    print("Options= ",optlist[optnum])
    optnum=optnum+1
    capitals_guess=input(">")

    if capitals_guess==capitals:
        print("That is correct. Good Job!")
        score=score+1
        print("score",score+0)
        
    elif capitals_guess== (""):
        print ("Please type something")
    else:
        print("That is not correct.")
