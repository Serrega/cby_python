# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.6.15 (default, Sep 23 2021, 15:41:43) [GCC]
# Embedded file name: base.py
# Size of source mod 2**32: 227 bytes
__version__ = 'Version:1.1'
import base64
from tkinter import *
from tkinter import filedialog as fd
icon = '\n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\n'
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


b1 = Button(text='??????????????', command=insert_img)
b1.grid(row=3, column=0, sticky=E, padx=5, pady=8)
b2 = Button(text='??????????????????', command=extract_text)
b2.grid(row=3, column=1, sticky=E, padx=5, pady=8)
erase_button = Button(text='????????????????', command=erase)
erase_button.grid(row=3, column=2, padx=35, pady=8, sticky='W')
scrollb = Scrollbar(root, command=(calculated_text.yview))
scrollb.grid(row=4, column=4, sticky='nsew')
calculated_text.grid(row=4, column=0, sticky='nsew', columnspan=3)
calculated_text.configure(yscrollcommand=(scrollb.set))
img = PhotoImage(data=icon)
root.tk.call('wm', 'iconphoto', root._w, img)
root.mainloop()