from email.mime import image
from operator import imod
from select import select
from tkinter import *
from tkinter import filedialog
import shutil
import os
import pyqrcode

from pyqrcode import QRCode
from scipy.fftpack import tilbert

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def generate():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Generating...')
    name = name_field.get()
    url = pyqrcode.create(get_link)
    done = url.png(f"{name}.png",scale=6)
    shutil.move(f"{name}.png", user_path)
    screen.title('QR Code Generated! Generate Another one!?')
    
screen = Tk()
title = screen.title('QRCode Generator')
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

#img
logo_img = PhotoImage(file='ss.png')
#       size
logo_img = logo_img.subsample(3, 3)
canvas.create_image(250, 100, image=logo_img)
#link 
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter The Link :", font={'Arial', 15})

#link label
canvas.create_window(250, 240, window=link_label)
canvas.create_window(250, 265, window=link_field)
#name
name_field = Entry(screen, width=50)
name_label = Label(screen, text="Enter The QR code name :", font={'Arial', 15})
#name label
canvas.create_window(250, 305, window=name_label)
canvas.create_window(250, 330, window=name_field)

#path
path_label = Label(screen, text="Select path for QR code :", font={'Arial', 15})
select_btn =  Button(screen, text="Select", command=select_path)
canvas.create_window(250, 375, window=path_label)
canvas.create_window(250, 410, window=select_btn)



#btn
gen_btn = Button(screen, text="Generate", bg='yellow', padx='22', pady='5',font=('Arial', 15), fg='black', command=generate)
canvas.create_window(250, 460, window=gen_btn)








screen.mainloop()