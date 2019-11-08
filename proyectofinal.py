# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 13:28:51 2019

@author: XAVIER EMMANUEL
"""
#XavierEmmanuelDomínguezGrajales
from tkinter import *
import serial, time
lista=[]

def holamundo():
    global lista
    try:
        archivo = open(Archivo.get(),"w")
        for i in range(len(lista)):
            archivo.write(str(int(lista[i]))+" ")
        archivo.close()
    except:
        print("Ingrese un nombre de archivo valido")

def CrearLista():
    global lista
    arduino = serial.Serial("COM3", 9600)
    time.sleep(4)
    lista = []
    try:
        for i in range(int(NumDatos.get())):
            lista.append(arduino.readline())
    except:
        print("Ingrese un valor valido")
    arduino.close()

def mostrarDatos():
    global lista
    if len(lista) > 0:
        print("Estos son los datos almacenados: ")
        for i in range(len(lista)):
            print(str(i+1)+") "+str(int(lista[i])))
        print("\n")
    else:
        print("No hay ningún dato exitente")

Ventana = Tk()
Ventana.title("Mi primer ventana")
frame = Frame(Ventana)
frame.pack(ipadx = 50, ipady = 50, side = BOTTOM)
etiqueta = Label(frame,text = "Número de datos:\n")
etiqueta.pack()
NumDatos = Entry(frame)
NumDatos.pack(ipadx = 10, ipady = 5)
espacio = Label(frame,text = "")
espacio.pack()
LeerDatos = Button(frame, text = "Leer datos", command = CrearLista)
LeerDatos.pack(ipadx = 10, ipady = 5)
Archivo = Entry(frame)
Archivo.pack(ipadx = 10, ipady = 5)
espacio2 = Label(frame,text = "Archivo")
espacio2.pack()
Guardar = Button(frame, text = "Guardar", command = holamundo)
Guardar.pack(ipadx = 10, ipady = 5)
espacio3 = Label(frame,text = "")
espacio3.pack()
Mostrar = Button(frame, text = "Mostrar", command = mostrarDatos)
Mostrar.pack(ipadx = 30, ipady = 5)
Ventana.geometry("500x400")
Ventana.mainloop()
