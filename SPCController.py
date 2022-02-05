from calendar import month
from doctest import master
from multiprocessing.sharedctypes import Value
from tkinter import *
from tkinter import messagebox
from scipy.stats import norm
from turtle import bgcolor, color, left, width
from tkcalendar import DateEntry
from  datetime import date
from tkinter import ttk
import mysql.connector
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import matplotlib.image as mpimg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np
from numpy import arange, sin, pi


#meta data variable
metaData = []



def focus_out_entry_box(widget, widget_text):
    if widget['fg'] == 'Black' and len(widget.get()) == 0:
        widget.delete(0, END)
        widget['fg'] = 'Grey'
        widget.insert(0, widget_text)

def reset(widget, widget_text):
    if widget['fg'] == 'Black' and len(widget.get()) > 0:
        widget.delete(0, END)
        widget['fg'] = 'Grey'
        widget.insert(0, widget_text)


def focus_in_entry_box(widget):
    if widget['fg'] == 'Grey':
        widget['fg'] = 'Black'
        widget.delete(0, END)

def getGraphData(queryToexecute):
    #graph variables
    TCWL =[]
    TCWR=[]
    BCWL=[]
    BCWR=[]
    TotalThickness=[]
    TotalWidth=[]
    totalParams=[]
    cnx = mysql.connector.connect(user='root', password='jagapathi',
                              host='192.168.1.3',
                              port='3306',
                              database='lmwind')
    cur=cnx.cursor()
    print(queryToexecute)
    cur.execute(queryToexecute)
    for i in cur:
        TCWL.append(float(i[0]))
        TCWR.append(float(i[1]))
        BCWL.append(float(i[2]))
        BCWR.append(float(i[3]))
        TotalThickness.append(float(i[4]))
        TotalWidth.append(float(i[5]))
    totalParams.append(TCWL)
    totalParams.append(TCWR)
    totalParams.append(BCWL)
    totalParams.append(BCWR)
    totalParams.append(TotalThickness)
    totalParams.append(TotalWidth)
    return totalParams

def getMetaData(nonEmptyData):
    
    cnx = mysql.connector.connect(user='root', password='jagapathi',
                              host='192.168.1.3',
                              port='3306',
                              database='lmwind')
    cur=cnx.cursor()
    query = "SELECT ID,Mode, BladeType, BladeID, CoilID,BatchNumber,Operator,Date FROM `metadata` where "

    for fields in nonEmptyData:
        query += fields[0] + "='"+ fields[1] +"' and "

    finalquery = query[:-4]
    cur.execute(finalquery)
    for i in cur:
        metaData.append(i)
    if(len(metaData)>0):
        return metaData
    else:
        messagebox.showwarning("No data", "No data available for seleted option")


root = Tk()
root.state('zoomed')
root.resizable(False,False)
root.title('SPC Controller')
root.config(bg='grey')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# create all of the main containers
center = Frame(root, width=50, height=40)
btm_frame = Frame(root, bg='#036360', height=30)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)

center.grid_rowconfigure(1, weight=1)
center.grid_columnconfigure(0, weight=1)

center.grid(row=0, sticky="nsew" )
btm_frame.grid(row=2, sticky="nsew")

#create side panel
ctr_left = Frame(center, bg='white', width=(screen_width)/8, height=screen_height-55)
#create main view
ctr_right = Frame(center, bg='#212121', width=(screen_width)/1.3, height=screen_height-55)
#create side panel children
ctr_left_Top = Frame(ctr_left)
ctr_left_Bottom = Frame(ctr_left, height=200)
ctr_left_Top.pack(expand=True, fill=BOTH)
ctr_left_Bottom.pack(expand=1, fill=BOTH)
ctr_left_Bottom.pack_propagate(False)
#ctr_left_Top.pack_propagate(False)
ctr_right.pack_propagate(False)
 
