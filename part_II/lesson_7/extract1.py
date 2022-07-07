# uncompyle6 version 3.8.0
# Python bytecode 3.7.0 (3394)
# Decompiled from: Python 3.6.15 (default, Sep 23 2021, 15:41:43) [GCC]
# Embedded file name: base.py
# Size of source mod 2**32: 227 bytes
__version__ = 'Version:1.1'
import base64
from tkinter import *
from tkinter import filedialog as fd
icon = '\niVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAJvUlEQVR42pVXC3BU1Rn+7j6z2d08N5tsNo8lQBJiIBCwRh5aoZZix6FlRJ06HVptq1bQttNqp0xtrbT10XZsOz7QKshoRUUeQWIUIw95JBAIBAOBkEA2ye4m+37v3Xvv3v737oKxJlHOzL/37r3n/P93vvO/LoOvO6xrbwHEJQDTSFIDRlFKVwM9i0AUXBD5fohcN4RoO8a27qUVCRLhq9QyU74tvd8ARn0XTbvDZitfPs1mZUrNJiHXqGMqrTkpg16lGHJGGF+AFUORuGLE5cag3SHaL19sJyDNiHa/gehno6SJJxGvDYB13XL6vX92fe33Z9dNx3XVJaJBp2S8wSSElIgU7S1FE5J8CiKpViiVUCkUSNG7S4NO9PT2o7en6zA4z2Z4d2+jqeGJGJkYgPXhB0uKTetvWDDb2jTfhhyDBh5f2nCCS4HjBLonAGRZMi4L5B8wDAONSiWrOXf+Mk52dfndjrOvw7Pjb/ToChtTALCue7R65rQnFjc1ZF3fUCo6xhKMQLj5JA9OTF01LI1U6nPDaSDETOaqJDaytGo4XV50dJ7iBy8c/S88O/9Ay0ZIuIkB0M5nzqj8xy2LG9Uzpxcq/UR3ghMhZGhWSTSrlLJySRgFA4EQ8SQsscIRSJbj04dNSAQCnJ2lRcAfxuGOTt5+/uDr8LVsoLfDV5hgxu18eUlx0avfvvXG0mpbAaIJMLEEKaNdKpUKaDVq+PwRXLY7YR92wuXyIBSOIMdogNlciAqrBeVlJTDmZCOe4JBMclfZ0BMIt9ePA/v3h73Dh55D8PBGsuiSfIL53Ns1W26/benKBQ0VTDwpMixLOyCO1bRjXhDxWc8ATpw4zgbGekaRdDjAOkfAe71Qm7KgtZZAU1qRZ55VOWdOo66m2iYbjieS8tnwhCTHoEPfRTv2t+3oha/11+ADh8lykMnE+H3X1dX+50d3LhE8YU6RYFOMRK3kTLE4h/bjZ3Dq2B4XhVQv4v1dtKI/c5Y+EpZES1IAQ8NN0NWsqJ+3tHbe3Dr5mOIsSyyKUNB9ti4LBw51oL+7eSsC+56kNX0ZAOs+uGvVim9Ns5lUCY6RvVxaDJHBwSNdONW+YwjBQ0chhI/R7FMklzLG45nQUpLoZBBa61zkLPxVfeOyRQvmzQGbZJFkOdlx9dk6jLq92PvBO4MYe+sRmv8pI2W4iorytkd+skJ0+VhFLC5QfIuy83Sf6cfe1q1j8Ld9SpTtowVHSAZIIpNkOQmIAdm118N4/bMz6m6eq88pJt8JQMmI0JAfWYoL0H26Hf5L219C5PRzBOChx5csbnpi5a0NGPYkwLKC7HQsOeB7u1p5X/+2DsTO7SbFH5P0ksQmy2rjIisbBbfdazA3PlNd942sYCCGRCIh+4OpqBAe9yBGencdhf/j30sM7Fy9asVtc64rV4+6Y+Ao5LK0GvResOPD9193wrPrPVLYQtJOEvgK4+NB5KHkx9tm1t20VJOVS6EYkB3TSFHDMEn0du2yw71tPQFYd+6+NatmWswGpTvAUVzTJL0OH7a142zH5i6Ejr1Byt7PUM9/DeNXhgrF9zxmLpu3oayiFi6HSwagpc3lF+ag6+iuEEY3EwNljwT/sn6NweHhFHE2nUT0Oh22vNmMYP9re8Dat9CjNhLvNRhPj6LVN+sLZu2vb1iEwct2SAVEchKrrQLHjjRzcLz0JAH4hbDhdz9kRlxJhqWc6/azxJ8We/bshDD0/Cak4m/SmqOZs7+2kb/UrMxpHG1a+B30910k+7RBsjG9pgbth5pFOF94RmZgzT0rs5UqjWrIFcOQK4qi/Fwc+bSFALzwMlKxTaSq8xrpzzBwZ75SV+67gQBcPN9LLQMvO4fVZkPXsWYeo5v+KTnh+btXr5zuDUPZbw/J8WopykP3yYOIDm55G4nLz10FYH347xj51x/pnlKcnICmHqUPzNcbCjtn1S/EYN8FYoCDWq1BnqkAvad3R+B593mGJrUsWrxseSCRpYjG0jpN+UbYB85grG/7QYSO/Ek+Auu6X4JRbqDQuYMyYgfSmVD8CgA/LzLbni8umQ6nfQApYiDbaISSqrX9fIsTgdYXGVjue6q8at5jRTTJF4zK63IoCuLhMfSd2X0J7u2/heXeCp3B8izFD+LO1lcQ7nwV6Yw4NQuWB96ZNmPuaoWogd/tpPItoKDIglDIAc9gy1mEOzYyMN/9PaOpdvus+ibGF4zJpVWjVsGoU+J8TzsX8XTv1+TWLZvTuERhHziHsYGWdsrjfyb1B5DuciYz/l29Mf8t27QGo9flQiIapASnhMlSiaHBTsSczW1IXNos+YQelp/uralfcqM2uxChaFxen0dlNexzUPj0ihRGTJJn6P8whi582E8tltRYSI3n2CTGLeTuGytss2/XqI3wuIapIAkw5hXSKQoY6tvrhn/POzRzhwRACfMPflNgmf3X6dVzEQgnqM/j5UqYZ8ii5MEjEGJl+pSpCPp6PvZSIXmc1knpeehLxq1rqUthH9VodE/V1t8Mj2MIsbAfKrUWBcWllJDOIeRo7UL09Fs0uzldDfX1ZVQ8tlbVLFyUZyqDLxCRs1Z2llpuMmORKB2/CIOOwdnT+wSMviYBeJekb0IGDPNLkFXTZswtrSuzNcJl7yPPt1BlDMIx8Mkogp/sQYpthlwN00ONwtvX6PJrn66a2Vig1BgRDEUpJKkySu1YipdjuMiUj+5O2rhv1wvg/VJXc2aSSNBCXdQA45K3DXmVtsqqGxCPBzAy2JlgvQeOI963k+a04mo/kC4euSha9WSuueGh6lkLmHCERSQao6PkkeKoI+Y5ar2K0dPVDDHUvhuJC0/TmuOZnPD/I10RVfnzkfPNLdm5tkqFUiFEXPvOInLyA3r3EckJXO2IpJG/LBvZNW2VVXOaSixVcI26qclMyskjRU1Fik+i0GTGpQv7kAyeOoboySckCqeIhAyIgvnIW/YKkiMhyilHMmukq9SiC+Ob0q3Wshl3VVTVUcPpluu3SLsWknGZ/hTPIrfAjLGRTkT9n11E+PCVSHBPkQnSIBS6eqopM5BuZE7jS12x9eF/FxWXra2pnU9OR70/FQyBJ6EWm+M48HQEKfovzR4dPoGg+6wXoY8mj4Qvg5DatZyM0SC+8F1gXbuePqw26PVG2Z9E+ZuLl6kn7skHKNmJUnuekr96eIkVPk6x2SwB2DZpJMj54EEGzhfFcUDEidDpSepImkjK5YhQm/LAaPVkVZleM16HNBQCeNdBei91SgNf0FjyMw1cL3P4ep2TrFEjuSCkjjbdXktDmbmXRDHBOkm5H+nuODCBzvHzphz/AxC+sYug/sWGAAAAAElFTkSuQmCC\n'
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
