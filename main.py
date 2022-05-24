import add as fun_add
change = ''
while(change!='0'):
	print("1.Для поиска контакта введите '1'\n2.Для добавления контакта введите '2'\n3.Для отключения программы введите '0'")
	change = input()
	if (change!="1") and (change!="2"):
		print("Некоректное число. Введите чило без пробелов")
	elif change=="2":
		lis = []
		nik = input("Введите имя контакта: ")
		fun_add.add_name(lis, nik)
		print("Введите номер телефона контакта", nik, ": ")
		phone = input()
		fun_add.add_name(lis, phone)
		print("Введите описание контакта", nik, ": ")
		char = input()
		fun_add.add_name(lis, char)
		fun_add.add_contact(lis)
		print("Контакт", nik, " был добавлен.")
	elif change=="1":
		name = input('Введите имя контакта: ')
		fun_add.search(name.lower())
exit()