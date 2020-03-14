from tkinter import *
global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont

def inicio():
    
    ini=Label(ventana,text="jueguen piedra papel o tijera para ver quien empieza con X",width=45,height=5)
    ini.grid(column=0,row=0)
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont,win
  # J1=Label(ventana,text=texto).grid(column=0,row=0)
   #J1=Label(ventana,text=texto).place(x=200, y=500)
    g1.config(state=NORMAL)
    g2.config(state=NORMAL)
    g3.config(state=NORMAL)
    g4.config(state=NORMAL)
    g5.config(state=NORMAL)
    g6.config(state=NORMAL)
    g7.config(state=NORMAL)
    g8.config(state=NORMAL)
    g9.config(state=NORMAL)
    
    s=0
    x1=0
    x2=0
    x3=0
    x4=0
    x5=0
    x6=0
    x7=0
    x8=0
    x9=0
    o1=0
    o2=0
    o3=0
    o4=0
    o5=0
    o6=0
    o7=0
    o8=0
    o9=0
    cont=0
    win=0

def seleccion1():
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont
    if(s==0):
        t1.set("X")
        s=s+1
        x1=1
    else:
        t1.set("O")
        s=s-1
        o1=1        
    g1.config(state=DISABLED)
    cont=cont+1
    com()
def seleccion2():
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont
    if(s==0):
        t2.set("X")
        s=s+1
        x2=1
    else:
        t2.set("O")
        s=s-1
        o2=1
    g2.config(state=DISABLED)
    cont=cont+1
    com()
def seleccion3():
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont
    if(s==0):
        t3.set("X")
        s=s+1
        x3=1
    else:
        t3.set("O")
        s=s-1
        o3=1
    g3.config(state=DISABLED)
    cont=cont+1
    com()
def seleccion4():
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont
    if(s==0):
        t4.set("X")
        s=s+1
        x4=1
    else:
        t4.set("O")
        s=s-1
        o4=1
    g4.config(state=DISABLED)
    cont=cont+1
def seleccion5():
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont
    if(s==0):
        t5.set("X")
        s=s+1
        x5=1
    else:
        t5.set("O")
        s=s-1
        o5=1
    g5.config(state=DISABLED)
    cont=cont+1
    com()
def seleccion6():
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont
    if(s==0):
        t6.set("X")
        s=s+1
        x6=1
    else:
        t6.set("O")
        s=s-1
        o6=1
    g6.config(state=DISABLED)
    cont=cont+1
    com()
def seleccion7():
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont
    if(s==0):
        t7.set("X")
        s=s+1
        x7=1
    else:
        t7.set("O")
        s=s-1
        o7=1
    g7.config(state=DISABLED)
    cont=cont+1
    com()
def seleccion8():
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont
    if(s==0):
        t8.set("X")
        s=s+1
        x8=1
    else:
        t8.set("O")
        s=s-1
        o8=1
    g8.config(state=DISABLED)
    cont=cont+1
    com()
def seleccion9():
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont
    if(s==0):
        t9.set("X")
        s=s+1
        x9=1
    else:
        t9.set("O")
        s=s-1
        o9=1
    g9.config(state=DISABLED)
    cont=cont+1
    com()
def com():
    global s,t1,t2,t3,t4,t5,t6,t7,t8,t9,x1,x2,x3,x4,x5,x6,x7,x8,x9,o1,o2,o3,o4,o5,o6,o7,o8,o9,cont,win
    skeler=0
    
    if(x1==1 and x2==1 and x3==1):
        res=Label(ventana,text="El ganador es el jugador 1",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(x1==1 and x4==1 and x7==1):
        res=Label(ventana,text="El ganador es el jugador 1",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(x1==1 and x5==1 and x9==1):
        res=Label(ventana,text="El ganador es el jugador 1",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(x2==1 and x5==1 and x8==1):
        res=Label(ventana,text="El ganador es el jugador 1",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(x3==1 and x5==1 and x7==1):
        res=Label(ventana,text="El ganador es el jugador 1",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(x3==1 and x6==1 and x9==1):
        res=Label(ventana,text="El ganador es el jugador 1",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(x4==1 and x5==1 and x6==1):
        res=Label(ventana,text="El ganador es el jugador 1",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(x7==1 and x8==1 and x9==1):
        res=Label(ventana,text="El ganador es el jugador 1",width=45,height=5)
        res.grid(column=0, row=1)
        win=1

    if(o1==1 and o2==1 and o3==1):
        res=Label(ventana,text="El ganador es el jugador 2",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(o1==1 and o4==1 and o7==1):
        res=Label(ventana,text="El ganador es el jugador 2",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(o1==1 and o5==1 and o9==1):
        res=Label(ventana,text="El ganador es el jugador 2",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(o2==1 and o5==1 and o8==1):
        res=Label(ventana,text="El ganador es el jugador 2",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(o3==1 and o5==1 and o7==1):
        res=Label(ventana,text="El ganador es el jugador 2",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(o3==1 and o6==1 and o9==1):
        res=Label(ventana,text="El ganador es el jugador 2",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(o4==1 and o5==1 and o6==1):
        res=Label(ventana,text="El ganador es el jugador 2",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(o7==1 and o8==1 and o9==1):
        res=Label(ventana,text="El ganador es el jugador 2",width=45,height=5)
        res.grid(column=0, row=1)
        win=1
    if(win!=1 and cont==9):
        res=Label(ventana,text="Fue empate",width=45,height=5)
        res.grid(column=0, row=1)
    
    


ventana=Tk()
t1=StringVar()
t2=StringVar()
t3=StringVar()
t4=StringVar()
t5=StringVar()
t6=StringVar()
t7=StringVar()
t8=StringVar()
t9=StringVar()

b0=Button(ventana,text="iniciar", command=inicio, width=45, height=5)
b0.grid(column=0, row=0)

g1=Button(ventana,textvariable=t1, command=seleccion1,state=DISABLED, width=12, height=5)
g1.grid(column=1,row=1)

g2=Button(ventana,textvariable=t2, command=seleccion2,state=DISABLED, width=12, height=5)
g2.grid(column=2,row=1)

g3=Button(ventana,textvariable=t3, command=seleccion3,state=DISABLED, width=12, height=5)
g3.grid(column=3,row=1)

g4=Button(ventana,textvariable=t4, command=seleccion4,state=DISABLED, width=12, height=5)
g4.grid(column=1,row=2)

g5=Button(ventana,textvariable=t5, command=seleccion5,state=DISABLED, width=12, height=5)
g5.grid(column=2,row=2)

g6=Button(ventana,textvariable=t6, command=seleccion6,state=DISABLED, width=12, height=5)
g6.grid(column=3,row=2)

g7=Button(ventana,textvariable=t7, command=seleccion7,state=DISABLED, width=12, height=5)
g7.grid(column=1,row=3)

g8=Button(ventana,textvariable=t8, command=seleccion8,state=DISABLED, width=12, height=5)
g8.grid(column=2,row=3)

g9=Button(ventana,textvariable=t9, command=seleccion9,state=DISABLED, width=12, height=5)
g9.grid(column=3,row=3)

#g10=Button(ventana,text="reiniciar", command=inicio,state=DISABLED, width=12, height=5)
#g10.grid(column=0,row=3)
#g10.config(state=NORMAL)

