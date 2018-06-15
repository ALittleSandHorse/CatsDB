from os.path import dirname, abspath
from tkinter import *
import sys

"""
	Скрипт для инициализации графического интерфейса
	Автор: Магомедов Шамиль и Духнай Екатерина
"""

scripts_folder = dirname(abspath(__file__))
workspace = dirname(scripts_folder)
sys.path.insert(0, workspace)

import Library.win_tools as wt
import Library.win_constants as w
import Library.db_helper as dh

# создание главного окна
root = Tk()
root.configure(background=w.bg_col)
root.wm_title(w.main_title)

imgframe = Frame()
imgframe.pack(side=TOP)

f = Frame()
f.pack(side=TOP)

# канва
canvas = Canvas(f, width=w.WIDTH, height=w.HEIGHT, bg=w.bg_col)
canvas.pack(expand=YES, fill=BOTH)

# картинка для фона
image = PhotoImage(file=workspace + w.path_img)
canvas.create_image(w.ZERO, w.ZERO, anchor=NW, image=image)

img_add = PhotoImage(file=workspace + w.path_add)

img_show = PhotoImage(file=workspace + w.path_show)

img_change = PhotoImage(file=workspace + w.path_change)

img_del = PhotoImage(file=workspace + w.path_del)

img_format = PhotoImage(file=workspace + w.path_format)

img_ok = PhotoImage(file=workspace + w.path_ok)

img_sumbit = PhotoImage(file=workspace + w.path_sumbit)

img_quit = PhotoImage(file=workspace + w.path_quit)

img_select = PhotoImage(file=workspace + w.path_select)

img_stats = PhotoImage(file=workspace + w.path_stats)

img_save = PhotoImage(file=workspace + w.path_save)

bshow = Button(f, image=img_show, command=(lambda k=img_quit: wt.show_table(k, dh.get_dict_from_db(dh.db_path))))
bshow.pack()
canvas.create_window((w.X_MARG, w.Y_1), anchor="nw", window=bshow)

badd = Button(f, image=img_add,
              command=(lambda t=w.add_info, n=w.add, f=w.fields, s=img_sumbit: wt.create_win(t, f, n, s)))
badd.pack()
canvas.create_window((w.X_MARG, w.Y_2), anchor="nw", window=badd)

bchange = Button(f, image=img_change,
                 command=(lambda t=w.change_info, f=w.fields2, n=w.change, s=img_sumbit: wt.create_win(t, f, n, s)))
bchange.pack()
canvas.create_window((w.X_MARG, w.Y_3), anchor="nw", window=bchange)

bdel = Button(f, image=img_del, command=(lambda s=img_sumbit: wt.del_win(s)))
bdel.pack()
canvas.create_window((w.X_MARG, w.Y_4), anchor="nw", window=bdel)

bform = Button(f, image=img_format, command=(lambda k=img_ok: wt.format_db(k)))
bform.pack()
canvas.create_window((w.X_MARG, w.Y_5), anchor="nw", window=bform)

bselect = Button(f, image=img_select, command=(lambda s=img_sumbit, q=img_quit: wt.select_options(s, q)))
bselect.pack()
canvas.create_window((w.X_MARG, w.Y_6), anchor="nw", window=bselect)

bstats = Button(f, image=img_stats, command=(lambda s=img_save, s1=img_sumbit, q=img_quit: wt.stats_win(s,s1, q)))
bstats.pack()
canvas.create_window((w.X_MARG, w.Y_7), anchor="nw", window=bstats)

root.minsize(width=w.WIDTH, height=w.HEIGHT)
root.maxsize(width=w.WIDTH, height=w.HEIGHT)

a=Entry()
print(a.__class__)

root.mainloop()
