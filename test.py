from tkinter import *

root = Tk()
root.state('zoomed')
root.resizable(False,False)
root.title('SPC Controller')
root.config(bg='grey')
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


ctr_left = Frame(center, bg='white', width=(screen_width/3.5), height=((screen_height-30)/2))
label1 = Text(ctr_left,bg='white',height=1)
label1.pack()
ctr_left.grid(row=0, column=0, sticky="nsew")

ctr_left2 = Frame(center2, bg='white', width=(screen_width/3.5), height=((screen_height-30)/2), padx=0, pady=0)
label1 = Label(ctr_left2,bg='white', text="Width").place(x=50,y=50)
ctr_left2.grid(row=1, column=0, sticky="nsew")

ctr_right = Frame(center, bg='#212121', width=(screen_width/1.42), height=((screen_height-30)/2))
label2 = Label(ctr_right,bg='white', text="Width").place(x=50,y=50)
ctr_right.grid(row=0, column=2, sticky="nsew")

ctr_right2 = Frame(center2, bg='#212121', width=(screen_width/1.42), height=((screen_height-30)/2))
label3 = Label(ctr_right2,bg='white', text="Width").place(x=50,y=50)
ctr_right2.grid(row=1, column=2, sticky="nsew")



# frame_top = Frame(root, width=400, height=250)
# frame_top.pack(side="top", expand=1, fill="both")


# ctr_bottom_frame = Frame(ctr_left_Bottom)
# bottomlabel = Label(ctr_bottom_frame,text="hello")
# bottomlabe2 = Label(ctr_bottom_frame,text="hello")
# bottomlabe3 = Label(ctr_bottom_frame,text="hello")
# bottomlabe4 = Label(ctr_bottom_frame,text="hello")
# bottomlabel.grid(row=0, column=0)
# bottomlabe2.grid(row=0, column=1)
# bottomlabe3.grid(row=1, column=0)
# bottomlabe4.grid(row=1, column=1)
# ctr_bottom_frame.bind('<Button-1>', lambda e: box("2"))
# ctr_bottom_frame.pack(fill='x')


#  labelDynamic1=Label(ctr_left_Bottom,text="Hello \t\t Hello \n abcd \n abcd",borderwidth=1,relief="solid",pady=1)
#     labelDynamic1.bind('<Button-1>', lambda e: box(labelDynamic1))
#     labelDynamic2=Label(ctr_left_Bottom,text="Hello \t\t Hello \n abcd \n abcd",borderwidth=1,relief="solid",pady=1)
#     labelDynamic2.bind('<Button-1>', lambda e: box(labelDynamic2))
#     labelDynamic1.pack(fill='x')
#     labelDynamic2.pack(fill='x')


# mainFrame= Frame(ctr_left_Bottom)
# mainFrame.pack(fill=BOTH,expand=1)
# my_canvas = Canvas(mainFrame)
# my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
# myscrollbar=Scrollbar(mainFrame, orient="vertical", command=my_canvas.yview)
# myscrollbar.pack(side=RIGHT,fill=Y)
# my_canvas.configure(yscrollcommand=myscrollbar.set)
# my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
# second_frame = Frame(my_canvas)
# for i in range(20):
#     Label(second_frame,text="hello").pack(fill='x')
# my_canvas.create_window((0,0), window=second_frame, anchor="nw")

# f = Figure(figsize=(4,4), dpi=100)
#         a = f.add_subplot(111)
#         a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
#         a.set_title("fig" + str(i))
#         canvas = FigureCanvasTkAgg(f,master=ctr_right)
#         canvas.draw()
#         canvas.get_tk_widget().pack(side=TOP, fill=X, expand=1)
#         scrollable_frame.window_create(END, window=canvas.get_tk_widget())
#         scrollable_frame.insert(END, '\n')

root.mainloop()