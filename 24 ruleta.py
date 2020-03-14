#equipo
#Gallegos González Leonardo Uriel
#López Molina Edgar
#Gómez Acosta José Miguel
#Velazquez Ocampo Enrique Yael
#Arreguín Arreguín Felix
from tkinter import *
import random
global hacer_apuesta,minimo,din_dis,color,apostad,tablero
minimo=100
color=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
    
def comienzo():
    global hacer_apuesta,minimo,din_dis,color,tablero
    
#    hacer_apuesta.withdraw()
    
    
    tdin=m.get()
    din_dis=float(tdin)
    hacer_apuesta=Toplevel()
    hacer_apuesta.title("Apuesta")
    hacer_apuesta.withdraw()
    hacer_apuesta.geometry("500x590")
    
    LIMG=Label(hacer_apuesta,image=tablero)
    LIMG.place(x=0,y=0)

    BCR=Button(hacer_apuesta,text="rojos",command=rojos)
    BCR.place(x=0,y=292)

    BCN=Button(hacer_apuesta,text="negros",command=negros)
    BCN.place(x=38,y=292)

    BPAR=Button(hacer_apuesta,text="Pares",command=negros)
    BPAR.place(x=85,y=292)

    BIPR=Button(hacer_apuesta,text="Impares",command=rojos)
    BIPR.place(x=125,y=292)

    BPAS=Button(hacer_apuesta,text="Pasa",command=pasa)
    BPAS.place(x=178,y=292)

    BFAL=Button(hacer_apuesta,text="Falta",command=falta)
    BFAL.place(x=214,y=292)

    LEA=Label(hacer_apuesta,textvariable=numinv)
    LEA.place(x=214,y=350)

    NUM=Entry(hacer_apuesta,textvariable=au)
    NUM.place(x=250,y=292)

    BUM=Button(hacer_apuesta,text="verificar numero",command=numero)
    BUM.place(x=360,y=292)
        
    a=1
    color[0]="verde"

    while(a<=18):
        color[2*a]="negro"
        color[(2*a)-1]="rojo"
        a=a+1
    color[37]="verde"

    if(din_dis<minimo):
        error.set("necesitas mas dinero")
    else:
        error.set("El jugador comenzo con: "+ str(din_dis))
        Brev.config(state=NORMAL)
        Ball.config(state=NORMAL)
        BI.config(state=DISABLED)
        dinero.config(state=DISABLED)
        bienvenido.set("Usted esta jugando, la apuesta minima es de 100")
        Dpa.config(state=NORMAL)
        

def verificar():
    global din_dis,minimo,apostad

    dr=da.get()

    a=float(dr)

    if(a<=0 and a>din_dis):
        if(a<minimo):
            apostado.set("no puedes apostar esa cantidad \n Prueba de nuevo")
    if(a>=minimo and a<=din_dis):
        porapostar.set("Usted est apostando: " + str(a))
        apostado.set(" ")
        apostad=a

        Ball.config(state=DISABLED)
        Brev.config(state=DISABLED)
        Dpa.config(state=DISABLED)

        hacer_apuesta.deiconify()
    else:
        apostado.set("no puedes apostar esa cantidad \n Prueba de nuevo")
        
def todo():
    global din_dis,minimo,apostad

    porapostar.set("Usted est apostando: " + str(din_dis))
    apostad=din_dis

    Ball.config(state=DISABLED)
    Brev.config(state=DISABLED)
    Dpa.config(state=DISABLED)

    hacer_apuesta.deiconify()

def rojos():

    G=1
    I=1
    N=0
    comparacion(G,I,N)
    
def negros():

    G=1
    I=2
    N=0
    comparacion(G,I,N)

def pasa():

    G=1
    I=4
    N=0       
    comparacion(G,I,N)
    
def fin():
    global din_dis

    m.set("")
    da.set("")
    au.set("")
    bienvenido.set("¿Desea iniciar nuevo juego?")
    apostado.set("El jugador se a retirado con :" + str(din_dis))
    porapostar.set("")
    ganado.set("")
    d_act.set("")
    numinv.set("")
    Ball.config(state=DISABLED)
    Brev.config(state=DISABLED)
    Dpa.config(state=DISABLED)
    dinero.config(state=NORMAL)
    BI.config(state=NORMAL)
    BRet.config(state=DISABLED)