#side panel top layer children
modeTxtField = Entry(ctr_left_Top,bg='white',font='Arial 12', fg='Grey')
modeTxtField.insert(0,"Mode")
modeTxtField.bind("<FocusIn>", lambda args: focus_in_entry_box(modeTxtField))
modeTxtField.bind("<FocusOut>", lambda args: focus_out_entry_box(modeTxtField, "Mode"))
modeTxtField.pack(expand=True, fill='x', padx=10, side=TOP)

bladeIdTxtField = Entry(ctr_left_Top,bg='white',font='Arial 12', fg='Grey')
bladeIdTxtField.insert(0,"Blade Id")
bladeIdTxtField.bind("<FocusIn>", lambda args: focus_in_entry_box(bladeIdTxtField))
bladeIdTxtField.bind("<FocusOut>", lambda args: focus_out_entry_box(bladeIdTxtField, "Blade Id"))
bladeIdTxtField.pack(expand=True, fill='x', padx=10, side=TOP)

bladeTypeTxtField = Entry(ctr_left_Top,bg='white',font='Arial 12', fg='Grey')
bladeTypeTxtField.insert(0,"Blade Type")
bladeTypeTxtField.bind("<FocusIn>", lambda args: focus_in_entry_box(bladeIdTxtField))
bladeTypeTxtField.bind("<FocusOut>", lambda args: focus_out_entry_box(bladeIdTxtField, "Blade Type"))
bladeTypeTxtField.pack(expand=True, fill='x', padx=10, side=TOP)

coilIdTxtField = Entry(ctr_left_Top,bg='white',font='Arial 12', fg='Grey')
coilIdTxtField.insert(0,"Coil Id")
coilIdTxtField.bind("<FocusIn>", lambda args: focus_in_entry_box(coilIdTxtField))
coilIdTxtField.bind("<FocusOut>", lambda args: focus_out_entry_box(coilIdTxtField, "Coil Id"))
coilIdTxtField.pack(expand=True, fill='x', padx=10, side=TOP)

supplierNameTxtField = Entry(ctr_left_Top,bg='white',font='Arial 12', fg='Grey')
supplierNameTxtField.insert(0,"Suplier Name")
supplierNameTxtField.bind("<FocusIn>", lambda args: focus_in_entry_box(coilIdTxtField))
supplierNameTxtField.bind("<FocusOut>", lambda args: focus_out_entry_box(coilIdTxtField, "Suplier Name"))
supplierNameTxtField.pack(expand=True, fill='x', padx=10, side=TOP)

batchnumberTxtField = Entry(ctr_left_Top,bg='white',font='Arial 12', fg='Grey')
batchnumberTxtField.insert(0,"Batch Number")
batchnumberTxtField.bind("<FocusIn>", lambda args: focus_in_entry_box(batchnumberTxtField))
batchnumberTxtField.bind("<FocusOut>", lambda args: focus_out_entry_box(batchnumberTxtField, "Batch Number"))
batchnumberTxtField.pack(expand=True, fill='x', padx=10, side=TOP)

operatorTxtField = Entry(ctr_left_Top,bg='white',font='Arial 12', fg='Grey')
operatorTxtField.insert(0,"Operator")
operatorTxtField.bind("<FocusIn>", lambda args: focus_in_entry_box(operatorTxtField))
operatorTxtField.bind("<FocusOut>", lambda args: focus_out_entry_box(operatorTxtField, "Operator"))
operatorTxtField.pack(expand=True, fill='x', padx=10, side=TOP)

dateField = DateEntry(ctr_left_Top,locale='en_US',font='Arial 12',day=1,month=1,year=2022)
dateField.pack(expand=True, fill='x', padx=10, side=TOP)

# def deleteAllFields():
#     modeTxtField.delete(0,END)
#     bladeIdTxtField.delete(0,END)
#     coilIdTxtField.delete(0,END)
#     batchnumberTxtField.delete(0,END)
#     operatorTxtField.delete(0,END)
#     dateField.delete(0,END)

