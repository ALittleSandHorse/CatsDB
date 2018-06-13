from tkinter import *

from Library import db_helper as dh
from Library import db_tools as dt
from Scripts import win_constants as w


def fetch_add(entries, label, window):
	"""
		Получает введенные пользователем значения из entries
		В зависимости от fun обрабатывает эти значения
		Устанавливает в label метку об успешном завершении действия
		Параметры: list entries, str fun, tkinter.Label label
		Автор:
	"""
	cat = {}
	i = 0
	for entry in entries:
		field = dh.fields[i]
		text = entry[1].get()
		entry[1].delete(0, 'end')
		cat[field] = text
		i += 1
	for c in cat:
		print(c, cat[c])
	dt.add_cat(cat, dh.db_path)
	# elif fun == w.change:
	#     b = 0
	#     i = 0
	#     for entry in entries:
	#         if b == 0:
	#             id = entry[1].get()
	#             b = 1
	#         else:
	#             field = dh.fields[i]
	#             try:
	#                 text=entry[1].get()
	#             except:
	#                 label.configure(text=w.error, fg=w.error_col)
	#             entry[1].delete(0, 'end')
	#             cat[field] = text
	#             i += 1
	#     print(id)
	#     for c in cat:
	#         print(c, cat[c])
	#         dt.edit_fields(id, cat, dh.db_path)
	label.configure(text=w.done, fg=w.done_col)
	window.destroy()


# ???
def fetch_change(entries, label, window):
	"""
		Меняет значение для ключа key у поля с указанным пользователем идентификатором
		Устанавливает в label метку об успешном завершении действия
		Параметры: tkinter.Entry entry, tkinter.Label label
		Автор:
	"""
	cat = {}
	b = 0
	for en in entries:
		if b == 0:
			id = en[1].get()
		else:
			text = en[1].get()
			if text != '':
				en[1].delete(0, 'end')
				cat[dh.fields[b - 1]] = text
		b += 1
	for c in cat:
		print(c, cat[c])
	dt.edit_fields(id, cat, dh.db_path)
	label.configure(text=w.done, fg=w.done_col)
	window.destroy()


def fetch_del(entry, label, window):
	"""
		Удаляет запись по указанному пользователем id
		Устанавливает в label метку об успешном завершении действия
		Параметры: tkinter.Entry entry, tkinter.Label label
		Автор:
	"""
	id = entry.get()
	print(id)
	try:
		dt.del_cat(id, dh.db_path)
		label.configure(text=w.done, fg=w.done_col)
	except KeyError:
		label.configure(text=w.error, fg=w.error_col)
	window.destroy()


def makeform(root, fields):
	"""
		Формирует набор полей ввода для каждого элемента из fields в окне root
		Параметры: tkinter.Toplevel root, tuple fields
		Автор:
	"""
	entries = []
	for field in fields:
		row = Frame(root)
		lab = Label(row, width=w.WIDTH30, text=field, bg=w.bg_col, anchor='w')
		ent = Entry(row, fg=w.bg_col)
		row.pack(side=TOP, fill=X, padx=5, pady=5)
		lab.pack(side=LEFT)
		ent.pack(side=RIGHT, expand=YES, fill=X)
		entries.append((field, ent))
	return entries


def create_win(title, field, fun, ph_sumbit):
	"""
		Формирует окно с заголовком title и полями ввода для каждого элемента из field
		и привязывает окно к определенному действию в зависимости от fun
		Отображает кнопки с фонами ph_quit и ph_sumbit
		Параметры: str title, tuple field, str fun, PIL.ImageTk.PhotoImage ph_quit, PIL.ImageTk.PhotoImage ph_sumbit
		Автор:
	"""
	win = Toplevel()
	win.wm_title(title)
	win.configure(background=w.bg_col)
	ents = makeform(win, field)
	l1 = Label(win, text='', bg=w.bg_col)
	l1.pack(side=LEFT, padx=5, pady=5)
	# win.bind('<Button-1>', (lambda event, e=ents, l=l1: fetch_add(e, l)))
	# b2 = Button(win, image=ph_quit, command=win.destroy)
	# b2.pack(side=RIGHT, padx=5, pady=5)
	if fun == w.add:
		b1 = Button(win, image=ph_sumbit,
					command=(lambda e=ents, l=l1, w=win: fetch_add(e, l, w)))
	elif fun == w.change:
		b1 = Button(win, image=ph_sumbit,
					command=(lambda e=ents, l=l1, w=win: fetch_change(e, l, w)))
	b1.pack(side=RIGHT, padx=5, pady=5)


