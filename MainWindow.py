from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import mysql.connector
from scipy.stats import norm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure



cnx = mysql.connector.connect(user='root', password='jagapathi',
                              host='192.168.1.2',
                              port='3300',
                              database='lmwind')
cur=cnx.cursor()
cur.execute("SELECT TotalWidth,PlankWidth FROM `lm80`")
total = []
plank = []
  
for i in cur:
    total.append(float(i[0]))
    plank.append(float(i[1]))

#Set the geometry of tkinter frame
root = Tk()
root.state('zoomed')
root.resizable(False,False)
root.title('SPC Controller')
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


def pdf(x):
    mean = np.mean(x)
    std = np.std(x)
    y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
    return y_out

def graph():
    x = plank
    y = pdf(x)
    plt.plot(x, y)
    plt.xlim(right=111.7) #xmax is your value
    plt.xlim(left=111.4) #xmin is your value
    # plt.ylim(top=9) #ymax is your value
    # plt.ylim(bottom=8) #ymin is your value
    #plt.scatter( x, y, marker = 'o', s = 25, color = 'red')
    plt.show()

def graph1():
    # Generate some data for this 
# demonstration.
    data = plank
  
# Fit a normal distribution to
# the data:
# mean and standard deviation
    mu, std = norm.fit(data) 
  
# Plot the histogram.
    plt.hist(data, bins=1, density=True, alpha=0, color='b')
  
# Plot the PDF.
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax)
    p = norm.pdf(x, mu, std)
  
    plt.plot(x, p, 'k', linewidth=2)
    plt.show()

variable = StringVar(root)
variable.set("one") # default value

w = OptionMenu(root, variable, "one", "two", "three")
w.pack()



#Create a button to show the plot
Button(root, text= "Total Width", command= graph).pack(pady=20)
Button(root, text= "Plank Width", command= graph1).pack(pady=20)
root.mainloop()

      
