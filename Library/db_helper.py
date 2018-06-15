import math as m
import shelve as sh
from os.path import dirname, abspath

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
fields_wo_weight = ['name', 'genus', 'colour', 'habitat']
stats_fields = ['Средний вес', 'Дисперсия', 'Количество']
last_id_field = 'last_id'

workspace = dirname(dirname(abspath(__file__)))
db_name = 'data'
data_folder = workspace + '/Data/'
output_folder = workspace + '/Output/'
db_path = data_folder + db_name


def create_db_from_dict(cats, db_name):
	"""
		Создает БД (db_name) из словаря (cats)
		Параметры: dict cats, str db_name
		Возвращаемое значение: -
		Автор: Магомедов Шамиль
	"""
	db = sh.open(data_folder + db_name)
	index = 0
	for cat in cats:
		db[str(index)] = cats[cat]
		index += 1
	db[last_id_field] = index
	print(str(index))
	db.close()


def from_txt_to_db(file_path, db_name):
	"""
		Записывает котов из файла (file_path) в файл базы данных с именем db_name
		Параметры: str file_path, str db_name
		Возвращаемое значение: -
		Автор: Духнай Екатерина
	"""
	file = open(file_path, 'r')
	db = sh.open(data_folder + db_name)
	index = 0
	for line in file:
		db[str(index)] = dict(zip(fields, line.rstrip('\n').split(' | ')[1:]))
		index += 1
	db[last_id_field] = str(index)
	db.close()


def from_ls_ls_to_dict(cats_list):
	"""
		Преобразовывает список списков (котов) в словарь котов
		Параметры: list cats_list
		Возвращаемое значение: dict cats_dict
		Автор: Магомедов Шамиль
	"""
	cats_dict = {}
	for index in range(len(cats_list)):
		cats_dict[index] = dict(zip(fields, cats_list[index]))
	return cats_dict


def from_ls_dict_to_dict(cats_list):
	"""
		Преобразовывает список словарей (котов) в словарь котов
		Параметры: list cats_list
		Возвращаемое значение: dict cats
		Автор: Магомедов Шамиль
	"""
	cats = {}
	index = 0
	for cat in cats_list:
		cats[str(index)] = cat
		index += 1
	return cats


def from_dict_to_ls(cats_dic):
	"""
			Преобразовывает словарь словарей (котов) в список котов
			Параметры: dict cats_list
			Возвращаемое значение: list cats
			Автор: Магомедов Шамиль
	"""
	cats = []
	for cat in cats_dic:
		if cat != last_id_field:
			cats.append(cats_dic[cat])
	return cats


def print_dict_to_txt(file_name, cats_dict):
	"""
		Записывает словарь котов в файл [file_name].txt
		Параметры: str file_name, dict cats_dict
		Возвращаемое значение: -
		Автор: Духнай Екатерина
	"""
	file = open(output_folder + file_name + '.txt', 'w')
	for index in cats_dict:
		print("%d" % index, end='', file=file)
		for key in fields:
			print(" | %s" % cats_dict[index][key], end='', file=file)
		print(file=file)
	file.close()


def print_dict(cats_dict):
	"""
		Выводит в консоль словарь котов в форматированном виде
		Параметры: dict cats_dict
		Возвращаемое значение: -
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
		Возвращаемое значение: -
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
		Возвращаемое значение: список совпадений (list) matches
		Автор: Магомедов Шамиль
	"""
	db = sh.open(db_path)
	matches = []
	for key in db:
		if key != last_id_field:
			for field in db[key]:
				if field in fields and key not in matches:
					if str(db[key].get(field)).lower().find(request.lower()) != -1:
						matches.append(db[key])
	db.close()
	return matches


def get_cats_by_weight(w1, w2, db_path):
	"""
		Возвращает список котов удовлетворяющих условию: w1<= вес <=w2
		Параметры: float w1, float w2, str db_path
		Возвращаемое значение: список котов (list) matches
		Автор: Магомедов Шамиль
	"""
	db = sh.open(db_path)
	matches = []
	for item in db:
		if item != last_id_field:
			weight = db[item][fields[2]]
			if isFloat(str(weight)) and w1 <= weight <= w2:
				matches.append(db[item])
	db.close()
	return matches


def get_count(db_path):
	"""
		Получает из базы данных (db_path) количество котов
		Параметры: str db_path
		Возвращаемое значение: количество котов(int) count
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
		Возвращаемое значение: словарь котов(list) dict
		Автор: Духнай Екатерина
	"""
	dict = {}
	database = sh.open(db_path)
	for item in database:
		dict[item] = database[item]
	database.close()
	return dict


def get_dispersion(db_path):
	"""
		Вычисляет дисперсию массы кота
		Параметры: str db_path
		Возвращаемое значение: дисперсия веса кота (float) disp
		Автор: Духнай Екатерина
	"""
	db = sh.open(db_path)
	disp = 0
	mid = 0
	count = 0
	for item in db:
		if item != last_id_field:
			mid = mid + int(db[item][fields[2]])
			count = count + 1
	mid = mid / count
	for item in db:
		if item != last_id_field:
			disp = disp + m.pow((mid - db[item][fields[2]]), 2)
			disp = disp / count
	db.close()
	return disp


def get_average(db_path):
	"""
		Вычисляет средний вес котов
		Параметры: str db_path
		Возвращаемое значение: средний вес котов (float) average
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
		Возвращаемое значение: словарь статистики (dict) stats
		Автор: Духнай Екатерина
	"""
	stats = {}
	stats[stats_fields[0]] = get_average(db_path)
	stats[stats_fields[1]] = get_dispersion(db_path)
	stats[stats_fields[2]] = get_count(db_path)
	return stats


def print_stats_to_txt(file_name, stats):
	"""
		Записывает словарь статистики в файл [file_name].txt
		Параметры: str file_name, dict stats
		Возвращаемое значение: -
		Автор: Магомедов Шамиль
	"""
	file = open(output_folder + file_name + '.txt', 'w')
	for item in stats:
		print("%s = %s" % (item, stats[item]), file=file)
	file.close()


def sort(param, cats_list, reverse):
	"""
		Сортирует котов (cats_list) по определенному параметру (param)
		Параметры: str param, list cats_list, bool reverse
		Возвращаемое значение: отсортированный список котов(list)
		Автор: Магомедов Шамиль
	"""
	return sorted(cats_list, key=lambda cat: cat[param], reverse=reverse)

def isFloat(text):
    """
            Проверяет, является ли text float
            Параметры: str text
            Возвращаемое значение: Boolean True или Boolean False
            Автор:Духнай Екатерина
        """
    try:
        text = text.replace(",", ".")
        if isinstance(float(text), float) == False or float(text) <= 0:
            return False
    except ValueError:
        return False
    return True