def clearData(resetButton):
    #deleteAllFields()
    reset(modeTxtField,"Mode")
    reset(bladeIdTxtField,"Blade Id")
    reset(coilIdTxtField,"Coil Id")
    reset(batchnumberTxtField,"Batch Number")
    reset(operatorTxtField,"Operator")
    dt=date(2022,1,1)
    dateField.set_date(dt)
    resetButton.focus()



def listFilterDetails():
    
    if((modeTxtField.get()=="Mode" or modeTxtField.get() == "")
    and (coilIdTxtField.get() =="Coil Id" or coilIdTxtField.get() == "")
    and (bladeIdTxtField.get()== "Blade Id" or bladeIdTxtField.get()== "")
    and (batchnumberTxtField.get() == "Batch Number" or batchnumberTxtField.get() == "")
    and (operatorTxtField.get() == "Operator" or operatorTxtField.get() == "")
    and (str(dateField.get_date())=='2022-01-01') or str(dateField.get_date())<'2022-01-01'):
        messagebox.showerror("ERROR","At least one field is required/ Date cannot be on or before 01-01-2022")
    else:
        nonEmptyData =[]
        fields =[(modeTxtField,"Mode"),
            (coilIdTxtField,"CoilId"),
            (bladeIdTxtField,"BladeID"),
            (batchnumberTxtField,"BatchNumber"),
            (operatorTxtField,"Operator"),
            (dateField,"Date")]
        fieldHints=["Mode","Coil Id","Blade Id","Batch Number","Operator","01-01-2022"]
        for field in fields:
            if(field[0].get() not in fieldHints and field[0].get()!=""):
                if (field[1] == "Date"):
                    dateValue = field[0].get_date().strftime("%d-%m-%Y")
                    nonEmptyData.append((field[1],dateValue))
                    continue
                nonEmptyData.append((field[1],field[0].get()))


        addItemsListView(nonEmptyData)

searchButton = Button(ctr_left_Top,text="SEARCH",bg='white',height=1,border=0,command=listFilterDetails)
searchButton.pack(expand=True, fill='x', padx=10, side=TOP)
resetButton = Button(ctr_left_Top,text="RESET",bg='white',height=1,border=0,command=lambda:clearData(resetButton))
resetButton.pack(expand=True, fill='x', padx=10, side=TOP)

def addItemsListView(nonEmptyData):
    for widget in ctr_left_Bottom.winfo_children():
        widget.destroy()

    data=getMetaData(nonEmptyData)

    scrollbar1 = Scrollbar(ctr_left_Bottom, bg="green")
    scrollbar1.pack( side = RIGHT, fill = Y)
    list = Listbox(ctr_left_Bottom, yscrollcommand = scrollbar1.set)
    for i in data:
        list.insert(END, i)
        ttk.Separator(ctr_left_Bottom,orient="horizontal")
        
    list.bind('<<ListboxSelect>>', graphView)
    list.pack( side = LEFT, fill = BOTH,expand=1,pady=10)
    scrollbar1.config( command = list.yview )
       


#side panel bottom layer children
# def box(id):
#     messagebox.showinfo(id)
    
#render side panel and main view
ctr_left.grid(row=0, column=0, sticky="nsew")
ctr_right.grid(row=0, column=1, sticky="nsew")