def comprobar():
    global din_dis,minimo

    if(din_dis<minimo):
        m.set("")
        da.set("")
        au.set("")
        bienvenido.set("¿Desea iniciar nuevo juego?")
        apostado.set("El jugador se a retirado con :" + str(din_dis))
        porapostar.set("No tiene dinero para la apuesta minima")
        ganado.set("")
        d_act.set("")
        numinv.set("")
        Ball.config(state=DISABLED)
        Brev.config(state=DISABLED)
        Dpa.config(state=DISABLED)
        dinero.config(state=NORMAL)
        BI.config(state=NORMAL)
        BRet.config(state=DISABLED)        

def falta():

    G=1
    I=3
    N=0
    comparacion(G,I,N)
    
def numero():

    G=36
    I=0
    t=au.get()
    N=float(t)
    if(N<=36 and N>=0):
        comparacion(G,I,N)
        numinv.set("")
    numinv.set("numero no valido")
    

def comparacion(G,V,N):
    global din_dis,apostad,color

    hacer_apuesta.withdraw()
    tg=0.0
    
    num=random.randint(0,37)
    
    if(num<37):
        apostado.set("La ruleta cayo en: " + str(num) + " color: " + str(color[num]))
    else:
        apostado.set("La ruleta cayo en: 00" + " color: " + str(color[num]))

    r=1
    W=0
    
    if(V>0 and V<=4):
        if(V==1):

            if(color[num]=="rojo"):
                ganado.set("a ganado: " + str(G*apostad))
                tg=din_dis+(G*apostad)
                W=1
             
            
        if(V==2):
            
            if(color[num]=="negro"):
                ganado.set("a ganado: " + str(G*apostad))
                tg=din_dis+(G*apostad)
                W=1
                
        if(V==3):

            if(num<=18 and num>0):
                ganado.set("a ganado: " + str(G*apostad))
                tg=din_dis+(G*apostad)
                W=1

        if(V==4):

            if(num<=36 and num>18):
                ganado.set("a ganado: " + str(G*apostad))
                tg=din_dis+(G*apostad)
                W=1

    if(V==0):

        if(num==N):
            ganado.set("a ganado: " + str(G*apostad))
            tg=din_dis+(G*apostad)
            W=1

    if(W==0):
        tg=din_dis-(apostad)
        ganado.set("a perdido: " + str(apostad))
        d_act.set("El jugador cuenta con: "+ str(tg))
    if(W==1):    
        d_act.set("El jugador cuenta con: "+ str(tg))

    din_dis=tg

    Ball.config(state=NORMAL)
    Brev.config(state=NORMAL)
    Dpa.config(state=NORMAL)
    BRet.config(state=NORMAL)

    comprobar()

ventana=Tk()

m=StringVar()
da=StringVar()
au=StringVar()
error=StringVar()
bienvenido=StringVar()
apostado=StringVar()
porapostar=StringVar()
ganado=StringVar()
d_act=StringVar()
numinv=StringVar()

bienvenido.set("Bienvenido \n La apuesta minima es de: " + str(minimo) + "\n Cuanto dinero tiene?")
dinero=Entry(ventana,textvariable=m)
dinero.grid(row=3,column=2)
BI=Button(ventana,text="ingresar cantidad",command=comienzo)
BI.grid(row=4,column=2)


merror=Label(ventana,textvariable=error)
merror.grid(row=5,column=2)

tablero=PhotoImage(file="tablero.png")
Lb=Label(ventana,textvariable=bienvenido)
Lb.grid(row=1,column=2)
La=Label(ventana,textvariable=apostado)
La.grid(row=6,column=2)
Lpa=Label(ventana,textvariable=porapostar)
Lpa.grid(row=7,column=2)
Dpa=Entry(ventana,textvariable=da)
Dpa.grid(row=8,column=2)
Brev=Button(ventana,text="Verificar apuesta",command=verificar,state=DISABLED)
Brev.grid(row=9,column=2)
Ball=Button(ventana,text="Apostar todo",command=todo,state=DISABLED)
Ball.grid(row=9,column=3)
Lganado=Label(ventana,textvariable=ganado)
Lganado.grid(row=11,column=2)
BRet=Button(ventana,text="salir",command=fin,state=DISABLED)
BRet.grid(row=10,column=2)
Lact=Label(ventana,textvariable=d_act)
Lact.grid(row=12,column=2)


ventana.mainloop()
