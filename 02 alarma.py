#variable=input("Lo que quieras que diga en pantalla"
class alarma:
    def __init__(self): #ruido,vibracion,luz,activacion,movimiento,personalizacion):

        #self.ruido=ruido
        #self.vibracion=vibracion
        #self.luz=luz
        #self.activacion=activacion
        #self.movimiento=movimiento
        #self.personalizacion=personalizacion
      pass

    def activacion (self):

        activacion=input("¿quieres activar la alarma? escribe: si\n")
        minutos=input("cuantos minutos quieres que se active\n")
        if(activacion=="si"):
            personalizacion=input("¿quieres personalizar tu alarma?, escribe: si\n")
            if(personalizacion=="si"):
                luz=input("¿Quieres que prenda una luz? escribe si\n")
                if(luz=="si"):
                 luzind="si"
                else:
                 luz="no"
                vibracion=input("¿Quieres que la alarma vibre? escribe si\n")
                if(vibracion=="si"):
                            vibracionind="si"
                else:
                            vibracionind="no"
                ruido=input("¿Quieres que la alarma haga ruido? escribe si\n")
                if(ruido=="1"):
                            ruidoind="si"
                else:
                            ruidoind="no"
            else:
                    luz="si"
                    vibracion="si"
                    ruido="si"
            movimiento=0
            while(movimiento=="si"):
             movimiento=input("¿hay movimiento?\n")

            print("la alarma ha sido ativada, ayudaaaaa\n la alarma esta \n vibrando:", vibracion,"\n", "haciendo ruido:", ruido,"\n", "emitiendo luz:", luz, "\n",
                  "duro", minutos, " minutos activada")
            
              

                   
        else:
            print("adios")
            
alarma=alarma()
alarma.activacion()
               


        
