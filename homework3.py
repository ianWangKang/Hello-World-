# _*_ conding:utf-8 _*_

#import random

#def rall_dice(number=3, points=None):
#    print('<<< ROLL THE DICE! >>>')
#    if points is None:
#        points = []
#    while number > 0:
#        point = random.randrange(1,7)
#        points.append(point)
#        number = number - 1
#    return points

#def roll_result(total):
#    isBig = 11 <= total <=18
#    isSmall = 3 <= total <=10
#    if isBig:
#        return 'Big'
#    elif isSmall:
#        return 'Small'

#def start_game():
#    your_money = 1000
#    while your_money > 0:
#        print('<<< GAME START! >>>')
#        choices = ['Big','Small']
#        your_chioce = input('Big or Small:')

#        if your_chioce in choices:
#            your_bet = int(input('how much you wanna bet ? - '))
#            points = rall_dice()
#            total = sum(points)
#            youWin = your_chioce == roll_result(total)
#            if youWin:
#                print('The points are',total,'you win!')
#                print('you gained {},you have {} now'.format(your_bet,your_money + your_bet))
#                your_money = your_money + your_bet
#            else:
#                print('The points are',total,'you lose!')
#                print('you lost {},you have {} now'.format(your_bet,your_money - your_bet))
#                your_money = your_money - your_bet
#        else:
#            print('Invalid mords')
#    else:
#        print('GAME OVER')
#start_game()




def number_test():

    while True:
        number = input('Enter your number:')
        CN_mobile = [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
        CN_union = [130,131,132,155,156,185,186,145,176,1709]
        CN_telecom = [133,153,180,181,189,177,1700]
        first_three = int(number[0:3])
        first_four = int(number[0:4])

        if  len(number) == 11:

            if first_three in CN_mobile or first_four in CN_mobile:
                print('Operator: China Mobile')
                print('We\'re sending verification code via text to your phone:',number)
                break
            elif first_three in CN_telecom or first_four in CN_telecom:
                print('Operator: China telecom')
                print('We\'re sending verification code via to your phone:',number)
                break
            elif first_three in CN_union or first_four in CN_union:
                print('Operator: China Union')
                print('We\re sending verification code via to your phone:',number)
                break
            else:
                print('No such a operator')
        else:
            print('Invalid length ,your number should be in 11 digits')
number_test()

