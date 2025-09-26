from tkinter import *
import requests
def actualizar():
    url ="https://timeapi.io/api/time/current/zone?timeZone=America%2FGuatemala"

    data = requests.get(url).json()
    anio = data["year"]
    hora = data["hour"]
    minutos =data["minute"]
    segundos = data["seconds"]


    texto = (f"hora: {hora}  " 
             f" minutos: {minutos}  " 
             f" segundos: {segundos}  " 
             f"anio :{anio}")
    etiqueta.config(text=texto)


    app.after(1000, actualizar)

app =Tk()

app.title("aplicacion de la hora")
app.geometry("300x200")
app.resizable(width=False,height=False)

etiqueta = Label(app,text = "hora",fg="blue")
etiqueta.grid(column =0,row=1,padx=3,pady=3)

actualizar()
app.mainloop()