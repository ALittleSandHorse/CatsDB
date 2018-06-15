from tkinter import *

from Library import db_helper as dh, win_constants as w
from Library import db_tools as dt

"""
	Библиотека методов для создания графического интерфейса и взаимодействия с ним
	Автор: Магомедов Шамиль, Духнай Екатерина
"""

def fetch_add(entries, label, window):
    """
        Получает введенные пользователем значения из entries
        Проверяет все поля ввода на валидность и добавляет их в словарь котов
        Устанавливает в label метку об успешном завершении действия или об ошибках
        По завершении действий закрывает окно window
        Параметры: list entries, tkinter.Label label, tkinter.Toplevel window
        Возвращаемое значение: -
        Автор: Магомедов Шамиль
    """
    cat = {}
    i = 0
    f = 0
    w1=0
    count=0
    for entry in entries:
        field = dh.fields[i]
        text = entry[1].get()
        if text == w.empty_str:
            f = -1
        else:
            if count==2:
                if dh.isFloat(text)==False:
                    w1 = -1
                    entry[1].delete(0, 'end')
            cat[field] = text
            i += 1
        count+=1
    if w1==-1:
        label.configure(text=w.error_weight, fg=w.error_col)

    elif f==-1:
        label.configure(text=w.no_fill, fg=w.error_col)
    else:
        for c in cat:
            print(c, cat[c])
        dt.add_cat(cat, dh.db_path)
        label.configure(text=w.done, fg=w.done_col)
        window.destroy()



def fetch_change(entries, label, window):
    """
        Меняет значение для ключа key у поля с указанным пользователем идентификатором с проверкой вводимого значения
        Устанавливает в label метку об успешном завершении действия или об ошибках
        По завершении действий закрывает окно window
        Параметры: tkinter.Entry entry, tkinter.Label label, tkinter.Toplevel window
        Возвращаемое значение: -
        Автор: Магомедов Шамиль
    """
    cat = {}
    b = 0 #счетчик
    f = 0 #флаг для пустого идентификатора
    fw= 0 #проверка массы на float
    fid=0 #проверка идентификатора на положительный int
    count=0 #количество пустых полей для изменения
    for en in entries:
        if b == 0:
            id = en[1].get()
            if id == w.empty_str:
                label.configure(text=w.no_ident, fg=w.error_col)
                f = -1
            elif id.isdigit() == False or int(id)<=0:
                fid=-1
        else:
            text = en[1].get()
            if text != w.empty_str:
                if b== 3:
                    if dh.isFloat(text)==False:
                        fw=-1
                        en[1].delete(0, 'end')
                cat[dh.fields[b - 1]] = text
            else:
                count+=1
        b += 1
    if fid==-1:
        label.configure(text=w.error_id, fg=w.error_col)
    elif fw == -1:
        label.configure(text=w.error_weight, fg=w.error_col)
    elif count == 5 and f != -1:
        label.configure(text=w.no_edit_fields, fg=w.error_col)
    elif f != -1 and count != 5:
        dt.edit_fields(id, cat, dh.db_path)
        label.configure(text=w.done, fg=w.done_col)
        window.destroy()




