from tkinter import *
import sys
sys.path.insert(0, '../Library')
import Library.win_tools as wt
import Library.win_constants as w


# создание главного окна
root = Tk()
root.configure(background=w.bg_col)
root.wm_title(w.main_title)

imgframe = Frame()
imgframe.pack(side=TOP)

f = Frame()
f.pack(side=TOP)

#канва
canvas = Canvas(f, width=w.WIDTH, height=w.HEIGHT, bg=w.bg_col)
canvas.pack(expand=YES, fill=BOTH)

#картинка для фона
image = PhotoImage(file=w.path_img)
canvas.create_image(0, 0, anchor=NW, image=image)

img_add = PhotoImage(file=w.path_add)

img_show = PhotoImage(file=w.path_show)

img_change = PhotoImage(file=w.path_change)

img_del = PhotoImage(file=w.path_del)

img_format = PhotoImage(file=w.path_format)

img_ok = PhotoImage(file=w.path_ok)

img_sumbit = PhotoImage(file=w.path_sumbit)

img_quit = PhotoImage(file=w.path_quit)

img_select = PhotoImage(file=w.path_select)

# TODO add button save
img_save = PhotoImage(file=w.path_select)


bshow = Button(f, image=img_show, command=(lambda k=img_quit: wt.show_table(k)))
bshow.pack()
canvas.create_window((20, 230), anchor="nw", window=bshow)


badd = Button(f, image=img_add,command=(lambda t=w.add_info, n=w.add, f=w.fields, s=img_sumbit: wt.create_win(t, f, n, s)))
badd.pack()
canvas.create_window((20, 280), anchor="nw", window=badd)


bchange = Button(f, image=img_change,command=(lambda t=w.change_info, f=w.fields2, n=w.change, s=img_sumbit: wt.create_win(t, f, n, s)))
bchange.pack()
canvas.create_window((20, 330), anchor="nw", window=bchange)


bdel = Button(f, image=img_del, command=(lambda s=img_sumbit: wt.del_win(s)))
bdel.pack()
canvas.create_window((20, 380), anchor="nw", window=bdel)


bform = Button(f, image=img_format, command=(lambda k=img_ok: wt.format_db(k)))
bform.pack()
canvas.create_window((20, 430), anchor="nw", window=bform)


bselect = Button(f, image=img_select, command=(lambda s=img_sumbit, q=img_quit: wt.select_options(s,q)))
bselect.pack()
canvas.create_window((20, 480), anchor="nw", window=bselect)

bstats = Button(f, image=img_select, command=(lambda s=img_save, q=img_quit: wt.stats_win(s,q)))
bstats.pack()
canvas.create_window((20, 530), anchor="nw", window=bstats)


root.minsize(width=w.WIDTH, height=w.HEIGHT)
root.maxsize(width=w.WIDTH, height=w.HEIGHT)

root.mainloop()
