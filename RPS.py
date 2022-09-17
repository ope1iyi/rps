import random
import time

intro = ''' This is a game of Rock, Paper and scissors, do enjoy and give some comments'''

print(intro)
time.sleep(2)


def play_again():
    run = True
    while run:
        replay = input('Do you want to play another round [yes/y or no/n] ')
        if replay in ['yes','y']:
            main()
        elif replay in ['no', 'n']:
            print('computer scored:', comp_score)
            print('you scored:', user_score)
            break
        else:
            print('Enter yes or no')
            

def main():
    global user_score
    global comp_score
    user_score = 0
    comp_score = 0

    Choices = ['rock','paper', 'scissors']
    dic_choices = {0:'rock', 1:'paper', 2:'scissors'}
   
    com = dic_choices[random.randint(0,2)]
    computer = com
    user_name = input('Please enter your name: ')

    rounds = 0
    no_plays = int(input("how may rounds do you want to play? "))
    print("Okay let's commence, shall we ")
    time.sleep(1.2)

    while rounds < no_plays:
        user_option = input('\nChoose rock, paper or scissors: ').lower()
        computer = random.choice(Choices)
        if user_option not in Choices:
            print(' Enter valid option ')
        if user_option == computer:
            print('computer picked', computer)
            print(user_name, 'picked', user_option)
            print("it's a tie")

        elif user_option == 'rock':
            if computer == 'paper':
                print('Computer picked', computer)
                time.sleep(0.6)
                print(user_name, 'picked', user_option)
                print('\n',"computer wins this round")
                comp_score += 1

            if computer == 'scissors':
                print('computer picked', computer)
                time.sleep(0.6)
                print(user_name, 'picked', user_option)
                print('\n',user_name, "wins this round")
                user_score += 1

        elif user_option == 'paper':
            if computer == 'scissors':
                print('computer picked', computer)
                time.sleep(0.6)
                print(user_name, 'picked', user_option)
                print('\n',"computer wins this round")
                comp_score += 1

            if computer == 'rock':
                print('computer picked', computer)
                time.sleep(0.6)
                print(user_name, 'picked', user_option)
                print('\n',user_name," wins this round")
                user_score += 1
                
        elif user_option == 'scissors':
            if computer == 'rock':
                print('computer picked', computer)
                time.sleep(0.6)
                print(user_name, 'picked', user_option)
                print('\n',"computer wins this round")
                comp_score += 1

            if computer == 'paper':
                print('\ncomputer picked', computer)
                print(user_name, 'picked', user_option)
                print('\n',user_name, " wins this round")
                user_score += 1

     
        rounds += 1
    print('computer scored:', comp_score)
    print('you scored:', user_score)


if __name__ == '__main__':  
    main()
    play_again()
