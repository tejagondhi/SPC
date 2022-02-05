from tkinter import *
from PIL import Image, ImageTk
import math
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

mu = 0
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x, stats.norm.pdf(x, mu, sigma))
plt.show()

root = Tk()
root.state('zoomed')
root.resizable(False,False)
root.title('SPC Controller')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# create all of the main containers
center = Frame(root, width=50, height=40)
center2 = Frame(root, width=50, height=40)
btm_frame2 = Frame(root, bg='#036360', height=30)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

center.grid(row=0, sticky="nsew" )
center2.grid(row=1, sticky="nsew")
btm_frame2.grid(row=2, sticky="nsew")

# create the center widgets
center.grid_rowconfigure(0, weight=1)
center.grid_columnconfigure(0, weight=1)
center.grid_columnconfigure(1, weight=1)
center.grid_columnconfigure(2, weight=1)

center2.grid_rowconfigure(1, weight=1)
center2.grid_columnconfigure(0, weight=1)
center2.grid_columnconfigure(1, weight=1)
center2.grid_columnconfigure(2, weight=1)

ctr_left = Frame(center, bg='white', width=(screen_width/3), height=((screen_height-30)/2))
label1 = Label(ctr_left,bg='white', text="Width").place(x=50,y=50)
label2 = Label(ctr_left,bg='white', text="Thickness").place(x=50,y=90)
label3 = Label(ctr_left,bg='white', text="Champer Top").place(x=50,y=130)
label4 = Label(ctr_left,bg='white', text="Champer Bottom").place(x=50,y=170)

ctr_mid = Frame(center, bg='#212121', width=(screen_width/3), height=((screen_height-30)/2))
ctr_right = Frame(center, bg='white', width=(screen_width/3), height=((screen_height-30)/2))

ctr_left.grid(row=0, column=0, sticky="nsew")
ctr_mid.grid(row=0, column=1, sticky="nsew")
ctr_right.grid(row=0, column=2, sticky="nsew")


ctr_left2 = Frame(center2, bg='#212121', width=(screen_width/3), height=((screen_height-30)/2), padx=0, pady=0)
ctr_mid2 = Frame(center2, bg='white', width=(screen_width/3), height=((screen_height-30)/2))
ctr_right2 = Frame(center2, bg='#212121', width=(screen_width/3), height=((screen_height-30)/2))

ctr_left2.grid(row=1, column=0, sticky="nsew")
#image = Image.open('C:\\Users\\gondh\\Pictures\\Saved Pictures\\iron-man-mask-minimal-zc.jpg')
#image = image.resize(((int)(screen_width/3), (int)((screen_height-30)/2)), Image.ANTIALIAS)
#photo = ImageTk.PhotoImage(image)
#label = Label(ctr_left2, image = photo).place(x=-2,y=-2)

ctr_mid2.grid(row=1, column=1, sticky="nsew")
ctr_right2.grid(row=1, column=2, sticky="nsew")
# for i in range(2):
#     root.grid_rowconfigure(i, weight=1)
#     for j in range(3):
#         root.grid_columnconfigure(j, weight=1)
#         Button(root, text=f'Button {i}-{j}').grid(row=i, column=j, sticky=NSEW)

root.mainloop()
