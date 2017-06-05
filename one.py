# _*_ coding:utf-8 _*_
#file = open('/Users/wangkang/Desktop/file.txt','w')
#file.write('hello world!')


#what_he_does = ' plays '
#his_instrument = 'guitar'
#his_name = 'Robert Johnson'
#artist_intro = his_name + what_he_does + his_instrument

#print(artist_intro)

#num = 1
#srting = '1'
#num2 = int(srting)
#print(num+num2)

#words = 'words' * 3
#print(words)

#word = 'a looooooong word'
#num = 12
#srting = 'bang'
#total = srting * (len(word) - num)
#print(total)

#name = 'My name is MiKe'

#print(name[0])

#print(name[-4])

#print(name[11:14])

#print(name[11:15])

#print(name[5:])

#print(name[:5])

#word = 'friends'
#find_the_evil_in_your_friends = \
#    word[0]+word[2:6]
#print(find_the_evil_in_your_friends)


#phone_number= '138-6666-0006'
#hiding_number= phone_number.replace(phone_number[:9],'*' * 9)
#print(hiding_number)

#search = '168'
#num_a = '138-6168-0006'
#num_b= '168-1222-0006'

#print(search + ' is at ' + str(num_a.find(search)) + ' to ' + str(num_a.find(search) + len(search)) + ' of num_a')
#print(search + ' is at ' + str(num_b.find(search)) + ' to ' + str(num_b.find(search) +len(search)) + ' of num_b')


#
#def fahrenheit_converter(C):
#    fahrenheit = C * 9/5 +32
#    return str(fahrenheit) + '℉'

#lyric_length = len('I Cry Out For Magic!')
#print(lyric_length)

#C2F = fahrenheit_converter(35)
#print(C2F)

#def fahrnheit_converter(C):
#    fahrnheit = C * 9/5 + 32
#    print(str(fahrnheit) + '℉')

#C2F = fahrnheit_converter(35)
#print(C2F)

#def trapezoid_area(base_up,base_down,height):
#    return 1/2 * (base_up + base_down) * height
#print(trapezoid_area(height=3,base_down=2,base_up=1))   #right
#print(trapezoid_area(height=3,base_down=2, 1))         #wrong
#print(trapezoid_area(base_up=1,base_down=2,3))         #wrong
#print(trapezoid_area(1,2,height=3))                     #right

#base_up = 1
#base_down = 2
#height = 3

#trapezoid_area(height,base_down,base_up)

#def flashlight (battery1,battery2):
#    return 'Light!'
#nanfu1 = 600
#nanfu2 = 600

#flashlight(nanfu1,nanfu2)


#def trapezoid_area(base_up,base_down,height=3):
#    return 1/2 * (base_up + base_down) * height
#trapezoid_area(1,2)


#file = open('/Users/wangkang/Desktop/file.txt','w')
#file.write('hello World!!!!')



#def text_create(name,msg):
#    desktop_path = '/Users/wangkang/Desktop/'
#    full_path = desktop_path + name + '.txt'
#    file = open(full_path,'w')
#    file.write(msg)
#    file.close()
#    print('Done')
#text_create('hello','hello!')



#def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'):
#    return word.replace(censored_word,changed_word)
#text_filter('python is lame!')

#def censored_text_create(name, msg):
#    clean_msg = text_filter(msg)
#    text_create(name,clean_msg)
#print(censored_text_create('Try','lame!lame!lame!'))


#album = ['Black Star','David Bowie',25,True]
#album.append('new song')
#print(album[0],album[-1])

#'Black Star' in album


#def account_login():
#    password = input('password:')
#    if password == '123456':
#        print('Login success!')
#    else:
#        print('Wrong passwrod or invalid input!')
#        account_login()
#account_login()

#def account_login():
#    password = input('password:')
#    password_correct = password == '123456'
#    if password_correct:
#        print('Login success!')
#    else:
#        print('Wrong password or invalid input!')
#        account_login()
#account_login()


#password_list = ['*#*#','123456']
#def account_login():
#    password = input('Password:')
#    password_correct = password == password_list[-1]
#    password_reset = password == password_list [0]
#    if password_correct:
#        print('Login success!')
#    elif password_reset:
#        new_password = input('Enter a new password:')
#        password_list.append(new_password)
#        print('Your password has changed sucessfully!')
#        account_login()
#    else:
#        print('Wrong password or invalid input!')
#        account_login()
#account_login()


#for every_letter in 'Hello world':
#    print(every_letter)

#for num in range(1,11):
#    print(str(num) + ' + 1 =',num + 1)

#songslist = ['Holy Diver','Thunderstruck','Rebel Rebel']
#for song in songslist:
##    if song == 'Holy Diver':
 #       print(song,' - Dio')
#    elif song == 'Thunderstruck':
#        print(song,' - AC/DC')
#    elif song == 'Rebel Rebel':
#        print(song,' - David Bowie')



#for i in  range(1,10):
#    for j in range(1,10):
#        print('{} x {} = {}'.format(i,j,i*j))



#count = 0
#while True:
#    print ('Repeat this line !')
#    count = count + 1
#    if count == 5:
#        break




#password_list = ['****','123456']

#def account_login():
#    tries = 3
#    while tries > 0:
#        password = input('Password:')
#        password_correct = password == password_list[-1]
#        password_reset = password == password_list[0]

#        if password_correct:
#            print('Login success!')
#        elif password_reset:
#            new_password = input('Enter a new password:')
#            password_list.append(new_password)
#            print('Password has changed successfully!')
#            account_login()
#        else:
#            print('Wrong password or invalid input!')
#            tries = tries - 1
#            print(tries,'times left')

#    else:
#        print('Your accout has been susoended')

#account_login()




#weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
#print(weekday[0])

#all_in_list = [
#    1,
#    1.0,
#    'a word',
#    print(1),
#    True,
#    [1,2],
#    (1,2),
#    {'Key':'value'}
#]
#print(all_in_list)



#fruit = ['pineapple','pear','grape']
#print(fruit)
##fruit.insert(0,'grape')
##fruit[0:0] = ['0range']
#fruit.remove('grape')
#print(fruit)
#fruit[0] = 'Grapefruit'
#print(fruit)
#del fruit[0:2]
#print(fruit)




#NASDAQ_code = {
#    'BIDU':'Baidu',
#    'SINA':'Sina',
#}
#NASDAQ_code['YOKU'] = 'Youku'
#NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})
#print(NASDAQ_code)
#del NASDAQ_code['FB']
#print(NASDAQ_code)




#letters = ('a','b','c','d','e','f','g')
#print(letters[1])



#a_set = {1,2,3,4}
#a_set.add(5)
#print(a_set)
#a_set.discard(5)
#print(a_set)




#num_list = [6,2,7,4,1,3,5]
#print(sorted(num_list,reverse=True))


num = [1,2,3]
str = [4,5,6]

for a,b  in zip(num,str):
    print(b,'is',a)