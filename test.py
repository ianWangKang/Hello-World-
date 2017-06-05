#encoding: utf-8

#提示用户分别输入name和age,并打印出"my name is xx,and i'm xx years old"
'''
print('hello world')

n = input('please your name:')
a = input('please your age:')
print("my name is",n,"and i'm",a,"years old")
'''

#提示用户从控制台输入两个数字,计算两个数字的和、差、积、商,并进行打印
'''
num1 = float(input('please input  some number1:'))
num2 = float(input('please input some number2:'))
print(num1, '+' ,num2, '=',num1 + num2)
print(num1,' -' ,num2, '=' ,num1 - num2)
print(num1 ,'*' ,num2 ,'=',num1 * num2)
print(num1,' / ',num2 ,'=',num1 / num2)
'''

'''
#妻子
print('>>>买一斤包子')
show = input('你看到西瓜了吗?')
if show == '看到了':
    print('>>>买一个西瓜')
'''

'''
#丈夫
print('>>>买一斤包子')
show = input('你看到西瓜了吗?')
if show == '看到了':
    print('买一个包子')
else:
    print('>>>买一斤包子')
'''

'''
#提示用户从控制台输入一个分数,并判断打印出来
num = int(input('please input a number:'))
if num >= 90:
    print('优秀')
elif num >= 80:
    print('良好')
elif num >= 60:
    print('及格')
else:
    print('不及格')
'''

'''
#提示用户输入一个年份,判断年份是否为润年
year = float(input('please input a year:'))
if year % 4 == 0  and year % 100 != 0 or year % 400 == 0:
    print(year,'是闰年 ')
else:
    print(year,'不是闰年')
'''

#求1到100的和
'''
idx = 1
idx_sum = 0

while idx <= 100:
    idx_sum = idx_sum +idx
    idx = idx + 1
print(idx_sum)
'''

#提示用户在控制台上输入数字或者exit,当用exit后结束程序,并打印所有输入数字的和与平均数
'''
input_text = input('请输入一个数字或exit(结束):')

input_sum = 0
input_conut = 0
while input_text != 'exit' :
    input_sum += float(input_text)
    input_conut += 1
    input_text = input('请输入一个数字或exit(结束):')

if input_conut == 0:
    print('sum:0, avg: 0')
else:
    print('sum:',input_sum,',avg',input_sum / input_conut)
'''

#break与continue的区别
'''
idx = 0

while idx <= 5:
    idx += 1
    if idx == 3:
        break
    print(idx)

idx = 0

while idx <= 5:
    idx += 1
    if idx == 3:
        continue
    print(idx)
'''

#打印99乘法表
'''
for x in range(1,10):
    for y in range(1,x+1):
        print(y,'x',x,'=',y * x,'\t',end='')
    print(end='\n')
'''


#猜数游戏,随机生成一个0到100的数字,提示用户在控制台上输入一个数字,小于生成的随机数,则打印猜小了,大于生成的随机数,则打印猜大了,等于生成的随机数,则打印猜对了,并结束程序,如5次都错误了,则打印太笨了,并结束程序

import random
random_num = random.randint(0,100)
user_num = 0
chance = 5
while user_num != random_num and chance >= 1:
    user_num = float(input('please input a number:'))
    #print(random_num)
    if user_num > random_num:
        print('猜大了')
    elif user_num == random_num:
        print('猜对了')
        exit()
    else:
        print('猜小了')
    chance -= 1
    print('你还有',chance,'次机会')
print('太笨了,游戏结束!')





