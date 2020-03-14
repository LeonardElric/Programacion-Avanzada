
from tkinter import *

global posx, posy

#matris de 5x5 decidir de que hacerla, de label etc, la del centro de otro color
#agregar 4 botones, arriba abajo derecha izquierda, para mover un color

def iniciar():
    global posx, posy
    posx=2
    posy=2
    t26.grid(column=posx,row=posy)
def movera():
    global posx, posy
    posx=posx-1
    if(posx<0):
        posx=4
    t26.grid(column=posx,row=posy)
def moverw():
    global posx, posy
    posy=posy-1
    if(posy<0):
        posy=4
    t26.grid(column=posx,row=posy)
def movers():
    global posx, posy
    posy=posy+1
    if(posy>4):
        posy=0
    t26.grid(column=posx,row=posy)
def moverd():
    global posx, posy
    posx=posx+1
    if(posx>4):
        posx=0
    t26.grid(column=posx,row=posy)



#iniciar()
ventana=Tk()

t1=Button(ventana,bg="red", width=30,height=5)
t1.grid(column=0,row=0)
t2=Button(ventana,bg="red", width=30,height=5)
t2.grid(column=1,row=0)
t3=Button(ventana,bg="red", width=30,height=5)
t3.grid(column=2,row=0)
t4=Button(ventana,bg="red", width=30,height=5)
t4.grid(column=3,row=0)
t5=Button(ventana,bg="red", width=30,height=5)
t5.grid(column=4,row=0)
t6=Button(ventana,bg="red", width=30,height=5)
t6.grid(column=0,row=1)
t7=Button(ventana,bg="red", width=30,height=5)
t7.grid(column=1,row=1)
t8=Button(ventana,bg="red", width=30,height=5)
t8.grid(column=2,row=1)
t9=Button(ventana,bg="red", width=30,height=5)
t9.grid(column=3,row=1)
t10=Button(ventana,bg="red", width=30,height=5)
t10.grid(column=4,row=1)
t11=Button(ventana,bg="red", width=30,height=5)
t11.grid(column=0,row=2)
t12=Button(ventana,bg="red", width=30,height=5)
t12.grid(column=1,row=2)
t13=Button(ventana,bg="red", width=30,height=5)
t13.grid(column=2,row=2)
t14=Button(ventana,bg="red", width=30,height=5)
t14.grid(column=3,row=2)
t15=Button(ventana,bg="red", width=30,height=5)
t15.grid(column=4,row=2)
t16=Button(ventana,bg="red", width=30,height=5)
t16.grid(column=0,row=3)
t17=Button(ventana,bg="red", width=30,height=5)
t17.grid(column=1,row=3)
t18=Button(ventana,bg="red", width=30,height=5)
t18.grid(column=2,row=3)
t19=Button(ventana,bg="red", width=30,height=5)
t19.grid(column=3,row=3)
t20=Button(ventana,bg="red", width=30,height=5)
t20.grid(column=4,row=3)
t21=Button(ventana,bg="red", width=30,height=5)
t21.grid(column=0,row=4)
t22=Button(ventana,bg="red", width=30,height=5)
t22.grid(column=1,row=4)
t23=Button(ventana,bg="red", width=30,height=5)
t23.grid(column=2,row=4)
t24=Button(ventana,bg="red", width=30,height=5)
t24.grid(column=3,row=4)
t25=Button(ventana,bg="red", width=30,height=5)
t25.grid(column=4,row=4)

b4=Button(ventana,text="iniciar", command=iniciar, width=30, height=5)
b4.grid(column=1, row=6)
b0=Button(ventana,text="A", command=movera, width=30, height=5)
b0.grid(column=1, row=7)
b1=Button(ventana,text="W", command=moverw, width=30, height=5)
b1.grid(column=2, row=6)
b2=Button(ventana,text="S", command=movers, width=30, height=5)
b2.grid(column=2, row=7)
b3=Button(ventana,text="D", command=moverd, width=30, height=5)
b3.grid(column=3, row=7)

t26=Button(ventana,bg="blue", width=30,height=5)

