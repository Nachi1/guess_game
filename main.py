# guessing game using random module
import random

corct_num = random.randint(1, 20)
max_of_guess = 4
count_of_guess = 0
while count_of_guess < max_of_guess:
    count_of_guess += 1
    guessed_number = int(input('Guess a number: '))
    if guessed_number == corct_num:
        print('you won\n'
              '{0} is the correct number '.format(corct_num))
        break
    else:
        print('try again')
        if count_of_guess == 1:
            print('you have 4 trial left')
        elif count_of_guess == 2:
            print('you have 3 trial left')
        elif count_of_guess == 3:
            print('you have 2 trial left')
        elif count_of_guess == 4:
            print('you have 1 trial left')
        else:
            continue
else:
    print('sorry you failed')
    print(corct_num, 'is the number')
