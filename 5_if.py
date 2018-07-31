#if cars.py
cars=['audi', 'bmw', 'subaru', 'toyata']
for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

#topping.py

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("\nHold the anchovies")

#banned_users.py 
banned_users =['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(user.title() + ", you can post a reponse if you wish.")

#voting.py
age = 17
if age >= 18:
	print("\nYou are old enough to vote!")
	print("Have you registered to vote yet?")
else:
	print ("Sorry, you are too young to vote,Please register to vote as soon as you turn 18!")

#amusement_park.py
age = 12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")

age = 13
if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 65:
	price = 10
else:
	price = 5

print("Your admission cost is $" + str(price) + ",")

	
#topping.py
requested1_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested1_toppings:
	print("\nAdding mushrooms.")
if 'pepperoni' in requested1_toppings:
	print("Adding pepperoni.")
if 'extra cheese' in requested1_toppings:
	print("Adding extra cheese.")

print("\nFinished making you pizza!")

#green peppers
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry,We are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("\nFinished making you toppings")

#list is blank
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("\nAdding " + requested_topping + ".")
	else:
		print("Sorry, we don't have " + requested_topping + ".")
	
print("\nFinished making your pizza!")

#exercise
users = ['admin', 'Eric', 'Jack', 'Bob', 'Tao']
for user in users:
	if user == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print("Hello " + user + " , thank you for logging in again")
		
users = ['admin', 'Eric', 'Jack', 'Bob', 'Tao']
if users:
	for user in users:
		if user == 'admin':
			print("\nHello admin, would you like to see a status report?")
		else:
			print("Hello " + user + " , thank you for logging in again")
else:
	print("We need to find some users!")
	
#exercise2
current_users = ['admin', 'Eric', 'Jack', 'Bob', 'Tao']
new_users = ['admin', 'Jack', 'Mary', 'Sara', 'Tom']
for new_user in new_users:
	if new_user in current_users:
		print("You need to input other diffenent user_names")
	else:
		print("The user_name has not been used yet!")


