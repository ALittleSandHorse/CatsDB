import shelve as sh

"""
	Библиотека методов для работы с даннами из БД
	Автор: Магомедов Шамиль и Духнай Екатерина
"""

cats = [["Лесная кошка", "Felis", 7, "Серо-коричневый", "Европа"],
		["Степная кошка", "Felis", 6, "Серый", "Азия"],
		["Каракал", "Caracal", 20, "Песочный", "Африка"],
		["Калимантанская кошка", "Catopuma", 4.5, "Коричневый", "Калимантан"],
		["Ириомотейская кошка", "Felis", 3, "Коричневый", "Япония"],
		["Онцилла", "Leopardus", 2.8, "Охристый", "Южная Америка"],
		["Ягуарунди", "Herpailurus", 9, "Рыжий", "Южная Америка"],
		["Кошка Жоффруа", "Oncifelis", 4.2, "Охристый", "Южная Америка"],
		["Андская кошка", "Oreailurus", 4, "Серебристо-серый", "Анды"],
		["Дымчатый леопард", "Neofelis", 20, "Светло-желтый", "Азия"],
		["Лев", "Panthera", 190, "Темно-золотой", "Африка"],
		["Пума", "Puma", 100, "Желто-бурый", "Африка"],
		["Леопард", "Panthera", 70, "Золотистый", "Азия"],
		["Бенгальский кот", "Prionailurus", 8, "Серо-желтый", "Азия"],
		["Рысь", "Lynx", 15, "Рыжий", "Сибирь"],

		["Сервал", "Leptailurus", 18, "Желтый", "Северная Африка"],
		["Оцелот", "Leopardus", 10, "Песчаный", "Южная Америка"],
		["Манул", "Otocolobus", 4.5, "Желтый", "Азия"],
		["Суматранская кошка", "Prionailurus", 2.1, "Коричневый", "Океания"],
		["Африканская золотая кошка", "Profelis", 11, "Золотой", "Африка"],
		["Кошка Темминка", "Catopuma", 12.3, "Коричневый", "Азия"],
		["Китайская кошка", "Felis", 9, "Песочный", "Китай"],
		["Маргай", "Leopardus", 3, "Коричнево-желтый", "Северная Америка"],
		["Пампасская кошка", "Oncifelis", 8, "Желтовато-серый", "Южная Америка"],
		["Онза", "Puma", 27, "Темно-рыжий", "Мексика"],
		["Тигр", "Panthera", 300, "Рыжий", "Азия"],
		["Ягуар", "Panthera", 100, "Темно-рыжий", "Южная Африка"],
		["Гепард", "Acinonyx", 50, "Песочный", "Африка"],
		["Снежный барс", "Uncia", 70, "Дымчатый", "Средняя Азия"],
		["Мраморная кошка", "Pardofelis", 3, "Коричневый", "Азия"]]

fields = ['name', 'genus', 'weight', 'colour', 'habitat']
stats_fields = ['Средний вес', 'Дисперсия', 'Количество']
db_name = 'data'
db_path = '../Data/' + db_name
last_id_field = 'last_id'


def create_db_from_dict(cats, db_name):
	"""
		Создает БД (db_name) из словаря (cats)
		Параметры: dict cats, str db_name
		Автор: Магомедов Шамиль
	"""
	db = sh.open('../Data/' + db_name)
	index = 0
	for cat in cats:
		db[str(index)] = cats[cat]
		index += 1
	db[last_id_field] = index
	print(str(index))
	db.close()


def from_txt_to_db(file_path, db_name):
	"""
		Записыввает котов из файла (file_path) в файл базы данных с именем db_name
		Параметры: str file_path, str db_name
		Автор: Духнай Екатерина
	"""
	file = open(file_path, 'r')
	db = sh.open('../Data/' + db_name)
	index = 0
	for line in file:
		db[str(index)] = dict(zip(fields, line.rstrip('\n').split(' | ')[1:]))
		index += 1
	db[last_id_field] = str(index)
	db.close()


def from_ls_to_dict(cats_list):
	"""
		Преобразовывает список котов в словарь котов
		Параметры: list cats_arr
		Автор: Магомедов Шамиль
	"""
	cats_dict = {}
	for index in range(len(cats_list)):
		cats_dict[index] = dict(zip(fields, cats_list[index]))
	return cats_dict


def print_dict_to_txt(file_name, cats_dict):
	"""
		Записыввает словарь котов в файл [file_name].txt
		Параметры: str file_name, dict cats_dict
		Автор: Духнай Екатерина
	"""
	file = open('../Output/' + file_name + '.txt', 'w')
	for index in cats_dict:
		print("%d" % index, end='', file=file)
		for key in fields:
			print(" | %s" % cats_dict[index][key], end='', file=file)
		print(file=file)
	file.close()


def print_dict(cats_dict):
	"""
		Выводит в консоль словарь котов в правильном виде
		Параметры: dict cats_dict
		Автор: Магомедов Шамиль
	"""
	for index in cats_dict:
		print("%d" % index, end='')
		for key in fields:
			print(" | %s" % cats_dict[index][key], end='')
		print()


