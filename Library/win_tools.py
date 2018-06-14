from tkinter import *

from Library import db_helper as dh, win_constants as w
from Library import db_tools as dt


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
    f = 0
    for entry in entries:
        field = dh.fields[i]
        text = entry[1].get()
        if text == '':
            f = -1
        else:
            entry[1].delete(0, 'end')
            cat[field] = text
            i += 1
    if f == 0:
        for c in cat:
            print(c, cat[c])
        dt.add_cat(cat, dh.db_path)
        label.configure(text=w.done, fg=w.done_col)
        window.destroy()
    else:
        label.configure(text=w.no_fill, fg=w.error_col)


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
		Параметры: str title, tuple field, str fun, PhotoImage ph_quit, PhotoImage ph_sumbit
		Автор:
	"""
    win = Toplevel()
    win.wm_title(title)
    win.configure(background=w.bg_col)
    ents = makeform(win, field)
    l1 = Label(win, text='', bg=w.bg_col)
    l1.pack(side=LEFT, padx=5, pady=5)
    if fun == w.add:
        b1 = Button(win, image=ph_sumbit,
                    command=(lambda e=ents, l=l1, w=win: fetch_add(e, l, w)))
    elif fun == w.change:
        b1 = Button(win, image=ph_sumbit,
                    command=(lambda e=ents, l=l1, w=win: fetch_change(e, l, w)))
    b1.pack(side=RIGHT, padx=5, pady=5)


def del_win(ph_sumbit):
    """
		Формирует окно с с полем ввода названия кота для удаления соответствующей
		записи из базы
		Отображает кнопки с фонами ph_quit и ph_sumbit
		Параметры: PhotoImage ph_quit, .PhotoImage ph_sumbit
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
    b1 = Button(win, image=ph_sumbit,
                command=(lambda e=ent, l=l1, w=win: fetch_del(e, l, w)))
    b1.pack(side=RIGHT, padx=5, pady=5)


def change_win(title, field, ph_sumbit):  # не тот код
    """
		Формирует окно для задания новых параметров
		Отображает кнопки с фоном ph_sumbit
		Параметры: PhotoImage ph_quit, PhotoImage ph_sumbit
		Автор:
	"""
    win = Toplevel()
    win.wm_title(title)
    win.configure(background=w.bg_col)
    ents = makeform(win, field)
    l1 = Label(win, text='', bg=w.bg_col)
    l1.pack(side=LEFT, padx=5, pady=5)
    b1 = Button(win, image=ph_sumbit,
                command=(lambda e=ents, l=l1, w=win: fetch_add(e, l, w)))
    b1.pack(side=RIGHT, padx=5, pady=5)


