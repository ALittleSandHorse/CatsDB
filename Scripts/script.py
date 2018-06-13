""" 
    Выводит в консоль список котов и записывает их в базу данных
    Авторы: Магомедов Шамиль и Духнай Екатерина
"""

from Library import db_helper as db
from Library import db_tools as tools

############## тестирую фнкции
tools.clear_db()
db.print_all_db(db.db_path)
id = str(input())
tools.del_cat(id, db.db_path)
db.print_all_db(db.db_path)
##############

answ = -1
while answ != 0:
	print("1.Поиск кота\n"
		  + "2.Изменить данные кота\n"
		  + "3.Вывести базу данных в консоль\n"
		  + "4.Вывести базу данных в текстовый файл\n"
		  + "5.Добавить кота в базу данных\n"
		  + "0.Выход")
	answ = int(input())
	if answ == 1:
		print("Выберите один или несколько вариантов:\n"
			  + "1.Название\n"
			  + "2.Род\n"
			  + "3.Вес\n"
			  + "4.Цвет\n"
			  + "5.Среда обитания")
		ls = list(input())
		fields = []
		for i in ls:
			fields.append(db.fields[int(i) - 1])
			req = input('Введите, что хотите найти: ')
			matches = db.search(req, fields, db.db_path)
			if len(matches) > 0:
				print(matches)
			else:
				print('Ничего не найдено :(')