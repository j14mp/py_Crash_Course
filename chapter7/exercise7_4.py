prompt = '\nWhat toppings would you like on your pizza? '

while True:
	toppings = input(prompt)
	if toppings != 'quit':
		print(f"I'll add {toppings} to your pizza!")
	else:
		break

	
ticket_prompt = "\nWelcome to the movies!\nHow old are you?"

age = int(input(ticket_prompt))
if age < 3:
	print("Tickets are on the house.")
elif age >= 3 and age <= 12:
	print("That will be ten dollars.")
else:
	print("Tickets are $15.")
