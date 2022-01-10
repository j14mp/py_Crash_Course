def customer_toppings(*toppings):
	print('\nThe customer wants the following toppings:')
	for topping in toppings:
		print(f'- {topping}')

customer_toppings('pepperoni')
customer_toppings('sausage', 'chicken')
customer_toppings('extra cheese', 'chicken', 'bacon', 'sausage')

def build_profile(first, last, **user_info):
	user_info['first'] = first
	user_info['last'] = last
	return user_info

user_prof = build_profile('Kevin', "O'leary", age = 22, ethnicity = 'caucasian', nationality = 'Irish')

print(user_prof)

def car_info(manufacturer, model_name, **kargs):
	kargs['manufacturer'] = manufacturer
	kargs['model'] = model_name
	return kargs

my_car = car_info('Toyota', 'Corolla', four_wheel_drive = False, sun_roof = False)
print(my_car)