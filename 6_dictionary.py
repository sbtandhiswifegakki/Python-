alien_0 = {'color': 'green','point':5}
print(alien_0['color'])
print(alien_0['point'])
new_points = alien_0['point']
print("You just earned " + str(new_points) + " points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#添加＆修改
alien_0 = {}
alien_0['color'] = 'green'
alien_0['point'] = 5
print(alien_0)

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['speed'] = 'fast'
print("Original x_position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
	x_increasement = 1
elif alien_0['speed'] == 'medium':
	x_increasement = 2
else:
	x_increasement = 3
	
alien_0['x_position'] = alien_0['x_position'] + x_increasement
print("New x_position: " + str(alien_0['x_position']))

alien1_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'points': 10}
del alien1_0['points']
print(alien1_0)

#favorite language
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")
#exercies
informations = {'first_name': 'she', 'last_name': 'tao', 'age': 23, 'city': 'hangzhou'}
print(informations)


#user
user_0 = {
	'username': 'efermi',
	'first': 'enrico',
	'last': 'fermi',
	}
for key, value in user_0.items():
	print("\nKey: " + key)
	print("Value: " + value)

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name,language in favorite_languages.items():
	print(name.title() + " 's favorite language is " +
		language.title() + ".")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name in favorite_languages.keys():
	print(name.title())
	
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print(" Hi " + name.title() + ". I see your favorite language is " + 
		favorite_languages[name].title() + "!")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
if 'erin' not in favorite_languages.keys():
	print("\nErin, please take our poll!")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for name in sorted(favorite_languages.keys()):
	print(name.title() + " , thank you for taking the poll.")	
		
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for language in favorite_languages.values():
	print("The following languages have been mentioned: " + language.title())

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
for language in set(favorite_languages.values()):
	print(language.title())
	
#嵌套

alien_1 = {'color': 'green', 'points': '5'}
alien_2 = {'color': 'yellow', 'point': '10'}
alien_3 = {'color': 'red', 'point': '15'}

aliens = [alien_1, alien_2, alien_3]
for alien in aliens:
	print(alien)

aliens = []
for alien_number in range(30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens.append(new_alien)
print(aliens)

print("Total number of aliens: " + str(len(aliens)))

for alien in aliens[:5]:
	print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))
	
aliens5 = []
for alien_number in range(0,30):
	new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
	aliens5.append(new_alien)
for alien in aliens5[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10
		print(alien)
for alien in aliens5[4:8]:
	if alien['color'] == 'green':
		alien['color'] = 'red'
		alien['speed'] = 'fast'
		alien['points'] = 15
for alien in aliens5[0:10]:
	print(alien)
print("...")

#pizza

pizza = {
	'crust': 'thick',
	'toppings': ['mushrooms', 'extra cheese'],
	}

print("You ordered a " + pizza['crust'] + "-crust pizza" +
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)


#
favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python', 'haskell'],
	}
for name, languages in favorite_languages.items():
	print("\n" + name.title() + "'s favorite languages are:")
	for language in languages:
		print("\t" + language.title())

users = {
	'aeinstein': {
		'first': 'albert',
		'last': 'einstein',
		'location': 'princeton',
		},
	'mcurie':{
		'first': 'marie',
		'last': 'curie',
		'location': 'paris',
		},
	}