def graphView(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    currentData=metaData[index]
    plankPrefix = "00000"
    plankId = plankPrefix[:-len(str(currentData[0]))] + str(currentData[0])
    queryToExecute = "select TCWL,TCWR,BCWL,BCWR,TotalThickness,FinalTotalWidth from plank_"+plankId
    totalParams =getGraphData(queryToExecute)
    for widget in ctr_right.winfo_children():
        widget.destroy()

    scrollable_frame = ScrolledText(ctr_right,height=int(screen_height-55))
    scrollable_frame.pack(fill=BOTH)

    #---------------------------------------------
    Figure(figsize = (7,7),dpi = 100)
    y = totalParams[0]
    mu, std = norm.fit(y)
    fig = plt.figure(figsize=(6.5,6.5))
    plt.title('Top Champher Left', fontdict={'fontsize':20})
    plt.xlabel('TCWL', fontsize=18)
    plt.ylabel('Frequency', fontsize=16)
    plt.yticks([])
    plt.hist(y, bins=5, density=True, alpha=0)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    canvas = FigureCanvasTkAgg(fig, master=ctr_right)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=X, expand=1)
    scrollable_frame.window_create(END, window=canvas.get_tk_widget())
    scrollable_frame.insert(END, '\n')

    #---------------------------------------------
    Figure(figsize = (7,7),dpi = 100)
    y = totalParams[1]
    mu, std = norm.fit(y)
    fig = plt.figure(figsize=(6.5,6.5))
    plt.title('Top Champher Right', fontdict={'fontsize':20})
    plt.xlabel('TCWR', fontsize=18)
    plt.ylabel('Frequency', fontsize=16)
    plt.yticks([])
    plt.hist(y, bins=5, density=True, alpha=0)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    canvas = FigureCanvasTkAgg(fig, master=ctr_right)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=X, expand=1)
    scrollable_frame.window_create(END, window=canvas.get_tk_widget())
    scrollable_frame.insert(END, '\n')
    #---------------------------------------------
    Figure(figsize = (7,7),dpi = 100)
    y = totalParams[2]
    mu, std = norm.fit(y)
    fig = plt.figure(figsize=(6.5,6.5))
    plt.title('Bottom champher Left', fontdict={'fontsize':20})
    plt.xlabel('BCWL', fontsize=18)
    plt.ylabel('Frequency', fontsize=16)
    plt.yticks([])
    plt.hist(y, bins=5, density=True, alpha=0)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    canvas = FigureCanvasTkAgg(fig, master=ctr_right)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=X, expand=1)
    scrollable_frame.window_create(END, window=canvas.get_tk_widget())
    scrollable_frame.insert(END, '\n')
    #---------------------------------------------
    Figure(figsize = (7,7),dpi = 100)
    y = totalParams[3]
    mu, std = norm.fit(y)
    fig = plt.figure(figsize=(6.5,6.5))
    plt.title('Bottom Champher Right', fontdict={'fontsize':20})
    plt.xlabel('BCWR', fontsize=18)
    plt.ylabel('Frequency', fontsize=16)
    plt.yticks([])
    plt.hist(y, bins=5, density=True, alpha=0)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    canvas = FigureCanvasTkAgg(fig, master=ctr_right)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=X, expand=1)
    scrollable_frame.window_create(END, window=canvas.get_tk_widget())
    scrollable_frame.insert(END, '\n')
    #---------------------------------------------
    Figure(figsize = (7,7),dpi = 100)
    y = totalParams[4]
    mu, std = norm.fit(y)
    fig = plt.figure(figsize=(6.5,6.5))
    plt.title('Total Thickness', fontdict={'fontsize':20})
    plt.xlabel('Total Thickness', fontsize=18)
    plt.ylabel('Frequency', fontsize=16)
    plt.yticks([])
    plt.hist(y, bins=5, density=True, alpha=0)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    canvas = FigureCanvasTkAgg(fig, master=ctr_right)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=X, expand=1)
    scrollable_frame.window_create(END, window=canvas.get_tk_widget())
    scrollable_frame.insert(END, '\n')
    #---------------------------------------------
    Figure(figsize = (7,7),dpi = 100)
    y = totalParams[5]
    mu, std = norm.fit(y)
    fig = plt.figure(figsize=(6.5,6.5))
    plt.title('Total Width', fontdict={'fontsize':20})
    plt.xlabel('Total Width', fontsize=18)
    plt.ylabel('Frequency', fontsize=16)
    plt.yticks([])
    plt.hist(y, bins=5, density=True, alpha=0)
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    canvas = FigureCanvasTkAgg(fig, master=ctr_right)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(side=TOP, fill=X, expand=1)
    scrollable_frame.window_create(END, window=canvas.get_tk_widget())
    scrollable_frame.insert(END, '\n')
    
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        

root.protocol("WM_DELETE_WINDOW", on_closing)


root.mainloop()
