# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.6.15 (default, Sep 23 2021, 15:41:43) [GCC]
# Embedded file name: base.py
# Size of source mod 2**32: 227 bytes
__version__ = 'Version:1.1'
import base64
from tkinter import *
from tkinter import filedialog as fd
icon = 'convert.png'
root = Tk()
root.title('Icon to BASE64  ' + str(__version__))
root.resizable(width=False, height=False)
root.geometry('420x300+300+300')
calculated_text = Text(root, height=15, width=50)
myFormats = [
 ('TXT files', '*.txt'),
 ('HTML files', '*.html;.htm'),
 ('All files', '*.*')]

def insert_img():
    file_name = fd.askopenfilename()
    f = open(file_name, 'rb')
    s = f.read()
    calculated_text.insert('1.0', str(base64.b64encode(s))[2:][:-1])
    f.close()


def extract_text():
    file_name = fd.asksaveasfilename(parent=root, filetypes=myFormats, defaultextension='')
    f = open(file_name, 'w')
    s = calculated_text.get(1.0, END)
    f.write(s)
    f.close()


def erase():
    calculated_text.delete('1.0', END)


b1 = Button(text='Открыть', command=insert_img)
b1.grid(row=3, column=0, sticky=E, padx=5, pady=8)
b2 = Button(text='Сохранить', command=extract_text)
b2.grid(row=3, column=1, sticky=E, padx=5, pady=8)
erase_button = Button(text='Очистить', command=erase)
erase_button.grid(row=3, column=2, padx=35, pady=8, sticky='W')
scrollb = Scrollbar(root, command=(calculated_text.yview))
scrollb.grid(row=4, column=4, sticky='nsew')
calculated_text.grid(row=4, column=0, sticky='nsew', columnspan=3)
calculated_text.configure(yscrollcommand=(scrollb.set))
img = PhotoImage(data=icon)
root.tk.call('wm', 'iconphoto', root._w, img)
root.mainloop()
