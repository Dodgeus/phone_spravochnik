def add_name(l, name):
	l.append(name.lower())
	l.append(" ")

def add_contact(l):
	data = open('contacts.txt', 'a')
	data.writelines(l)
	data.writelines("\n")
	data.close()

def search(word):
	text = open("contacts.txt", "r")
	line = text.readline()
	i = 0
	for line in text.readlines():
		if word in line:
			print("")
			print("Данные вашего контакта: ", line)
			break
	text.close()