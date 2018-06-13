import shelve as sh
from Library import db_helper

"""
	Библиотека методов для редактирования БД
	Автор: Духнай Екатерина и Магомедов Шамиль
"""


def clear_db():
	"""
		Сбрасывает базу данных к первоначальному виду
		Параметры: нет
		Автор:
	"""
	with sh.open(db_helper.db_path) as db:
		for index in range(len(db_helper.cats)):
			db[str(index)] = db_helper.from_ls_to_dict(db_helper.cats)[index]
		db[db_helper.count_field] = len(db_helper.cats)


def edit_fields(id, new_values, db_path):
	"""
		Заменяет данные в бд(путь db_path) у элемнта(номер id) на новые данные
		Параметры: str id, dict new_values, str db_path
		Автор:
	"""
	db = sh.open(db_path)
	buffer = db[str(id)]
	for key in new_values:
		buffer[key] = new_values[key]
	db[str(id)] = buffer
	db.close()


def del_cat(id, db_path):
	"""
		Удаляет кота из базы данных(db_path) по id
		Параметры: str id, str db_path
		Автор:
	"""
	db = sh.open(db_path)
	del db[id]
	db[db_helper.count_field] = int(db[db_helper.count_field]) - 1
	db.close()


def add_cat(cat, db_path):
	"""
		Добавляет кота(cat) в базу данных(db_path)
		Параметры: dict cat, str db_path
		Автор:
	"""
	db = sh.open(db_path)
	db[str(db[db_helper.count_field])] = cat
	db[db_helper.count_field] = int(db[db_helper.count_field]) + 1
	db.close()