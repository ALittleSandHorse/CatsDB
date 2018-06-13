import shelve as sh
from Library import db_helper as dh
import os

"""
	Библиотека методов для редактирования БД
	Автор: Духнай Екатерина и Магомедов Шамиль
"""


def clear_db():
	"""
		Сбрасывает базу (db_path) данных к первоначальному виду
		Параметры: нет
		Автор:
	"""
	try:
		os.remove('../Data/' + dh.db_name + '.bak')
		os.remove('../Data/' + dh.db_name + '.dat')
		os.remove('../Data/' + dh.db_name + '.dir')
	except OSError:
		pass
	dh.create_db_from_dict(dh.from_ls_to_dict(dh.cats), dh.db_name)

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
	#db[dh.last_id_field] = int(db[dh.last_id_field]) - 1
	db.close()


def add_cat(cat, db_path):
	"""
		Добавляет кота(cat) в базу данных(db_path)
		Параметры: dict cat, str db_path
		Автор:
	"""
	db = sh.open(db_path)
	db[str(db[dh.last_id_field])] = cat
	db[dh.last_id_field] = str(int(db[dh.last_id_field]) + 1)
	db.close()