def show_table(ph_quit):
    """
		Выводит текущую таблицу
		Отображает кнопку с фоном ph_quit
		Параметры: PhotoImage ph_quit
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


def select_options(ph_sumbit, ph_quit):
    """
		Создает окно для задания параметров выборки
		Отображает кнопку с фоном ph_quit
		Параметры: PhotoImage ph_sumbit
		Автор:
	"""

    win = Toplevel()
    check_vars = []
    v1 = IntVar()
    v2 = IntVar()
    v3 = IntVar()
    v4 = IntVar()

    radioVar = IntVar()
    radioVar.set(1)
    win.wm_title(w.title_select)
    win.configure(background=w.bg_col)

    l1 = Label(win, text=w.select, bg=w.bg_col)
    l1.grid(row=0, column=1, sticky=NSEW, columnspan=3, pady=w.PAD_Y)

    r1 = Radiobutton(win, text=w.sel_weight, variable=radioVar, value=2, bg=w.bg_col)
    r1.grid(row=1, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X20, pady=w.PAD_Y)

    l2 = Label(win, text=w.weight_range, bg=w.bg_col)
    l2.grid(row=2, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X20, pady=w.PAD_Y)

    l3 = Label(win, text=w.w_from, bg=w.bg_col)
    l3.grid(row=3, column=0, sticky=NSEW, padx=w.PAD_X5, pady=w.PAD_Y)

    ent_from = Entry(win, fg=w.bg_col, width=w.W10)
    ent_from.grid(row=3, column=1, sticky=NSEW, columnspan=1, pady=w.PAD_Y)

    l4 = Label(win, text=w.w_to, bg=w.bg_col)
    l4.grid(row=3, column=2, sticky=NSEW, padx=w.PAD_X5, pady=w.PAD_Y)

    ent_to = Entry(win, fg=w.bg_col, width=w.W10)
    ent_to.grid(row=3, column=3, sticky=NSEW, padx=w.PAD_X5, pady=w.PAD_Y)

    r2 = Radiobutton(win, text=w.sel_keyword, variable=radioVar, value=3, bg=w.bg_col)
    r2.grid(row=4, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X20, pady=w.PAD_Y)

    ent_key = Entry(win, fg=w.bg_col, width=w.W10)
    ent_key.grid(row=5, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X20, pady=w.PAD_Y)

    l5 = Label(win, text=w.in_category, bg=w.bg_col)
    l5.grid(row=6, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X20, pady=w.PAD_Y)

    check_name = Checkbutton(win, text=w.fields[0], variable=v1, onvalue=1, offvalue=0, background=w.bg_col)
    check_name.grid(row=7, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X20, pady=w.PAD_Y)

    check_genus = Checkbutton(win, text=w.fields[1], variable=v2, onvalue=1, offvalue=0, background=w.bg_col)
    check_genus.grid(row=8, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X20, pady=w.PAD_Y)

    check_color = Checkbutton(win, text=w.fields[3], variable=v3, onvalue=1, offvalue=0, background=w.bg_col)
    check_color.grid(row=9, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X20, pady=w.PAD_Y)

    check_habitat = Checkbutton(win, text=w.fields[4], variable=v4, onvalue=1, offvalue=0, background=w.bg_col)
    check_habitat.grid(row=10, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X20, pady=w.PAD_Y)

    b1 = Button(win, image=ph_sumbit,
                command=(lambda r=radioVar, w=ent_from, t=ent_to, s=ent_key, l=[v1, v2, v3, v4], p=ph_quit: select_result(r, w, t,s, l, p)))

    b1.grid(row=11, column=1)


def select_result(radioVar, w_from, w_to, str, check_list, ph_quit):
    """
		Выводит результаты выборки по критерию
		Отображает кнопку с фоном ph_quit
		Параметры: PhotoImage ph_quit
		Автор:
	"""
    win = Toplevel()
    win.wm_title(w.sel_results)
    cats=[]
    if radioVar.get() == 2:
        cats = dh.get_cats_by_weight(w_from.get(), w_to.get(), dh.db_path)
        print(cats)
    elif radioVar.get() == 3:
        flds=[]
        i = 0
        for i in range(4):
            if check_list[i].get == 1:
                flds.append(dh.fields[i])
                print(dh.fields[i])
            i += 1
        cats = dh.search(str.get(), flds, dh.db_path)
        cats_dict=dh.list_to_dict(cats)
        print(cats)

    rows = []
    b = 0
    id = 0
    for i in range(len(cats_dict) + 1):
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
                    e = Label(win, bg=w.bg_table, text= cats_dict[str(i - 1)][dh.fields[j - 1]])
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
		Параметры: PhotoImage ph_ok
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


def stats_win(ph_save, ph_quit):
    """
    		Выводит результаты о работе в файл
    		Имя файла задает пользователь
    		Параметры: PhotoImage ph_ok
    		Автор:
    	"""
    win = Toplevel()
    win.wm_title(w.stats)
    l1 = Label(win, text=w.disp, font=(w.font_ab, 10), bg=w.bg_col)
    l1.pack(padx=10, pady=10)
