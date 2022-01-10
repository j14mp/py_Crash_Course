def show_messages(texts):
	for text in texts:
		print(text)

def send_messages(texts):
	while texts:
		current_text = texts.pop()
		sent_messages.append(current_text)



text_messages = ['Hi, how are you?',
	'ttyl',
	'wru',
	'This is your grubhub driver',
	'wtf bro']

sent_messages = []

send_messages(text_messages[:])

print(f'These messages were sent: ')
for text in sent_messages:
	print(text)

print(f'This is the original list: {text_messages}')
print(f'This is the new list: {sent_messages}')

