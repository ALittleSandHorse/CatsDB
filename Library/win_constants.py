"""
	Строковые и числовые константы, использующиеся в графическом интерфейсе
	Автор: Магомедов Шамиль и Духнай Екатерина
"""

fields = ('Название', 'Род', 'Масса', 'Цвет', 'Среда обитания')

fields_n = ('№', 'Идентификатор', 'Название', 'Род', 'Масса', 'Цвет', 'Среда обитания')

fields2 = ('Идентификатор', 'Название', 'Род', 'Масса', 'Цвет', 'Среда')

f_name = ('Название кота')

main_title="База данных лучших котиков"

add = "add"

empty_str=""

float_format="%.2f"

change = "change"

delete = "del"

kek = "kek"

done = "Done"

error = "Неверное значение"

done_col = "#1F6846"

error_col = "#A01010"

bg_col = "#B1A1BC"

bg_table = "#A58888"

title_del = "Удалить существующую запись"

title_select="Выборка"

select="Сделать выборку:"

sel_weight="По массе"

sel_keyword="По ключевому слову"

in_category="В категории (для поиска по слову):"

weight_range="Диапазон масс:"

cats_count="Количество котов: "

mid_weight="Средняя масса кота: "

w_from="От "

w_to=" до"

title_curr = "Текущая таблица"

title_form = "Возврат к первоначальному состоянию"

font_ab = "Arial Bold"

ident = "Идентификатор"

done_form = "Форматирование завершено"

path_img = "/Graphics/Abyssinian_578.gif"

path_show = "/Graphics/btn_show.gif"

path_add = "/Graphics/btn_add.gif"

path_change = "/Graphics/btn_change.gif"

path_del = "/Graphics/btn_del.gif"

path_format = "/Graphics/btn_format.gif"

path_ok = "/Graphics/btn_ok.gif"

path_sumbit = "/Graphics/btn_sumbit.gif"

path_quit = "/Graphics/btn_quit.gif"

path_select = "/Graphics/btn_select.gif"

path_stats = "/Graphics/btn_stats.gif"

path_save = "/Graphics/btn_save.gif"

add_info = "Добавьте информацию о новом коте"

change_info = "Изменить существующую информацию"

no_fill="Заполнены не все поля"

disp="Дисперсия массы котов: "

no_ident="Нет идентификатора"

error_criterion="Выберите критерий"

error_choose="Выберите категорию(и)"

error_from_to="Введите диапазон"

error_wrong_d="Неверный диапазон"

choose_filename="Имя нового файла:"

no_edit_fields="Впишите, что нужно менять"

no_keyword="Впишите ключевое слово"

error_weight="Масса - число >0"

error_id="Идентификатор - целое число >0"

sel_results="Результаты выборки"

empty_sel="Выборка пуста"

stats="Статистика"

WIDTH = 960

HEIGHT = 600

RESIZE_W200 = 200

RESIZE_W50 = 50

RESIZE_W110 = 110

RESIZE_HEIGHT = 40

RESIZE_H30 = 30

RESIZE_H400 = 400

W10=10

COLUMNS = 7

BTN_COL = 5

WIDTH30 = 30

PAD_X5=5

PAD_Y=10

PAD_X15=15

X_MARG=20

ZERO=0

Y_1=240

Y_2=290

Y_3=340

Y_4=390

Y_5=440

Y_6=490

Y_7=540

FONT_SIZE=10

FONT_SIZE_LARGE=12

#TODO: change all path to 'os.get_path()...'