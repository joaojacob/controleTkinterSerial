import comands
from pySerial import *
from tkinter import ttk
from tkinter import *

def readSer():
        readS = readSerial()
        if readS != 'semLeitura':
            #print("ARDUINO: '{}'\n".format(readS))
            text_box.delete("1.0", "end")
            text_box.insert(0.0,readS)
        window.after(10, readSer)

width, height = 200, 150
window = Tk()
window.title('JSerial')
window.minsize(width=width, height=height)
window.maxsize(width=width, height=height)

primeiroContainer = Frame(window)
primeiroContainer.pack()

segundoContainer = Frame(window)
segundoContainer.pack()

btnligar = Button(primeiroContainer,height =2 ,width = 8,bg="dark green",fg="snow", text="LIGAR",command=comands.ligar)
btnligar.pack(side=LEFT)

btnDesligar = Button(primeiroContainer,height = 2,width =8,bg="dark red",fg="snow",text="DESLIGAR",command=comands.desligar)
btnDesligar.pack(side=LEFT)

text_box = Text(segundoContainer, width=120, height=10)
text_box.pack()

window.after(100,readSer)
window.mainloop()
