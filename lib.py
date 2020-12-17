from tkinter import *
from entity_manager import EntityManager


# Главное окно -----------
window = Tk()
window.geometry('700x500+200+100')
window.title('Зоопарк существ вселенных')
window.config(bg='PaleGreen')


# Картинки -----------
img_groot = PhotoImage(file='groot-gg.png')
img_bowtruckle = PhotoImage(file='Bowtruckle.png')
img_rapier = PhotoImage(file='Рапирник.png')
img_giant_kites = PhotoImage(file='Гигантские воспаритли.png')
img_sagittaria = PhotoImage(file='Сагиттария.png')


# Кнопки -----------
button_grut = Button(window, bd=0, text='Грут', font=("Comic Sans Ms", 12), fg='DarkGreen', bg='PaleGreen',
                     activeforeground='MediumSlateBlue', activebackground='LightCyan', width=30)
button_grut.place(x=0, y=30)

button_bowtruckle = Button(window, bd=0, text='Лечурка', font=("Comic Sans Ms", 12), fg='DarkGreen',
                           activeforeground='MediumSlateBlue', activebackground='LightCyan', width=30, bg='PaleGreen')
button_bowtruckle.place(x=0, y=65)

button_skewer = Button(window, bd=0, text='Рапирник', font=("Comic Sans Ms", 12), fg='DarkGreen',
                       activeforeground='MediumSlateBlue', activebackground='LightCyan', width=30, bg='PaleGreen')
button_skewer.place(x=0, y=100)

button_giant_kites = Button(window, bd=0, text='Гигантские воспаритли', font=("Comic Sans Ms", 12), fg='DarkGreen',
                            activeforeground='MediumSlateBlue', activebackground='LightCyan', width=30, bg='PaleGreen')
button_giant_kites.place(x=0, y=135)

button_sagittaria = Button(window, bd=0, text='Сагиттария', font=("Comic Sans Ms", 12), fg='DarkGreen',
                           activeforeground='MediumSlateBlue', activebackground='LightCyan', width=30, bg='PaleGreen')
button_sagittaria.place(x=0, y=170)


# Текстовое поле -----------
text = Text(window, width=50, height=18, wrap=WORD, font=("Arial", 10), bg='LightCyan',
            fg='DarkGreen', relief=RIDGE, bd=3)  # -> создание текстового поля
scroll = Scrollbar(window, command=text.yview)  # -> создание скроллера
scroll.pack(side=RIGHT, fill=Y)
text.place(x=300, y=20)
text.config(yscrollcommand=scroll.set)  # -> устанавливает скролер в текстовое поле


# Помещение теста в текстовое поле -----------
class TextInsert(object):
    def __init__(self, entity: EntityManager):
        self._text = entity

        text.insert(1.0, entity)  # -> втавляет текст в текстовое поле
        text.tag_add('title', 1.0, '1.end')  # -> указывает часть текста к которой будут применяться свойства
        text.tag_config('title', font=("Comic Sans Ms", 18, 'bold'),
                        justify=CENTER)  # -> свойства для указанной части текста


# Функции вставки текстов в текстовое поле -----------
def insert_text_grut():
    text.delete(1.0, END)
    grut = EntityManager().create_grut()
    text_grut = TextInsert(grut)
    return text_grut


def insert_text_bowtruckle():
    text.delete(1.0, END)
    bowtruckle = EntityManager().create_bowtruckle()
    text_bowtruckle = TextInsert(bowtruckle)
    return text_bowtruckle


def insert_text_skewer():
    text.delete(1.0, END)
    skewer = EntityManager().create_skewer()
    text_skewer = TextInsert(skewer)
    return text_skewer


def insert_text_giant_kites():
    text.delete(1.0, END)
    giant_kites = EntityManager().create_giant_kites()
    text_giant_kites = TextInsert(giant_kites)
    return text_giant_kites


def insert_text_sagittaria():
    text.delete(1.0, END)
    sagittaria = EntityManager().create_sagittaria()
    text_sagittaria = TextInsert(sagittaria)
    return text_sagittaria


# Функции вставки картинок сущностей -----------
def image_grut():
    img_gr = Label(window, image=img_groot, bg='black')
    img_gr.place(x=302, y=325)


def image_bowtruckle():
    img_bowtr = Label(window, image=img_bowtruckle, bg='black')
    img_bowtr.place(x=302, y=325)


def image_rapier():
    img_rap = Label(window, image=img_rapier, bg='black')
    img_rap.place(x=302, y=325)


def image_giant_kites():
    img_g_k = Label(window, image=img_giant_kites, bg='black')
    img_g_k.place(x=302, y=325)


def image_sagittaria():
    img_sag = Label(window, image=img_sagittaria, bg='black')
    img_sag.place(x=302, y=325)


# Конфигурация кнопок -----------
button_grut.config(command=(lambda: (insert_text_grut(), image_grut())))
button_bowtruckle.config(command=(lambda: (insert_text_bowtruckle(), image_bowtruckle())))
button_skewer.config(command=(lambda: (insert_text_skewer(), image_rapier())))
button_giant_kites.config(command=(lambda: (insert_text_giant_kites(), image_giant_kites())))
button_sagittaria.config(command=(lambda: (insert_text_sagittaria(), image_sagittaria())))
