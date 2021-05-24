# A list to store all questions
questions = [
    "What is the capital of New Zealand?",  # 1
    "What countries capital is Jakarta?",  # 2
    "What is the capital of Iraq?",  # 3
    "What countries capital is Berlin?",  # 4
    "What is the capital of Italy?",  # 5
    "What countries capital is New Delhi?",  # 6
    "What is the capital of Australia?",  # 7
    "What countries capital is Cairo?",  # 8
    "What is the capital of Fiji?",  # 9
    "What countries capital is Paris",  # 10
]
# A dictionary to store answers
answers = {
    "1": ["Wellington", "wellington","b","B"],
    "2": ["Indonesia", "indonesia", "B", "b"],
    "3": ["Baghdad", "B", "b", "baghdad"],
    "4": ["germany","Germany", "B", "b"],
    "5": ["rome", "Rome", "b", "B"],
    "6": ["India", "india", "b", "B"],
    "7": ["Canberra", "canberra" "b", "B"],
    "8": ["Egypt", "egypt","b", "B"],
    "9": ["Suva", "suva", "b", "B"],
    "10": ["France", "france", "b", "B"]
}
# A list to store all options
options = [
    ["London", "Wellington", "Auckland"],
    ["India", "Indoneisa", "Japan"],
    ["Madagascar", "Baghdad", "Barcelona"],
    ["Rome", "Germany", "America"],
    ["Canberra", "Rome", "UAE"],
    ["Pakistan", "India", "China"],
    ["Sydney", "Canberra", "Wellington"],
    ["India", "Egypt", "Cheetos"],
    ["Tonga", "Suva", "Apia"],
    ["Fellas", "France", "Compton"]
]

score = 0  # Starting value of the Score
plusScore = 0
minusScore = 0

print("********************************************************************************************************************************")
print("**************************************************** WELCOME TO CAPITALS QUIZ ****************************************************")
print("********************************************************************************************************************************\n")

def digitDetection(x):  # Function to find numbers in the strings
    index = 0
    while index < len(x):
        try:
            if x[index].isdigit():
                raise Exception
        except Exception:
            print('\nNumbers have been detected in your name \nPlease remove these numbers')
            askName()
            break
        index += 1

def addScore(condition):  # Function to add or remove score
    global score, plusScore, minusScore
    if condition == True:
        score += 1
        plusScore += 1
    elif condition == False:
        score -= 1
        minusScore += 1
        if score <= 0:
            score = 0
    else:
        print('ERROR')

def askName():  # Looped function to ask user name
    global name
    try:
        name = input("What is your name?:  ")
        if name == "":
            print("\nUnexpected Value, Please Enter Your Name \nIf you do not wish to enter you name, please enter: 'n/a'")
            raise Exception
        if name == 'n/a':
            name = "Anonymous User"
        digitDetection(name)
    except Exception:
        askName()
askName()

def askAge():  # Looped function to ask age
    try:
        age = int(input("What is your Age {}?:  ".format(name)))
        if age <= 0:
            raise Exception
    except ValueError:
        print("\nPlease Enter your age \nNOTE. Your age cannot be a decimal number (eg. 5.4) and cannot have words or letters in it (eg. five)")
        askAge()
    except Exception:
        print("\nYou are too young to take the quiz right now")
        askAge()
askAge()

def askYrLvl():  # Looped function to ask Year Level
    try:

        yrLvl = int(input("What is your Year Level {}?:  ".format(name)))
        if yrLvl <= 0:
            print("\nYou are too young to take the quiz right now")
            askYrLvl()
    except ValueError:
        print("\nPlease Enter your Year Level \nNOTE. Your year level cannot be a decimal number (eg. 5.4) and cannot have words or letters in it (eg. five)")
        askYrLvl()
askYrLvl()

def ready():     #Looped function to ask user if ready
    global state
    state = input("\nAre you ready to take the quiz {}?: \na. Yes \nb. No \n=> ".format(name))
    if state == 'Yes' or state == 'yes' or state == 'a' or state == 'A' or state == 'y' or state == 'Y':
        state = True
    elif state == 'No' or state == 'no' or state == 'b' or state == 'B' or state == 'n' or state == 'N':
        state = False
    else:
        print("\n'{}' is an Unexpected Value, please enter Yes or No".format(state))
        ready()
ready()

if state == False:                    #if user is not ready to do the quiz
    print("\nThank you for your time {} \nHave a good day \nSee you later!".format(name))
    input("\nPress enter to exit the quiz...") #Print this so that the user knows that when they press enter, the quiz will close
    quit()
elif state == True:                    #if user is ready to do the quiz
   
    def askQuestions():                #function to cycle though each question
        for questionNumber in range(1, 11):        #For Loop to go through each question
            print("\nQuestion: {} | Score: {}".format(questionNumber, score))#Print the question number and the score
            print(questions[questionNumber-1])    #Print Question
            for x in range(3):  #Print the letters that the options can be refered to
                if x == 0:
                    letter = 'a'
                elif x == 1:
                    letter = 'b'
                elif x == 2:
                    letter = 'c'
                print("{}. {}".format(letter, options[questionNumber-1][x]))     #Print Options       
            ans = input("d. {}\n=>".format(options[questionNumber-1][3]))       #Print final option and and an input for an answer
            #Checking if the answer is correct
            correctAnswer = False
            for x in answers[str(questionNumber)]:  #Check if he answer input matches with any of the valid answers
                if ans == x:
                    correctAnswer = True    #Using this new varible to make sure that 'correct' is only printed once and only add one point point 
            if correctAnswer == True:
                print("Correct!")
                addScore(True)
            else:
                print("Incorrect!\nThe Correct Answer is {}".format(answers[str(questionNumber)][0])) #state answer and remove one point if wrong
                addScore(False)
    askQuestions()
    print("\nCongratulations {}!".format(name))
    print("\nYour results are: \nQuestions answered correctly: {} \nQuestions answered incorrectly: {}".format(plusScore, minusScore))
    print("Final Score : {}".format(score))
    input("\nPress enter to exit the quiz...")
    quit()