def print_all_db(db_path):
	"""
		Выводит в консоль базу данных из db_path
		Параметры: str db_path
		Автор: Духнай Екатерина
	"""
	database = sh.open(db_path)
	for item in database:
		if item != last_id_field:
			print('-' * 4 + item + '-' * 4)
			for field in database[item]:
				print(str(field) + ' : ' + str(database[item].get(field)))
			print()
	print("Cats count = " + str(database[last_id_field]))
	database.close()


def search(request, fields, db_path):
	"""
		Находит все совпадения запроса(request) в базе данных(db_path) в полях(fields)
		Параметры: str request, list fields, str db_path
		Возвращает: список совпадений (list)
		Автор: Магомедов Шамиль
	"""
	db = sh.open(db_path)
	matches = []
	for key in db:
		if key != last_id_field:
			for field in db[key]:
				if field in fields and key not in matches:
					if db[key].get(field).lower().find(request.lower()) != -1:
						matches.append(db[key])
	db.close()
	return matches


def get_cats_by_weight(w1, w2, db_path):
	"""
		Возвращает список котов удовлетворяющих условию: вес
		Параметры: int w1, int w2, str db_path
		Возвращает: список котов (list)
		Автор: Магомедов Шамиль
	"""
	db = sh.open(db_path)
	matches = []
	for item in db:
		if item != last_id_field:
			# fields[2] - название поля, которое хранит вес кота
			weight = db[item][fields[2]]
			if str(weight).isdigit() and w1 <= weight <= w2:
				matches.append(db[item])
	db.close()
	return matches


def get_count(db_path):
	"""
		Получает из базы данных (db_path) количество котов
		Параметры: str db_path
		Возвращает: количество котов(int)
		Автор: Духнай Екатерина
	"""
	db = sh.open(db_path)
	count = len(db)
	db.close()
	return count


def get_dict_from_db(db_path):
	"""
		Получает из базы данных (db_path) словарь котов
		Параметры: str db_path
		Возвращает: словарь котов(list)
		Автор: Духнай Екатерина
	"""
	dict = {}
	database = sh.open(db_path)
	for item in database:
		dict[item] = database[item]
	database.close()
	return dict


def get_dispers(db_path):
	"""
		Вычисляет дисперсию веса кота
		Параметры: str db_path
		Возвращает: дисперсию веса кота (float)
		Автор: Духнай Екатерина
	"""
	count = 0
	sum = 0
	sq = 0
	db = sh.open(db_path)
	for item in db:
		if item != last_id_field:
			w = db[item][fields[2]]
			if str(w).isdigit():
				sum += float(w)
				sq = float(w) * float(w)
			count += 1
	average = get_average(db_path)
	disp = (sq - 2 * sum * average + count * average * average) / (count - 1)
	db.close()
	return disp


def get_average(db_path):
	"""
		Вычисляет средний вес котов
		Параметры: str db_path
		Возвращает: средний вес котов (float)
		Автор: Магомедов Шамиль
	"""
	average = 0
	count = 0
	db = sh.open(db_path)
	for item in db:
		if item != last_id_field:
			w = db[item][fields[2]]
			if str(w).isdigit():
				average += int(db[item][fields[2]])
			count += 1
	db.close()
	average /= count
	return average


def get_statistics(db_path):
	"""
		Создает статистику из дисперсии, среднего значения
		и общего количества котов
		Параметры: str db_path
		Возвращает: словарь статистики (dict)
		Автор: Духнай Екатерина
	"""
	stats = {}
	stats[stats_fields[0]] = get_average(db_path)
	stats[stats_fields[1]] = get_dispers(db_path)
	stats[stats_fields[2]] = get_count(db_path)
	return stats


def print_stats_to_txt(file_name, stats):
	"""
		Записывает словарь статистики в файл [file_name].txt
		Параметры: str file_name, dict stats
		Автор: Магомедов Шамиль
	"""
	file = open('../Output/' + file_name + '.txt', 'w')
	for item in stats:
		print("%s = %s" % (item, stats[item]), file=file)
	file.close()


def sort(param, cats_list, reverse):
	"""
		Сортирует котов (cats_list) по определенному параметру (param)
		Параметры: str param, list cats_list, bool reverse
		Возвращает: отсортированный список котов(list)
		Автор: Магомедов Шамиль
	"""
	return sorted(cats_list, key=lambda cat: cat[param], reverse=reverse)

def list_to_dict(lis):
	"""
			Бла-бла-бла
			Параметры: list lis
			Возвращает: отсортированный список котов(list)
			Автор: Магомедов Шамиль
		"""
	dic = {}
	index = 0
	for k in lis:
		dic[str(index)] = k
	index += 1
	return dic

# create_db_from_dict(from_ls_to_dict(cats), 'data')
# print_dict_to_txt('out', from_ls_to_dict(cats))
# from_txt_to_db('../Output/out.txt', 'data')
# create_db_from_dict(from_ls_to_dict(cats), 'data')
# print_all_db(db_path)
# new_ls = sort(fields[1], get_cats_by_weight(4, 6, db_path), False)

# print(search('Африка', [fields[4], fields[3]], db_path))
# print(get_cats_by_weight(10, 100, db_path))
# print(get_statistics(db_path))
# print_stats_to_txt('stats', get_statistics(db_path))
