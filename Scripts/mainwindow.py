from tkinter import *
from PIL import Image, ImageTk
from Scripts import win_constants as w
from Library import win_tools as wt

# создание главного окна
root = Tk()
root.configure(background=w.bg_col)

imgframe = Frame()
imgframe.pack(side=TOP)

image1 = Image.open(w.path_img)
image1 = image1.resize((w.WIDTH, w.RESIZE_H400), Image.ANTIALIAS)

photo1 = ImageTk.PhotoImage(image1)

label1 = Label(imgframe, image=photo1, anchor=W)
label1.image1 = photo1
label1.pack()

f = Frame()
f.pack(side=TOP)

img_btn_show = Image.open(w.path_show)
img_btn_show = img_btn_show.resize((w.RESIZE_W200, w.RESIZE_HEIGHT), Image.ANTIALIAS)
ph_show = ImageTk.PhotoImage(img_btn_show)

img_btn_add = Image.open(w.path_add)
img_btn_add = img_btn_add.resize((w.RESIZE_W200, w.RESIZE_HEIGHT), Image.ANTIALIAS)
ph_add = ImageTk.PhotoImage(img_btn_add)

img_btn_ch = Image.open(w.path_change)
img_btn_ch = img_btn_ch.resize((w.RESIZE_W200, w.RESIZE_HEIGHT), Image.ANTIALIAS)
ph_ch = ImageTk.PhotoImage(img_btn_ch)

img_btn_del = Image.open(w.path_del)
img_btn_del = img_btn_del.resize((w.RESIZE_W200, w.RESIZE_HEIGHT), Image.ANTIALIAS)
ph_del = ImageTk.PhotoImage(img_btn_del)

img_btn_form = Image.open(w.path_format)
img_btn_form = img_btn_form.resize((w.RESIZE_W200, w.RESIZE_HEIGHT), Image.ANTIALIAS)
ph_form = ImageTk.PhotoImage(img_btn_form)

img_btn_ok = Image.open(w.path_ok)
img_btn_ok = img_btn_ok.resize((w.RESIZE_W50, w.RESIZE_H30), Image.ANTIALIAS)
ph_ok = ImageTk.PhotoImage(img_btn_ok)

img_btn_sumbit = Image.open(w.path_sumbit)
img_btn_sumbit = img_btn_sumbit.resize((w.RESIZE_W110, w.RESIZE_H30), Image.ANTIALIAS)
ph_sumbit = ImageTk.PhotoImage(img_btn_sumbit)

img_btn_quit = Image.open(w.path_quit)
img_btn_quit = img_btn_quit.resize((w.RESIZE_W110, w.RESIZE_H30), Image.ANTIALIAS)
ph_quit = ImageTk.PhotoImage(img_btn_quit)

img_btn_select = Image.open(w.path_select)
img_btn_select = img_btn_select.resize((w.RESIZE_W200, w.RESIZE_HEIGHT), Image.ANTIALIAS)
ph_select = ImageTk.PhotoImage(img_btn_select)

bshow = Button(f, image=ph_show, command=(lambda k=ph_quit: wt.show_table(k)))
bshow.pack(fill=X)

badd = Button(f, image=ph_add,
              command=(lambda t=w.add_info,n=w.add, f=w.fields,s=ph_sumbit: wt.create_win(t, f,n, s)))
badd.pack(fill=X)

bchange = Button(f, image=ph_ch,
                 command=(
                     lambda t=w.change_info, f=w.fields2,n=w.change, s=ph_sumbit: wt.create_win(t, f, n, s)))
bchange.pack(fill=X)

bdel = Button(f, image=ph_del, command=(lambda q=ph_quit, s=ph_sumbit: wt.del_win(q, s)))
bdel.pack(fill=X)

bform = Button(f, image=ph_form, command=(lambda k=ph_ok: wt.format_db(k)))
bform.pack(fill=X)

bselect = Button(f, image=ph_select, command=(lambda k=ph_ok: wt.format_db(k)))
bselect.pack(fill=X)

root.minsize(width=w.WIDTH, height=w.HEIGHT)
root.maxsize(width=w.WIDTH, height=w.HEIGHT)

root.mainloop()
