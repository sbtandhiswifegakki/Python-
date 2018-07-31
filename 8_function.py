def greet_user():
	"""显示简单的问候"""
	print("Hello!")

greet_user()

def greet_user(username):
	"""显示简单的问候"""
	print("Hello, " + username.title() + "!")

greet_user('jack')

#exe8-1
def display_message():
	"""打印我在本章学的是什么"""
	print("我在本章学函数")

display_message()


#8-2
def favorite_book(title):
	"""显示我喜欢的一本书"""
	print("One of my favorite books is " + title.title() + " 。")
	
favorite_book('Harry_Potter')

def describe_pet(animal_type, pet_name):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
	
describe_pet('hamster', 'harry')
describe_pet('dog', 'xiaohei')
describe_pet(animal_type = 'cat', pet_name = "xiaohua")

def describe_pet(pet_name, animal_type='dog'):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(pet_name='mama')
describe_pet('lala')
describe_pet(pet_name='haha', animal_type='pig')

#8-3
def make_shirt(size, words):
	"""显示Ｔ恤的尺码和字样"""
	print("\nT-shirt's size is " + size + ".")
	print("\nT-shirt's words is " + words + ".")
	
make_shirt('middle', 'I am great') 	

def make_shirt(size='middle', words='I am Great'):
	"""显示Ｔ恤的大小和文字"""
	print("\nT-shirt's size is " + size + ".")
	print("\nT-shirt's words is " + words + ".")
make_shirt()

	
#下面这个有问题，显示非默认参数在默认参数后面	
def make_shirt(size='middle', words):
	"""显示Ｔ恤的大小和文字"""
	print("\nT-shirt's size is " + size + ".")
	print("\nT-shirt's words is " + words + ".")
make_shirt('I am Great')


def make_shirt(size='large', words='I love Python'):
	"""显示Ｔ恤的大小和文字"""
	print("\nT-shirt's size is " + size + ".")
	print("\nT-shirt's words is " + words + ".")
make_shirt()
make_shirt(size = 'middle')
make_shirt(words = 'I love R')

#describe_city
def describe_city(city, country):
	print("\n" + city.title() + " is in " + country.title())
describe_city('hangzhou', 'China')


def describe_city(city, country='China'):
	print("\n" + city.title() + " is in " + country.title())
describe_city('hangzhou')
describe_city('Beijing')
describe_city('Tokyo')

