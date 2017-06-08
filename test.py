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
'''
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
        break
    else:
        print('猜小了')
    chance -= 1
    print('你还有',chance,'次机会')
print('太笨了,游戏结束!正确数字是',random_num)
'''

#找出列表中最大的数
'''
nums = [6,11,7,9,4,2,1]
hand = None

for i in nums:
    if hand is None or  hand > i:
        hand = i
print(hand)
'''

#移动nums中最大的数字到最后

'''
nums = [6,11,7,9,4,2,1]

for j in range(len(nums)-1):
    for i in range(len(nums)-1):
        if nums[i]  > nums[i+1]:
            temp = nums[i]
            nums[i] = nums[i + 1]
            nums[i + 1] = temp

#    print(nums)
print(nums)
'''

#todolist  提示用户输入do或者任务(非do),如果用户输入任务,则添加到list中,如果用户输入do,当任务为空时则打印无任务并退出,否则从list中根据先进先出原则打印任务

'''
tasks = []

while True:
    input_text = input('please input do or a task:')
    if input_text != 'do':
        tasks.append(input_text)
    else:
        if len(tasks) == 0:
            print('无任务')
            break
        else:
            task = tasks.pop(0)
            print('任务:',task)
'''


#获取两个list中相同的元素到第三个列表中,并保证不重复
'''
nums1 = [1,2,3,4,5,3,10,11]
num2 = [1,2,3,1,4,5,5,3,12,34]
result = []

for i in nums1:
    if i in num2 and i not in result:
        result.append(i)
print(result)
'''


#用户管理
#1、让用户在控制台上输入"find/list/add/delete/update/exit"格式字符串
#2、如果输入add,则让用户继续输入用户名、年龄、联系方式等数据,将用户数据(用户名,年龄,联系方式),放入list中存储,在放入list之前检查用户名不重复,如果重复,则提示用户已存在
#3、如果输入delete,则让用户输入"用户名"字符串,根据用户名查找list中数据,若存在数据则将该数据移除,若用户数据不存在,则提示不存在
#4、如果输入update,则让用户分别输入用户名、年龄、联系方式等数据,根据用户名查找list中数据,若存在数据则将数据更新为新的(用户名,年龄,联系方式),若用户数据不存在,则提示不存在
#5、如果用户输入find,则让用户输入"用户名",根据用户名查找list中数据名等于字符串的用户信息,并打印
#6、如果用户输入list,则打印所有用户信息
#7、打印用户第一个行数据为用户信息描述,从第二行开始为用户数据
#8、如果用户输入exit,则打印退出程序,并退出


user_info_tpl ='|{0:>20}|{1:>5}|{2:>20}|'
user_info_header = user_info_tpl.format('name','age','telephone')
while True:
    action = input('please input (find/list/add/delete/update/exit): ')
    if action == 'add':
        #增加用户
        name = input('请输入用户名:')
        age = input('请输入年龄:')
        tel = input('请输入电话号码:')
        is_exists = False
        for user in users:
            if name == user[0]:
                print('添加用户失败,失败原因:用户名已存在')
                is_exists= True
                break

        if not is_exists:
            users.append((name,age,tel))
            print('添加用户成功')

    elif action == 'delete':
        #删除用户
        name = input('请输入你要删除的用户名:')
        is_exists = False
        for user  in users:
            if name == user[0]:
                is_exists = True
                users.remove(user)
                print('删除用户成功')
                break

            if not is_exists:
                print('用户删除失败,失败原因:用户不存在')

    elif action == 'update':
        #更新用户
        name = input('请输入用户名:')
        age = input('请输入年龄:')
        tel = input('请输入电话号码:')
        for user in users:
            if name == user[0]:
                users.remove(user)
                is_exists = True
                break

        if is_exists:
            users.append((name,age,tel))
            print('更新用户成功')
        else:
            print('更新用户失败,用户不存在')


    elif action == 'find':
        #查找用户
        is_exists = False
        name = input('请输入要查找的用户名:')
        print(user_info_header)
        for user in users:
            if name == user[0]:
                print(user_info_tpl.format(user[0],user[1],user[2]))
                is_exists = True

        if not is_exists:
            print('没有找到用户')

    elif action == 'list':
        #列出用户
        print(user_info_header)
        for user in users:
            print(user_info_tpl.format(user[0],user[1],user[2]))

    elif action == 'exit':
        #退出程序
        break
    else:
        print('error,please input find/list/add/delete/update/exit')