for username, user_info in users.items():
	print("\nUsername: " + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']
	
	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
	


#exercise 6-1
Captain_America = {
		'first_name': 'Steve',
		'last_name': 'Rogers',
		'age': '98',
		'city': 'New_York'
		}
print(Captain_America)

#exercise 6_2
favorite_numbers = {
	'Tony': 1,
	'Steve':6,
	'Peter':4,
	'Bruce':9,
	'Scott':0,
	}
for name,num in favorite_numbers.items():
	print("\n" + name + "'s favorite number is " + str(num) + ". Is it right?")

#6_3
Glossary = {
	'tuple': '元组',
	'list': '列表',
	'dict': '字典',
	'title': '首字大写',
	'del': '删除',
	}
print("tuple : " + Glossary['tuple'])
print("list : " + Glossary['list'])
print("dict : " + Glossary['dict'])
print("title : " + Glossary['title'])
print("del : " + Glossary['del'])


#6-4
Glossary = {
	'value': '值',
	'int': '整型',
	'float': '浮点数',
	'string': '字符串',
	'variable': '变量',
	}
for noun,meaning in Glossary.items():
	print("\n" + noun + ":" + meaning)

#6-5
Rivers = {
	'nile': 'egypt',
	'Amazon': 'brazil',
	'Changjiang': 'China',
	'Mississippi': 'American',
	}
for river,nation in Rivers.items():
	print("The " + river.title() + " runs through " + nation.title() + ".")
	print(nation.title())
	print(river.title())

#6-6
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}
query_lists = ['jen', 'sarah', 'edward', 'phil', 'Harry']

for name in query_lists:
	if name in favorite_languages.keys():
		print(name.title() + ", thanks for taking the poll")
	else:
		print(name.title() + ", please join our query")

#6-7
Captain_America = {
		'first_name': 'Steve',
		'last_name': 'Rogers',
		'age': 98,
		'city': 'New_York'
		}
Spider_Man = {
	'first_name': 'Petter',
	'last_name': 'Park',
	'age': 18,
	'city': 'New_York',
	}
Iron_Man = {
	'first_name': 'Tony',
	'las_name': 'Stark',
	'age': 32,
	'city': 'New_York',
	}
Hero_lists = [Captain_America, Spider_Man, Iron_Man]
for hero in Hero_lists:
	print(hero)

#6-8
pet1 = {'kind': 'pig', 'owner': 'Quill'}
pet2 = {'kind': 'cat', 'owner': 'Ben'}
pet3 = {'kind': 'dog', 'owner': 'Charles'}

Pets = [pet1, pet2, pet3]
for pet in Pets:
	print(pet)

#6-9
favorite_places = {
	'Victor': ['Grand Canyon Nation Park', 'Niagara Falls' 'Time Square'],
	'Susan': ['The White House', 'Metropolitan Museum of Art', 'Disneyland'],
	'Arthur': ['Las Vegas', 'Central Park', 'The Golden Gate Bridge'],
	}
for name, places in favorite_places.items():
	print("\n" + name + "'s favorite places are: " )
	for place in places:
		print("\t" + place)
		
#6-10
favorite_numbers = {
	'Tony': [1, 2, 3, 4],
	'Steve':[6, 3, 55, 99],
	'Peter':[4, 333],
	'Bruce':[9, 21, 33],
	'Scott':[0, 122],
	}
for name,nums in favorite_numbers.items():
	print("\n" + name + "'s favorite numbers are: " )
	for num in nums:
		print("\t" + str(num))
#6-11
cities = {
	'London': {
		'country': 'UK',
		'population': 30,
		'fact': 'old',
		},
	'Beijing': {
		'country': 'China',
		'population': 1300,
		'fact': 'big',
		},
	'New_York': {
		'country': 'USA',
		'population': 300,
		'fact': 'Advanced',
		},
	}
for City_name, City_info in cities.items():
	print("\nCity_name: " + City_name)
	print("\tcountry: " + City_info['country'])
	print("\tpopulation: " + str(City_info['population']))
	print("\tfact: " + City_info['fact'])
	


































#exercise 6-11

Heroes_infoes = {
		'Captain':{
		'first_name': 'Jack',
		'last_name': 'Sparrow',
		'age': '35',
		'city': 'New_York'
		},
		'Spider_man':{
		'first_name': 'Petter',
		'last_name': 'Park',
		'age': '19',
		'city': 'New_York'
		},
	}

			

for heroes, heroes_info in Heroes_infoes.items():
	print("\nSuperheroes: " + heroes)
	full_name =  heroes_info['first_name'] + " " + heroes_info['last_name']
	print("\tReal_name: " + full_name.title())
	print("\tage: " + heroes_info['age'])
	print("\tcity: " + heroes_info['city'])
