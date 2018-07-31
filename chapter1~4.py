#E42727#E42727#打印语句
message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course World!"
print(message)

print("you are a idiot!!!")

news = "You are a asshole"
news ="You are a beautiful girl!"
print(news)


#生日祝福
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

#向大家问好
print("Hello Python people!")


#list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0])
print(bicycles[-1])

print("My first bicycles was a " + bicycles[-2].title() + ".")

#magicians
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:#冒号不要忘了
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")
print("Thank you, everyone. That was a great magic show!")

#exercise
pizzas = ['peppernoi', 'bishengke', 'kendiji']
for pizza in pizzas:
	print(pizza)
	print("I like " + pizza + " pizza.\n")
print("I really love pizza!")

#大小写
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + "" + last_name
print("Hello, " + full_name.title() + "!")

my_name = "Eric"
print("Hello " + my_name.lower() + ", would you like to learn some Python today" + "?")
message1= "Albert Einstein once said, 'A person who never made a mistake never tried anything new.'"
print(message1)

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

#列表操作
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1, 'amazno')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['hona', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(1, 'amazno')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['hona', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")


Invitation_members = ['Harry', 'Emma', 'Tom']
news = "Tao wants " + Invitation_members[0] + " to come to my birthday party"
print(news)
news = "Tao wants " + Invitation_members[1] + " to come to my birthday party"
print(news)
news = "Tao wants " + Invitation_members[2] + " to come to my birthday party"
print(news)

Invitation_members = ['Harry', 'Emma', 'Tom']
missing_boys = 'Tom'
Invitation_members.remove(missing_boys)
print(Invitation_members)
print("\n" + missing_boys + " will not be with us")
Invitation_members.append('Jack')
print(Invitation_members)
Invitation_members.insert(2, 'Mary')
print(Invitation_members)
del Invitation_members[2]
print(Invitation_members)
popped_Invitation_members = Invitation_members.pop()
print(Invitation_members)
print(popped_Invitation_members)

#organize_list
cars = ['bam', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)
cars = ['audi', 'toyota', 'subara', 'bam']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the Original list again:")
print(cars)
cars.reverse()
print(cars)
len(cars)
print(cars[4])


#元组 can't be changed
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
	
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

foods = ("A", "B", "C", "D", "E")
for food in foods:
	print(food)


foods = ("\nA", "B", "C", "F", "G")
for food in foods:
	print(food)


#numbers
for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares =[]
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)

squares1 = [value**2 for value in range(1,11)]
print(squares1)

#exercise3
for value_ in range(1,21):
    print(value_)

number = list(range(1, 3))
for value in number:
    print(value)
print(min(number),max(number), sum(number))

num = list(range(1,21,2))
for value in num:
	print(value)

cubes = [value**3 for value in range(1,11)]
print(cubes)


#players
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:2])
print(players[-1:])

print("\nHere are the first three players on my team:")
for player in players[:3]:
	print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite food are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#exercise
my_num = ['1', '2', '3', '4', '5']
print("The first three items in the list are:")
myf_num = my_num[:3]
print(myf_num)
mym_num = my_num[1:4]
print("Three items from the middle of the list are:")
print(mym_num)
print("The last items in the list are:")
myl_num = my_num[-3:]
print(myl_num)


my_pizza = ['1', '2', '3', '4', '5', '6', '7']
my_pizza.append('9')
#I am done!

#列表解析
square4 = [num**2 for num in range（1,20）


   

