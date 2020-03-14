from tkinter import *
global M,G,CH,Total

def encendido():
    global M,G,CH,Total
    
    CH=0
    M=0
    G=0
    Total=M+CH+G
    l1=Label(ventana,text=CH).grid(column=0,row=2)
    l2=Label(ventana,text=M).grid(column=1,row=2)
    l3=Label(ventana,text=G).grid(column=2,row=2)
    l4=Label(ventana,text=Total).grid(column=1,row=3)
    l5=Label(ventana,text="Total:").grid(column=0,row=3)
    b1.config(state=NORMAL)
    b2.config(state=NORMAL)
    b3.config(state=NORMAL)
def chica():
    global CH,G,M,Total

    CH=CH+1
    Total=M+G+CH
    l1=Label(ventana,text=CH).grid(column=0,row=2)
    l4=Label(ventana,text=Total).grid(column=1,row=3)
    
def mediana():
    global CH,G,M,Total
    M=M+1
    Total=M+G+CH
    l2=Label(ventana,text=M).grid(column=1,row=2)
    l4=Label(ventana,text=Total).grid(column=1,row=3)
    
def grande():
    global CH,G,M,Total
    G=G+1
    Total=M+G+CH
    l3=Label(ventana,text=G).grid(column=2,row=2)
    l4=Label(ventana,text=Total).grid(column=1,row=3)

def apagado():
    global M,G,CH,Total
    Total=0
    CH=0
    M=0
    G=0
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    
ventana=Tk()
ventana.config(width=600, height=800)
b0=Button(ventana,text="iniciar", command=encendido, width=12, height=5)
b0.grid(column=0, row=0)
#b0.place(x=0,y=0)
b1=Button(ventana,text="caja chica", command=chica,width=12, height=5)
b1.grid(column=0,row=1)
#b1.place(x=8,y=0)
b2=Button(ventana,text="caja mediana", command=mediana,width=12, height=5)
b2.grid(column=1,row=1)
#b2.place(x=100,y=1)
b4=Button(ventana,text="apagado", command=apagado,width=12, height=5)
b4.grid(column=1,row=0)
b3=Button(ventana,text="caja grande", command=grande,width=12, height=5)
b3.grid(column=2,row=1)
b1.config(state=DISABLED)
b2.config(state=DISABLED)
b3.config(state=DISABLED)
