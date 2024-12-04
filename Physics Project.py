from tkinter import *
from tkinter  import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt  
import pandas as pd
import math

root = Tk()
root.title("Phy prob")
root.geometry('900x550')
headingLabel=Label(root, text='Determining the Band Gap of Semiconductor', font=('times new roman',30,'bold'), bg='#DEB887', fg='black', bd=12, relief=GROOVE)
headingLabel.pack(fill=X)

templist=[]
tempklist=[]
t1000=[]
Rlist=[]
LogIs=[]

#functions

def plotting():
    x=t1000
    y=LogIs
    plt.xlabel("1000/T")
    plt.ylabel("LogIs")
    plt.plot(x, y)
    plt.show()  

def entry1():
    templist.append(int(TempEntry.get()))
    tempklist.append(int(TempEntry.get())+273)
    r1=1000/((float(TempEntry.get()))+273)
    round1=round(r1,2)
    t1000.append(round1)
    TempEntry.delete(0,END)

def entry2():
    Rlist.append(float(REntry.get()))
    r2=math.log10((float(REntry.get()))*10**(-6))
    round2=round(r2,3)
    LogIs.append(round2)
    REntry.delete(0,END)

def dataframe():
    data = {"Temperature in C":templist, "Temperature in K":tempklist, "1000/T":t1000, "Reverse Saturation Current(x10^-6)":Rlist,"LogIs":LogIs}
    df=pd.DataFrame(data)
    tree = ttk.Treeview(table)
    tree.pack(fill=BOTH, expand=True)

    tree["columns"] = list(df.columns)
    tree["show"] = "headings"  

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    y=LogIs[len(LogIs)-4]-LogIs[len(LogIs)-7]
    x=t1000[len(t1000)-4]-t1000[len(t1000)-7]
    z=(-y)/x
    Eg=2.303*0.198*z

    messagebox.showinfo("Slope value","Slope value = {}".format(z))
    
    round3=round(Eg,4)
    answer=Label(root,text="Eg= 2.3023x 0.198 x slope eV\nEg = {} eV".format(round3),font=('times new roman',15,'bold'),fg='black', bd=8, relief=GROOVE, bg='#DEB887',anchor='w')
    answer.pack(fill="both",expand=True)

    root.mainloop()

#
values=Label(root,bg='#DEB887', bd=12)
values.pack(fill=X)

Temp=Label(values,text="Temperature",font=('times new roman',15,'bold'),bg='#DEB887', fg='black')
Temp.grid(row=0,column=0,sticky='w')
TempEntry=Entry(values,width=30,bd=5)
TempEntry.grid(row=0,column=1,padx=10)
Enter1=Button(values, text="Enter",font=('arial',15,'bold'),bg='#DEB887' ,bd=7, width=5,height=1 , command=entry1)
Enter1.grid(row=0,column=2,padx=20)

R=Label(values,text="Reverse Saturation Current",font=('times new roman',15,'bold'),bg='#DEB887', fg='black')
R.grid(row=1,column=0,pady=30)
REntry=Entry(values,width=30,bd=5)
REntry.grid(row=1,column=1,pady=30,padx=10)
Enter2=Button(values, text="Enter",font=('arial',15,'bold'),bg='#DEB887' ,bd=7, width=5,height=1 , command=entry2)
Enter2.grid(row=1,column=2,padx=20)


#
table=LabelFrame(root,text="Table",font=('times new roman',15,'bold'),fg='black', bd=8, relief=GROOVE, bg='#DEB887')
table.pack(fill=X)
plott=Label(root,bg='#DEB887', bd=12)
plott.pack(fill='both',expand=True)



Table_button=Button(table,text="Show Table",font=('arial',15,'bold'),bg='#DEB887' ,bd=7, width=10, command=dataframe)
Table_button.pack()
plot_button = Button(plott, text="Plot Graph",font=('arial',15,'bold'),bg='#DEB887' ,bd=7, width=10 , command=plotting)
plot_button.pack()

root.mainloop()
