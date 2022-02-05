from asyncio.windows_events import NULL
from tkinter import *
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from tkinter import messagebox


# the main Tkinter window
root = Tk()
root.state('zoomed')
root.resizable(False,False)
root.title('SPC Controller')
root.configure(bg="#212121")
#screen_width = root.winfo_screenwidth()
#screen_height = root.winfo_screenheight()

cnx = mysql.connector.connect(user='root', password='jagapathi',
                              host='192.168.1.3',
                              port='3306',
                              database='lmwind')
cur=cnx.cursor()
cur.execute("SELECT TopLaserWidth,BottomLaserWidth,TopTotalWidth FROM `plank_00001`")
plank = []
frame = []
profile = []

for i in cur:
    plank.append(float(i[0]))
    frame.append(float(i[1]))
    profile.append(float(i[2]))

#dynamic values for plank,frame,profile--from sql
Plank_Id = plank
Frame_Id = frame
Profile_ID = profile

# setting variable for plank
plank_variable = StringVar()
plank_variable.set("Select Coil Id")
# setting variable for Frame
frame_variable = StringVar()
frame_variable.set("Select Blade Type")
# setting variable for profile
Profile_variable = StringVar()
Profile_variable.set("Select Date")



def plot():
    
    frm = Frame(root)
    
    

    if (plank_variable.get()!="Select Plank Id") and (frame_variable.get()!="Select Frame Id") and (Profile_variable.get()!= "Select Profile Id") :

        
        Figure(figsize = (5, 5),dpi = 100)
        y = plank
        mu, std = norm.fit(y)
        fig = plt.figure(figsize=(4.9,4.9))
        plt.title('Plank Width Curve', fontdict={'fontsize':20})
        plt.xlabel('Plank Width', fontsize=18)
        plt.ylabel('Frequency', fontsize=16)
        plt.yticks([])
        plt.hist(y, bins=5, density=True, alpha=0, color='b')
        plt.rcParams.update({'figure.max_open_warning': 0})
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        canvas = FigureCanvasTkAgg(fig, master=frm)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        frm.place(x=50,y=55)
    #---------------------------------------------------------------------------
        frm = Frame(root)
        Figure(figsize = (5, 5),dpi = 100)
        y = profile
        mu, std = norm.fit(y)
        fig = plt.figure(figsize=(4.9,4.9))
        plt.title('Total Width Curve', fontdict={'fontsize':20})
        plt.xlabel('Plank Width', fontsize=18)
        plt.ylabel('Frequency', fontsize=16)
        plt.yticks([])
        plt.hist(y, bins=5, density=True, alpha=0, color='b')
        plt.rcParams.update({'figure.max_open_warning': 0})
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        canvas = FigureCanvasTkAgg(fig, master=frm)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        frm.place(x=650,y=55)
    #------------------------------------------------------------------------------------
        frm = Frame(root)
        Figure(figsize = (5, 5),dpi = 100)
        y = plank
        mu, std = norm.fit(y)
        fig = plt.figure(figsize=(4.9,4.9))
        plt.title('Left Champher Curve', fontdict={'fontsize':20})
        plt.xlabel('Plank Width', fontsize=18)
        plt.ylabel('Frequency', fontsize=16)
        plt.yticks([])
        plt.hist(y, bins=5, density=True, alpha=0, color='b')
        plt.rcParams.update({'figure.max_open_warning': 0})
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        canvas = FigureCanvasTkAgg(fig, master=frm)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        frm.place(x=1250,y=55)
        #----------------------------------------------------------------------------------------
        frm = Frame(root)
        Figure(figsize = (5, 5),dpi = 100)
        y = plank
        mu, std = norm.fit(y)
        fig = plt.figure(figsize=(4.9,4.9))
        plt.title('Right Champher Curve', fontdict={'fontsize':20})
        plt.xlabel('Plank Width', fontsize=18)
        plt.ylabel('Frequency', fontsize=16)
        plt.yticks([])
        plt.hist(y, bins=5, density=True, alpha=0, color='b')
        plt.rcParams.update({'figure.max_open_warning': 0})
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        canvas = FigureCanvasTkAgg(fig, master=frm)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        frm.place(x=50,y=550)
        #--------------------------------------------------------------------
        frm = Frame(root)
        Figure(figsize = (5, 5),dpi = 100)
        y = plank
        mu, std = norm.fit(y)
        fig = plt.figure(figsize=(4.9,4.9))
        plt.title('Top Champher Curve', fontdict={'fontsize':20})
        plt.xlabel('Plank Width', fontsize=18)
        plt.ylabel('Frequency', fontsize=16)
        plt.yticks([])
        plt.hist(y, bins=5, density=True, alpha=0, color='b')
        plt.rcParams.update({'figure.max_open_warning': 0})
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        canvas = FigureCanvasTkAgg(fig, master=frm)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        frm.place(x=650,y=550)
        #------------------------------------------------------------------------------
        frm = Frame(root)
        Figure(figsize = (5, 5),dpi = 100)
        y = plank
        mu, std = norm.fit(y)
        fig = plt.figure(figsize=(4.9,4.9))
        plt.title('Bottom Champher Curve', fontdict={'fontsize':20})
        plt.xlabel('Plank Width', fontsize=18)
        plt.ylabel('Frequency', fontsize=16)
        plt.yticks([])
        plt.hist(y, bins=5, density=True, alpha=0, color='b')
        plt.rcParams.update({'figure.max_open_warning': 0})
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax)
        p = norm.pdf(x, mu, std)
        plt.plot(x, p, 'k', linewidth=2)
        canvas = FigureCanvasTkAgg(fig, master=frm)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        frm.place(x=1250,y=550)
        #----------------------------------------------------------------------------------
       


    
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        button.config(state="normal")
        root.destroy()
        

root.protocol("WM_DELETE_WINDOW", on_closing)


class MyOptionMenu(OptionMenu):
    def __init__(self, master, status, *options):
        self.var = StringVar(master)
        self.var.set(status)
        OptionMenu.__init__(self, master, self.var, *options)
        self.config(font=('calibri',(10)),bg='#FFFFFF',width=12)
        self['menu'].config(font=('calibri',(10)),bg='#FFFFFF')



# creating plank widget
dropdown = OptionMenu(root,plank_variable,*Plank_Id)
dropdown.pack(expand=True)
dropdown.place(x=30,y=10)

# creating frame widget
dropdown = OptionMenu(root,frame_variable,*Frame_Id)
dropdown.pack(expand=True)
dropdown.place(x=200,y=10)

# creating profile widget
dropdown = OptionMenu(root,Profile_variable,*Profile_ID)
dropdown.pack(expand=True)
dropdown.place(x=360,y=10)

button = Button(root, text = 'Plot Graph', bd = '5',command = plot)
button.place(x=520,y=10)





# run the gui
root.mainloop()
