from tkinter import *
from tkinter import messagebox

global z
z=0
global y
y=0
global r
r=10

def a1():
    global z
    z=10*z+1
    x=Label(ventana,font=("Arial 30"),text=z).grid(column=0,row=0)
def a2():
    global z
    z=10*z+2
    x=Label(ventana,font=("Arial 30"),text=z).grid(column=0,row=0)
def a3():
    global z
    z=10*z+3
    x=Label(ventana,font=("Arial 30"),text=z).grid(column=0,row=0)
def a4():
    global z
    z=10*z+4
    x=Label(ventana,font=("Arial 30"),text=z).grid(column=0,row=0)
def a5():
    global z
    z=10*z+5
    x=Label(ventana,font=("Arial 30"),text=z).grid(column=0,row=0)
def a6():
    global z
    z=10*z+6
    x=Label(ventana,font=("Arial 30"),text=z).grid(column=0,row=0)
def a7():
    global z
    z=10*z+7
    x=Label(ventana,font=("Arial 30"),text=z).grid(column=0,row=0)
def a8():
    global z
    z=10*z+8
    x=Label(ventana,font=("Arial 30"),text=z).grid(column=0,row=0)
def a9():
    global z
    z=10*z+9
    x=Label(ventana,font=("Arial 30"),text=z).grid(column=0,row=0)
def a0():
    global z
    z=10*z+0
    x=Label(ventana,font=("Arial 30"),text=z).grid(column=0,row=0)
def suma():
    global z
    global y
    global r
    r=1
    if(y==0):
        y=z
        z=0
        x=Label(ventana,font=("Arial 30"),text="          ").grid(column=0,row=0)
        
    else:
        pass   
    
def resta():
    global z
    global y
    global r
    r=2
    if(y==0):
        y=z
        z=0
        x=Label(ventana,font=("Arial 30"),text="          ").grid(column=0,row=0)
        
    else:
        pass
def multiplicacion():
    global z
    global y
    global r
    r=3
    if(y==0):
        y=z
        z=0
        x=Label(ventana,font=("Arial 30"),text="          ").grid(column=0,row=0)
        
    else:
        pass
def division():
    global z
    global y
    global r
    r=4
    if(y==0):
        y=z
        z=0
        x=Label(ventana,font=("Arial 30"),text="          ").grid(column=0,row=0)
        
    else:
        pass
def igual():
    global z
    global y
    global r
    if (r==1):
        x=Label(ventana,font=("Arial 30"),text=z+y).grid(column=0,row=0)
    if (r==2):
        x=Label(ventana,font=("Arial 30"),text=y-z).grid(column=0,row=0)
    if (r==3):
        x=Label(ventana,font=("Arial 30"),text=z*y).grid(column=0,row=0)
    if (r==4):
        try:
            x=Label(ventana,font=("Arial 30"),text=y/z).grid(column=0,row=0)
        except:
            messagebox.showerror(title="advertencia",message="No puedes hacer eso")

def cln():
    global z
    global y
    global r
    z=0
    y=0
    r=0
    if(y==0):
        y=z
        z=0
        x=Label(ventana,font=("Arial 30"),text="          ").grid(column=0,row=0)
    


ventana=Tk()
b1=Button(ventana,text="1",font=("Arial 30"),bg="red",command=a1).grid(column=1,row=4)
b2=Button(ventana,text="2",font=("Arial 30"),bg="blue",command=a2).grid(column=2,row=4)
b3=Button(ventana,text="3",font=("Arial 30"),bg="red",command=a3).grid(column=3,row=4)
b4=Button(ventana,text="4",font=("Arial 30"),bg="blue",command=a4).grid(column=1,row=5)
b5=Button(ventana,text="5",font=("Arial 30"),bg="blue",command=a5).grid(column=2,row=5)
b6=Button(ventana,text="6",font=("Arial 30"),bg="blue",command=a6).grid(column=3,row=5)
b7=Button(ventana,text="7",font=("Arial 30"),bg="red",command=a7).grid(column=1,row=6)
b8=Button(ventana,text="8",font=("Arial 30"),bg="blue",command=a8).grid(column=2,row=6)
b9=Button(ventana,text="9",font=("Arial 30"),bg="red",command=a9).grid(column=3,row=6)
b0=Button(ventana,text="0",font=("Arial 30"),command=a0).grid(column=2,row=7)
bs=Button(ventana,text="+",font=("Arial 30"),command=suma).grid(column=4,row=4)
br=Button(ventana,text="-",font=("Arial 30"),command=resta).grid(column=4,row=5)
bm=Button(ventana,text="*",font=("Arial 30"),command=multiplicacion).grid(column=4,row=6)
bd=Button(ventana,text="/",font=("Arial 30"),command=division).grid(column=4,row=7)
bi=Button(ventana,text="=",font=("Arial 30"),command=igual).grid(column=3,row=7)
bclc=Button(ventana,text="Cln",font=("Arial 15"),command=cln).grid(column=1,row=7)


ventana.mainloop()
