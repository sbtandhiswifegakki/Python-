#1.parrot.py
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
#2.greeter
name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name + "!")

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 36:
	print("\nYou 're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little older.")

#even_or_odd
number = input("Enter a number, and I will tell you if it's even or odd: ")
number = int(number)
if number % 2 ==0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")


#exercise7.1
rent_cars = input("What kinds of cars do you want to rent?")
print("Let me see if I can find you a Subaru.")
#7.2
numbers = input("How many people are you going to have dinner?")
numbers = int(numbers)
if numbers >= 8:
	print("Sorry, We don't have free table ")
else:
	print("Yes,We have free table for you guys, Plesea follow me ,this way!")
#7.3
num = input("Enter a number, and I will tell you if it's a multiple of 10")
num = int(num)
if num % 10 == 0:
	print("It's a multiple of 10.")
else:
	print("It's not a multiple of 10.")

#while
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)
	

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(message)

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'input' to end the program. "
active = True
while active:
	message = input(prompt)
	if message == 'input':#key word is input
		active = False
	else:
		print(message)

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
	city = input(prompt)
	if city == 'Beijing':
		break
	else:
		print("I'd love to go to " + city.title() + "!")

current_num = 0
while current_num < 10:
	current_num += 1
	if current_num % 2 == 0:
		continue
	
	print(current_num)

x = 1
while x<= 5:
	print(x)
	x += 1
	
#execise7.4
#7.4
prompt = "\nPlease add your toppings:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
	message = input(prompt)
	if message == 'quit':
		active = False
	else:
		print("We would add " + message + " to your pizza.")
#7.5
age = input("Can you tell me your age?")
age = int(age)
if age < 3:
	print("You're free to watch the movie")
elif age >=3 and age <= 12:
	print("You have to pay $10.")
else:
	print("You have to pay $15.")
#7.6
prompt = "\nPlease add your toppings:"
prompt += "\nEnter 'quit' to end the program. "
while True:
	message = input(prompt)
	if message == 'quit':
		break
		
	else:
		print("We would add " + message + " to your pizza.")
#7.3.1		
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

#7.3.2
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
	pets.remove('cat')

print(pets)

#7.3.3 mountain_poll.py
responses = {}
polling_active = True
while polling_active:
	name = input("\nWhat is your name? ")
	response = input("What mountain would you like to climb someday? ")
	responses[name] = response#save key to value
	repeat = input("Would you like to let another person respond? (yes/ no) ")
	if repeat  == 'no':
		polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")

#exerciese7-8
sandwich_orders = ["tuna", "un Belge", "pieces"]
finished_orders = []
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("complishing orders: " + current_sandwich.title())
	finished_orders.append(current_sandwich)
print("The folling kinds of sandwiches in order have been finished: ")
for finished_order in finished_orders:
	print(finished_order.title())
	
#exerciese7-9
sandwich_orders = ["tuna", "un Belge", "pieces", "pastrami", "pastrami", "pastrami"]

print("All of pastrami have been sold out!")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print(sandwich_orders)

#7-10
answers = {}
polling_active = True
while polling_active:
	name = input("\nWhat is your name?")
	place = input("If you could visit one place in the world, Wher would you go?")
	answers[name] = place
	repeat = input("Would you like to let another person to answer this question? (yes/no) ")
	if repeat == "no":
		polling_active = False
for name, place in answers.items():
	print("\n" +name + " want to visit " + place + ".")