def fetch_del(entry, label, window):
    """
        Удаляет запись по указанному пользователем идентификатору с проверкой вводимого значения
        Устанавливает в label метку об успешном завершении действия или об ошибке
        По завершении действий закрывает окно window
        Параметры: tkinter.Entry entry, tkinter.Label label, tkinter.Toplevel window
        Возвращаемое значение: -
        Автор: Магомедов Шамиль
    """
    id = entry.get()
    if id == w.empty_str:
        label.configure(text=w.no_ident, fg=w.error_col)
    elif id.isdigit() == False or int(id) <= 0:
        label.configure(text=w.error_id, fg=w.error_col)
        entry.delete(0, 'end')
    else:
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
        Возвращаемое значение: -
        Автор: Духнай Екатерина
    """
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=w.WIDTH30, text=field, bg=w.bg_col, anchor='w')
        ent = Entry(row, fg=w.bg_col)
        row.pack(side=TOP, fill=X, padx=w.PAD_X5, pady=w.PAD_X5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries.append((field, ent))
    return entries


def create_win(title, field, fun, ph_sumbit):
    """
        Формирует окно с заголовком title и полями ввода для каждого элемента из field
        и привязывает окно к определенному действию в зависимости от fun
        Отображает кнопку с фоном ph_sumbit
        Параметры: str title, tuple field, str fun, PhotoImage ph_sumbit
        Возвращаемое значение: -
        Автор:Духнай Екатерина
    """
    win = Toplevel()
    win.wm_title(title)
    win.configure(background=w.bg_col)
    ents = makeform(win, field)
    l1 = Label(win, text=w.empty_str, bg=w.bg_col)
    l1.pack(side=LEFT, padx=w.PAD_X5, pady=w.PAD_X5)
    if fun == w.add:
        b1 = Button(win, image=ph_sumbit,
                    command=(lambda e=ents, l=l1, w=win: fetch_add(e, l, w)))
    elif fun == w.change:
        b1 = Button(win, image=ph_sumbit,
                    command=(lambda e=ents, l=l1, w=win: fetch_change(e, l, w)))
    b1.pack(side=RIGHT, padx=w.PAD_X5, pady=w.PAD_X5)


def del_win(ph_sumbit):
    """
        Формирует окно с полем ввода идентификатора кота для удаления соответствующей
        записи из базы
        Отображает кнопку с фоном ph_sumbit
        Параметры: PhotoImage ph_quit, .PhotoImage ph_sumbit
        Возвращаемое значение: -
        Автор: Духнай Екатерина
    """
    win = Toplevel()
    win.wm_title(w.title_del)
    win.configure(background=w.bg_col)
    row = Frame(win)
    lab = Label(row, text=w.ident, bg=w.bg_col, anchor='w', font=(w.font_ab, w.FONT_SIZE))
    ent = Entry(row)
    row.pack(side=TOP, fill=X, padx=w.PAD_X5, pady=w.PAD_X5)
    lab.pack(side=LEFT)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    l1 = Label(win, text=w.empty_str, bg=w.bg_col)
    l1.pack(side=LEFT, padx=w.PAD_X5, pady=w.PAD_X5)
    b1 = Button(win, image=ph_sumbit,
                command=(lambda e=ent, l=l1, w=win: fetch_del(e, l, w)))
    b1.pack(side=RIGHT, padx=w.PAD_X5, pady=w.PAD_X5)

def show_table(ph_quit, cats):
    """
        Выводит таблицу с данными
        Отображает кнопку с фоном ph_quit
        Параметры: PhotoImage ph_quit, dict cats
        Возвращаемое значение: -
        Автор: Магомедов Шамиль
    """
    win = Toplevel()
    win.wm_title(w.title_curr)
    win.configure(background=w.bg_col)
    if not cats:
        l1 = Label(win, text=w.empty_sel, font=(w.font_ab, w.FONT_SIZE_LARGE), bg=w.bg_col)
        l1.pack(padx=w.PAD_Y, pady=w.PAD_Y)
        b2 = Button(win, image=ph_quit, command=win.destroy)
        b2.pack(padx=w.PAD_X5, pady=w.PAD_X5)
    else:
        rows = []
        index = 0
        cols = []
        for i in range(w.COLUMNS):
            e = Label(win, bg=w.bg_col, text="  " + w.fields_n[i] + "  ")
            e.grid(row=0, column=i, sticky=NSEW)
        for key in cats:
            if key != dh.last_id_field:
                for j in range(w.COLUMNS):
                    if j == 0:
                        index += 1
                        e = Label(win, bg=w.bg_table, text="  " + str(index) + "  ")
                    elif j == 1:
                        e = Label(win, bg=w.bg_table, text="  " + key + "  ")
                    else:
                        e = Label(win, bg=w.bg_table, text=cats[str(key)][dh.fields[j - 2]])
                    e.grid(row=int(key) + 1, column=j, sticky=NSEW)
                    cols.append(e)
            rows.append(cols)
        b2 = Button(win, image=ph_quit, command=win.destroy)
        b2.grid(row=len(rows) + 15, column=w.COLUMNS - 1)


def select_options(ph_sumbit, ph_quit):
    """
		Создает окно для задания параметров выборки
		Отображает кнопки с фоном ph_sumbit
		Собирает выбранные опции для дальнейшей выборки
		Параметры: PhotoImage ph_sumbit, PhotoImage ph_quit
		Возвращаемое значение: -
		Автор: Духнай Екатерина
	"""

    win = Toplevel()
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
    r1.grid(row=1, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X15, pady=w.PAD_Y)

    l2 = Label(win, text=w.weight_range, bg=w.bg_col)
    l2.grid(row=2, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X15, pady=w.PAD_Y)

    l3 = Label(win, text=w.w_from, bg=w.bg_col)
    l3.grid(row=3, column=0, sticky=NSEW, padx=w.PAD_X5, pady=w.PAD_Y)

    ent_from = Entry(win, fg=w.bg_col, width=w.W10)
    ent_from.grid(row=3, column=1, sticky=NSEW, columnspan=1, pady=w.PAD_Y)

    l4 = Label(win, text=w.w_to, bg=w.bg_col)
    l4.grid(row=3, column=2, sticky=NSEW, padx=w.PAD_X5, pady=w.PAD_Y)

    ent_to = Entry(win, fg=w.bg_col, width=w.W10)
    ent_to.grid(row=3, column=3, sticky=NSEW, padx=w.PAD_X5, pady=w.PAD_Y)

    r2 = Radiobutton(win, text=w.sel_keyword, variable=radioVar, value=3, bg=w.bg_col)
    r2.grid(row=4, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X15, pady=w.PAD_Y)

    ent_key = Entry(win, fg=w.bg_col, width=w.W10)
    ent_key.grid(row=5, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X15, pady=w.PAD_Y)

    l5 = Label(win, text=w.in_category, bg=w.bg_col)
    l5.grid(row=6, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X15, pady=w.PAD_Y)

    check_name = Checkbutton(win, text=w.fields[0], variable=v1, onvalue=1, offvalue=0, background=w.bg_col)
    check_name.grid(row=7, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X15, pady=w.PAD_Y)

    check_genus = Checkbutton(win, text=w.fields[1], variable=v2, onvalue=1, offvalue=0, background=w.bg_col)
    check_genus.grid(row=8, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X15, pady=w.PAD_Y)

    check_color = Checkbutton(win, text=w.fields[3], variable=v3, onvalue=1, offvalue=0, background=w.bg_col)
    check_color.grid(row=9, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X15, pady=w.PAD_Y)

    check_habitat = Checkbutton(win, text=w.fields[4], variable=v4, onvalue=1, offvalue=0, background=w.bg_col)
    check_habitat.grid(row=10, column=1, sticky=NSEW, columnspan=3, padx=w.PAD_X15, pady=w.PAD_Y)

    l1 = Label(win, text=w.empty_str, bg=w.bg_col)
    l1.grid(row=11, column=0, columnspan=3, padx=w.PAD_Y)

    b1 = Button(win, image=ph_sumbit,
                command=(
                    lambda r=radioVar, w=ent_from, t=ent_to, s=ent_key, l=[v1, v2, v3, v4], p=ph_quit, lab=l1, win=win: select_result(r,w,t, s,l,p,lab,win)))
    b1.grid(row=11, column=3)



def select_result(radioVar, w_from, w_to, str, check_list, ph_quit,lab,win):
    """
        Выводит результаты выборки по критерию
        Отображает кнопку с фоном ph_quit
        Параметры: tkinter.IntVar radioVar, tkinter.Entry w_from, tkinter.Entry w_to, str str,
                   list check_list, PhotoImage ph_quit, tkinter.Label lab, tkinter.Toplevel win
        Возвращаемое значение: -
        Автор:Духнай Екатерина
    """
    if radioVar.get() == 1:
        lab.configure(text=w.error_criterion, fg=w.error_col)
    elif radioVar.get() == 2:
        if w_from.get()==w.empty_str or w_to.get()==w.empty_str:
            lab.configure(text=w.error_from_to, fg=w.error_col)
        elif  dh.isFloat(w_from.get())==False or dh.isFloat(w_to.get())==False or w_from.get()>w_to.get():
            lab.configure(text=w.error_wrong_d, fg=w.error_col)
        else:
            text = w_from.get().replace(",", ".")
            wf=float(text)
            text= w_to.get().replace(",", ".")
            wt=float(text)
            cats = dh.get_cats_by_weight(wf, wt, dh.db_path)
            cats_dict = dh.from_ls_dict_to_dict(cats)
            show_table(ph_quit, cats_dict)
            win.destroy()
    elif radioVar.get() == 3:
        flds = []
        count=0 #количество выбранных пунктов
        for i in range(4):
            if check_list[i].get() == 1:
                flds.append(dh.fields_wo_weight[i])
                count+=1
                print(dh.fields_wo_weight[i])
        if str.get()==w.empty_str:
            lab.configure(text=w.no_keyword, fg=w.error_col)
        elif count==0:
            lab.configure(text=w.error_choose, fg=w.error_col)
        else:
            cats = dh.search(str.get(), flds, dh.db_path)
            cats_dict = dh.from_ls_dict_to_dict(cats)
            show_table(ph_quit, cats_dict)
            win.destroy()



def format_db(ph_ok):
    """
        Возвращает базу данных к первоначальному состоянию
        Отображает кнопку с фоном ph_ok
        Параметры: PhotoImage ph_ok
        Возвращаемое значение: -
        Автор: Духнай Екатерина
    """
    win = Toplevel()
    dt.clear_db()
    win.configure(background=w.bg_col)
    win.wm_title(w.title_form)
    l1 = Label(win, text=w.done_form, font=(w.font_ab, w.FONT_SIZE_LARGE), bg=w.bg_col)
    l1.pack(padx=w.PAD_Y, pady=w.PAD_Y)
    b2 = Button(win, image=ph_ok, command=win.destroy)
    b2.pack(padx=w.PAD_X5, pady=w.PAD_X5)


def stats_win(ph_save, ph_sumbit, ph_quit):
    """
    		Создает окно для ввода пользователем имя файла, в который будут созранены результаты работы
    		Отображает кнопки с фонами  ph_sumbit, ph_quit
    		Параметры: PhotoImage ph_sumbit, PhotoImage ph_quit
    		Возвращаемое значение: -
    		Автор:Магомедов Шамиль
    	"""
    win = Toplevel()
    win.wm_title(w.stats)
    win.configure(background=w.bg_col)

    l1 = Label(win, text=w.cats_count+str(dh.get_count(dh.db_path)), font=(w.font_ab, w.FONT_SIZE), bg=w.bg_col)
    l1.pack(padx=w.PAD_Y, pady=w.PAD_Y)

    l3 = Label(win, text=w.mid_weight+w.float_format % dh.get_average(dh.db_path), font=(w.font_ab, w.FONT_SIZE), bg=w.bg_col)
    l3.pack(padx=w.PAD_Y, pady=w.PAD_Y)

    l5 = Label(win, text= w.disp+w.float_format % dh.get_dispersion(dh.db_path), font=(w.font_ab, w.FONT_SIZE), bg=w.bg_col)
    l5.pack(padx=w.PAD_Y, pady=w.PAD_Y)

    b1 = Button(win, image=ph_quit, command=win.destroy)
    b1.pack(side=RIGHT, padx=w.PAD_Y, pady=w.PAD_Y)

    b2 = Button(win, image=ph_save, command=(lambda p=ph_sumbit, win=win:ask_filename(p,win)))
    b2.pack(side=RIGHT, padx=w.PAD_Y, pady=w.PAD_Y)


def ask_filename(ph_sumbit, win_root):
    """
        	Показывает окно с полем ввода названия файла,
        		   куда будут записаны результаты работы
        	Отображает кнопку с фоном  ph_sumbit
        	Параметры: PhotoImage  ph_sumbit, tkinter.Toplevel win_root
        	Возвращаемое значение: -
        	Автор:Магомедов Шамиль
        """
    win = Toplevel()
    win.wm_title(w.title_del)
    win.configure(background=w.bg_col)
    row = Frame(win)
    lab = Label(row, text=w.choose_filename, bg=w.bg_col, anchor='w', font=(w.font_ab, w.FONT_SIZE))
    ent = Entry(row)
    row.pack(side=TOP, fill=X, padx=w.PAD_X5, pady=w.PAD_X5)
    lab.pack(side=LEFT)
    ent.pack(side=RIGHT, expand=YES, fill=X)
    b1 = Button(win, image=ph_sumbit,
                command=(lambda e=ent, win=win,wr=win_root: save_stats(e,win,wr)))
    b1.pack(side=RIGHT, padx=w.PAD_X5, pady=w.PAD_X5)

def save_stats(ent, win, wr):
    """
            Сохраняет результаты работы в файл, имя которого
            	  задал пользователь в ent
            Закрывает текущее окно со статистикой win и окно ввода названия файла wr
            Параметры: tkinter.Entry ent, tkinter.Toplevel win, tkinter.Toplevel wr
            Возвращаемое значение: -
            Автор:Духнай Екатерина
         """
    s=ent.get()
    dh.print_stats_to_txt(s, dh.get_statistics(dh.db_path))
    win.destroy()
    wr.destroy()

