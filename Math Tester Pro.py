#Kurt Carvalho - 60011901
#Assignment - fully functional maths test

import random
correct = 0
count = 1

print('Welcome to Maths Tester Pro!')
print('Select your difficulty')
print('1.) Easy')
print('2.) Medium')
print('3.) Hard')



def inputInt(prompt, errorMessage = 'Invalid input - Try again.', minValue = (1), maxValue = (3)):
    while True:
        try:
            difficulty = input('Select a difficulty: ')
            difficulty = int(difficulty)
        except(ValueError):
            print(errorMessage)

        else:
            if(int(difficulty) >= int(minValue) and int(difficulty) <= int(maxValue)):
               return int(difficulty)
               break
            else:
                print('out of range')

difficulty = inputInt('Select a difficulty: ')

if int(difficulty) is (1):
    print('Easy Test selected')
    maxNum = 10
    questionN = 5

elif int(difficulty) is (2):
    print('Medium Test selected')
    maxNum = 25
    questionN = 10

elif int(difficulty) is (3):
    print('Hard Test selected')
    maxNum = 50
    questionN = 15

 
def generateQuestion(maxNum):
    num1, num2 = random.randint(0,maxNum), random.randint(0,maxNum)
    operator = ('+', '-')
    op = random.choice(operator)
    question = str( num1 ) + op + str( num2 ) + ' is? :'
    answer = eval(str( num1 ) + op + str( num2 ))
    Uanswer = input(question)
    while str.isdigit(Uanswer) == False:
        Uanswer = input(question)
    x,y = {answer, Uanswer}
    return (x,y)


while(count <= questionN):
    print('Question' + str(count) + 'of' + str(questionN))
    x,y = generateQuestion(maxNum)
    if (int(x) == int(y)):
        print('Correct!')
        correct = correct + 1
    else:
        print('Wrong answer :(')
    count = count + 1
    score =  ((correct/questionN)*100)
    
print ('Results:')
print ('You got ' + str(correct) + '/' + str(questionN))
if int(score) >= 50:
    print('Which is ' + str(score) + '% - You passed! :-D')
else:
    print('Which is ' + str(score) + '% - You Failed! :-( ')
    print('Better luck next time!')