def del_win(ph_quit, ph_sumbit):
	"""
		Формирует окно с с полем ввода названия кота для удаления соответствующей
		записи из базы
		Отображает кнопки с фонами ph_quit и ph_sumbit
		Параметры: PIL.ImageTk.PhotoImage ph_quit, PIL.ImageTk.PhotoImage ph_sumbit
		Автор:
	"""
	win = Toplevel()
	win.wm_title(w.title_del)
	win.configure(background=w.bg_col)
	row = Frame(win)
	lab = Label(row, text=w.ident, bg=w.bg_col, anchor='w', font=(w.font_ab, 10))
	ent = Entry(row)
	row.pack(side=TOP, fill=X, padx=5, pady=5)
	lab.pack(side=LEFT)
	ent.pack(side=RIGHT, expand=YES, fill=X)
	l1 = Label(win, text='', bg=w.bg_col)
	l1.pack(side=LEFT, padx=5, pady=5)
	# b2 = Button(win, image=ph_quit, command=win.destroy)
	# b2.pack(side=RIGHT, padx=5, pady=5)
	b1 = Button(win, image=ph_sumbit,
				command=(lambda e=ent, l=l1, w=win: fetch_del(e, l, w)))
	b1.pack(side=RIGHT, padx=5, pady=5)


def change_win(title, field, ph_sumbit):  # не тот код
	"""
		Формирует окно для задания новых параметров
		Отображает кнопки с фоном ph_sumbit
		Параметры: PIL.ImageTk.PhotoImage ph_quit, PIL.ImageTk.PhotoImage ph_sumbit
		Автор:
	"""
	win = Toplevel()
	win.wm_title(title)
	win.configure(background=w.bg_col)
	ents = makeform(win, field)
	l1 = Label(win, text='', bg=w.bg_col)
	l1.pack(side=LEFT, padx=5, pady=5)
	# win.bind('<Button-1>', (lambda event, e=ents, l=l1: fetch_add(e, l)))
	# b2 = Button(win, image=ph_quit, command=win.destroy)
	# b2.pack(side=RIGHT, padx=5, pady=5)
	b1 = Button(win, image=ph_sumbit,
				command=(lambda e=ents, l=l1, w=win: fetch_add(e, l, w)))
	b1.pack(side=RIGHT, padx=5, pady=5)


def show_table(ph_quit):
	"""
		Выводит текущую таблицу
		Отображает кнопку с фоном ph_quit
		Параметры: PIL.ImageTk.PhotoImage ph_quit
		Автор:
	"""
	win = Toplevel()
	win.wm_title(w.title_curr)
	rows = []
	index = 0
	cols = []
	for i in range(w.COLUMNS):
		e = Label(win, bg=w.bg_col, text="  " + w.fields_n[i] + "  ")
		e.grid(row=0, column=i, sticky=NSEW)
	for key in dh.get_dict_from_db(dh.db_path):
		if key != dh.last_id_field:
			for j in range(w.COLUMNS):
				if j == 0:
					index += 1
					e = Label(win, bg=w.bg_table, text="  " + str(index) + "  ")
				elif j == 1:
					e = Label(win, bg=w.bg_table, text="  " + key + "  ")
				else:
					e = Label(win, bg=w.bg_table, text=dh.get_dict_from_db(dh.db_path)[str(key)][dh.fields[j - 2]])
				e.grid(row=int(key) + 1, column=j, sticky=NSEW)
				cols.append(e)
		rows.append(cols)
	b2 = Button(win, image=ph_quit, command=win.destroy)
	b2.grid(row=len(rows) + 15, column=w.COLUMNS - 1)


def select_options():
	"""
		Создает окно для задания параметров выборки
		Отображает кнопку с фоном ph_quit
		Параметры: PIL.ImageTk.PhotoImage ph_quit
		Автор:
	"""
	print("kek")


def select_result(ph_quit):
	"""
		Выводит результаты выборки по критерию
		Отображает кнопку с фоном ph_quit
		Параметры: PIL.ImageTk.PhotoImage ph_quit
		Автор:
	"""
	win = Toplevel()
	win.wm_title(w.title_curr)
	rows = []
	b = 0
	id = 0
	for i in range(dh.get_count(dh.db_path) + 1):
		cols = []
		for j in range(len(dh.fields) + 1):
			if b == 0:
				e = Label(win, bg=w.bg_table, text="  " + w.fields_n[j] + "  ")
				e.grid(row=i, column=j, sticky=NSEW)
			else:
				if j == 0:
					id += 1
					e = Label(win, bg=w.bg_table, text="  " + str(id) + "  ")
				else:
					e = Label(win, bg=w.bg_table, text=dh.get_dict_from_db(dh.db_path)[str(i - 1)][dh.fields[j - 1]])
				e.grid(row=i, column=j, sticky=NSEW)
			cols.append(e)
		b = 1
		rows.append(cols)
	b2 = Button(win, image=ph_quit, command=win.destroy)
	b2.grid(row=i + 1, column=w.COLUMNS - 1)


def format_db(ph_ok):
	"""
		Возвращает базу данных к первоначальному состоянию
		Отображает кнопку с фоном ph_ok
		Параметры: PIL.ImageTk.PhotoImage ph_ok
		Автор:
	"""
	win = Toplevel()
	dt.clear_db()
	win.configure(background=w.bg_col)
	win.wm_title(w.title_form)
	l1 = Label(win, text=w.done_form, font=(w.font_ab, 12), bg=w.bg_col)
	l1.pack(padx=10, pady=10)
	b2 = Button(win, image=ph_ok, command=win.destroy)
	b2.pack(padx=5, pady=5)
