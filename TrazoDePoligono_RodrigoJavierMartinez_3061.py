from tkinter import *    
from tkinter import scrolledtext
import turtle

ventana = Tk()
Nlados = IntVar()
seleccionAlg=IntVar()
seleccionFig=IntVar()

ventana.configure(bg = 'orange')
ventana.title('Representación y trazo de líneas y polígonos')
ventana.geometry("500x500")

txtTitulo=Label(ventana,text="Polígono de N lados por Algoritmo DDA y Bresenhams",bg = 'orange', fg='black',font=("Arial", 14)).place(x=20,y=20)

lblFig=Label(ventana,text="Ingresa el número de lados:",bg = 'orange', font=("Arial", 11)).place(x=35, y=60)
cajaNlados=Entry(ventana,textvariable=Nlados).place(x=35,y=90)


lbResult=Label(ventana,text="Resultados de X, Y:",bg = 'orange',font=("Arial", 11)).place(x=250, y=60)
txtResultado = scrolledtext.ScrolledText(ventana,width=25,height=23,bg = '#333333',fg='#FFFFFF',font=("Arial", 11))
txtResultado.grid(column=0,row=0)
txtResultado.place(x=250, y=90)

turtle.setup(800,800,-1,0)
g = turtle.Turtle()
g.pensize(2)
wn = turtle.Screen() 
wn.bgcolor("Black")  
wn.title("Poligono de N lados")

def calcularAlgoritmos():
    
    if seleccionAlg.get() == 1:
        angulo=0
        x1=2
        y1=2
        x2=2
        y2=6
        n=Nlados.get()

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        steps = 0
    
        if (dx) > (dy):
            steps = (dx)
        else:
            steps = (dy)
          
        xInc = float(dx / steps)
        yInc = float(dy / steps)

        xInc = round(xInc,1)
        yInc = round(yInc,1)

        ln = steps 
        txtResultado.insert(INSERT,'DDA\n')
        txtResultado.insert(INSERT,'dx: '+str(dx)+'\n')
        txtResultado.insert(INSERT,'dy: '+str(dy)+'\n')
        txtResultado.insert(INSERT,'Steps: '+str(steps)+'\n')
        txtResultado.insert(INSERT,'Xincremeto: '+str(xInc)+'\n')
        txtResultado.insert(INSERT,'Yincremento: '+str(yInc)+'\n')
        txtResultado.insert(INSERT,'Angulo: '+str(angulo)+'\n')
        txtResultado.insert(INSERT,'\n  X         Y\n')

        for i in range(steps, int(steps+1)):
            g.setx(x1)
            g.sety(y1)

            angulo=float(180-(((n-2)/n)*180))
            for i in range(n):
                g.left(angulo)
                g.fd(0)
                for i in range(ln):
                    g.fd(25)
                    g.color("blue")
                    p=g.pos()
                    txtResultado.insert(INSERT,'\n'+str(p))
                    for i in range(4):
                        g.forward(25)
                        g.left(90)
                g.forward(25)


    if seleccionAlg.get() == 2:
        angulo=0
        x1=4
        y1=2
        x2=4
        y2=6
        n=Nlados.get()

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        p = 2*dy - x1

        x = x1
        y = y1

        ln = (p)

        g.setx(x)
        g.sety(y)

        txtResultado.insert(INSERT,'Bresenhams\n')
        txtResultado.insert(INSERT,'dx: '+str(dx)+'\n')
        txtResultado.insert(INSERT,'dy: '+str(dy)+'\n')
        txtResultado.insert(INSERT,'p: '+str(p)+'\n')
        txtResultado.insert(INSERT,'X   Y\n')

        angulo=float(180-(((n-2)/n)*180))
        txtResultado.insert(INSERT,'Angulo: '+str(angulo)+'\n')
    
        while (x <= x2):
            x+=1
            if p < 0:
                p=p + 2 * dy
            else:
                p=p + (2*dy) -(2*dx)
                y+=1
                angulo=float(180-(((n-2)/n)*180))
                for i in range(n):
                    g.left(angulo)
                    g.fd(0)
                    for i in range(ln):
                        g.fd(25)
                        g.color("blue")
                        ps=g.pos()
                        txtResultado.insert(INSERT,'\n'+str(ps))
                        for i in range(4):
                            g.forward(25)
                            g.left(90)
                    g.forward(25)
    mainloop
def nuevo():
    seleccionAlg.set(None)
    seleccionFig.set(None)
    txtResultado.delete(1.0,END)
    Nlados.set("")
    g.clear()

def salir(): 
    ventana.destroy()
    wn.exitonclick()

lblAlg=Label(ventana,text="Selecciona el algoritmo:",bg = 'orange', font=("Arial", 11)).place(x=35, y=120)
rBDDA=Radiobutton(ventana,text="DDA",bg = 'orange', variable=seleccionAlg, value=1,font=("Arial", 11)).place(x=35, y=150)
rBBS=Radiobutton(ventana,text="Bresenhams",bg = 'orange', variable=seleccionAlg, value=2,font=("Arial", 11)).place(x=35, y=180)

btnCalcularBS=Button(ventana, text="Graficar", command=calcularAlgoritmos,bg = '#333333',fg='#FFFFFF',font=("Arial", 11)).place(x=20, y=350)
btnNuevo=Button(ventana, text="Nuevo", command=nuevo,bg = '#333333',fg='#FFFFFF',font=("Arial", 11)).place(x=100, y=350)
btnSalir=Button(ventana, text="Salir", command=salir,bg = '#333333',fg='#FFFFFF',font=("Arial", 11)).place(x=180, y=350)

ventana.mainloop()