#8.3返回值
def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def get_formatted_name(first_name, middle_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + middle_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('john', 'lee', 'hooler')
print(musician)

#
def get_formatted_name(first_name, last_name, middle_name =''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi', 'henrix')
print(musician)

singer = get_formatted_name('john', 'hooker', 'lee')
print(singer)

def build_person(first_name, last_name):
	"""返回一个字典，其中包含有关一个人的信息"""
	person = {'first': first_name, 'last': last_name}
	return person
player = build_person('jimi', 'hendrix')
print(player)

def build_person(first_name, last_name, age=''):
	"""返回一个字典，其中包含有关一个人的信息"""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person
police = build_person('jimi', 'hendrix', age=23)
print(police)

def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' to quit at any time)")
	
	f_name = input("first name: ")
	if f_name =='q':
		break
	l_name = input("last name: ")
	if l_name =='q':
		break
	formatted_name = get_formatted_name(f_name, l_name)
	print("\nHello, " + formatted_name + "!")


#8-6
def city_country(city, country):
	full = '"' + city + ' , ' + country + '"'
	return full.title()
	

aaa = city_country('Santiago', 'Chile')
sss = city_country('chongqing', 'China')
ttt = city_country('tongling', 'China')
print(aaa)
print(sss)
print(ttt)

#8-7
def make_album(singer, album_name):
	album = {'singer': singer, 'album_name': album_name}
	return album
my1 = make_album('Jay', '范特西')
print(my1)
my2 = make_album('JiJi', '进化论')
print(my2)
my3 = make_album('Jay', '摩羯座')
print(my3)



def make_album(singer, album_name, num_songs=""):
	album = {'singer': singer, 'album_name': album_name}
	if num_songs:
		album['num_songs'] = num_songs
	return album
my4 = make_album('Jolin', '看我七十二变', num_songs=11)
print(my4)

#8-8
def make_album(singer, album_name):
	album = {'singer': singer, 'album_name': album_name}
	return album

while True:
	print("\nPlease tell me who is you favorite singer and his/her album's name?")
	print("(enter 'q' to quit at any time)")
	singer = input("singer: ")
	if singer == 'q':
		break
	album_name = input("album_name: ")
	if album_name == 'q':
		break
	aaa = make_album(singer, album_name)
	print(aaa)	


def greet_users(names):
	"""向列表中的每位用户都发出简单的问候"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print("Printing model: " + current_design)
	completed_models.append(current_design)
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)


#
def print_models(unprinted_designs, completed_models):
	"""
	模拟打印每个设计，直到没有未打印的设计为止，打印每个设计后，都将其移到列表
	completed_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("\nPrinting model: " + current_design)
		completed_models.append(current_design)
 
def show_completed_models(completed_models):
	"显示打印好的所有模型"
	print("\nThe folling models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

unprinted_designs = ['iphone case', 'root pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#修改副本
def print_models(unprinted_designs, completed_models):
	"""
	模拟打印每个设计，直到没有未打印的设计为止，打印每个设计后，都将其移到列表
	completed_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("\nPrinting model: " + current_design)
		completed_models.append(current_design)
 
def show_completed_models(completed_models):
	"显示打印好的所有模型"
	print("\nThe folling models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
unprinted_designs = ['iphone case', 'root pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

#8-9
def show_magicians(names):
	for name in names:
		print(name)
Names = ['David Kobofer', 'Mr.Li', 'Mrs.A']
show_magicians(Names)
#8-10
def make_great(magicians,alter_magicians):
	for magician in magicians:
		magician = 'the Great ' + magician#对列表中的元素进行修改
		print(magician)
	for alter_magician in alter_magicians:
		alter_magician = magician
		print(magician)
		print(alter_magician)
sbt = ['David Kobofer', 'Mr.Li', 'Mrs.A']
yes = []

def show_changed_names(changed_names):
	"显示改变后的所有魔术师名字"
	print("\nThe folling magician's name have been printed:")
	for changed_name in changed_names:
		print(changed_name)

sbt = ['David Kobofer', 'Mr.Li', 'Mrs.A']
yes = []
make_great(sbt)
show_changed_names(sbt)


#8-11
def make_great(magicians,alter_magicians):
	while magicians:
		altering_member = magicians.pop()
		alterred_member = 'the Great ' + altering_member
		alter_magicians.append(alterred_member)
def show_changed_names(changed_names):
	"显示改变后的所有魔术师名字"
	print("\nThe folling magician's name have been printed:")
	for changed_name in changed_names:
		print(changed_name)	

sbt = ['David Kobofer', 'Mr.Li', 'Mrs.A']
yes = []
make_great(sbt[:], yes)
show_changed_names(yes)
print(yes)
print(sbt)

	
#8.5
def make_pizza(*toppings):
	"""打印顾客点的所有配料"""
	print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
	"""概述要制作的比萨"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("-" + topping)
make_pizza('pepperoni')		
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(size, *toppings):
	"""概述要制作的比萨"""
	print("\nMaking a " + str(size) +
			"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

def build_profile(first, last, **user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstein',
							location='princeton',
							field='physics')
print(user_profile)

#8-12
def order(*material):
	"""概述顾客点的三明治添加食材"""
	print(material)
order('1', '3', '5', '6')
#8-13
def my_profile(first, last, **my_info):
	"""创建一个字典，其中包含我们知道的有关佘本涛的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('本涛', '佘',
							location='浙江大学',
							field='生物信息学',
							age=23)
print(user_profile)

#8-14
def make_car(manufacture, model, **car_info):
	info = {}
	info['manufacture_name'] = manufacture
	info['model_name'] = model
	for key, value in car_info.items():
		info[key] = value
	return info
    
car = make_car('Toyota', 'Karolia', color='red', tow_package='have')
print(car)
	

def make_pizza(size, *toppings):
	"""概述要制作的比萨"""
	print("\nMaking a " + str(size) +
			"-inch pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)
def make_car(manufacture, model, **car_info):
	info = {}
	info['manufacture_name'] = manufacture
	info['model_name'] = model
	for key, value in car_info.items():
		info[key] = value
	return info
import test
test.make_pizza(16, 'pepperoni')

from test import make_car
car = make_car('Toyota', 'Karolia', color='blue', tow_package='have')
print(car)#保证模块的干净整洁

from test import make_pizza as s
s(12, 'mushrooms', 'green', 'extra cheese')

import test as p
p.make_pizza(12, 'mushrooms', 'green', 'extra cheese')

#from pizza import * 导入模块中的所有函数
