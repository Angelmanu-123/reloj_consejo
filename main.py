from tkinter import messagebox#libreria para mostrar mensajes emergentes
import requests#libreria para hacer peticiones a una API
from tkinter import *
# Función para obtener datos del clima
def obtenerClima():
    url = "https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    lat = "14.634915"
    lon = "-90.506882"
    url = url.replace("{lat}", lat).replace("{lon}", lon)
    dato = requests.get(url).json()
    temperatura = dato["current_weather"]["temperature"]  # grados celsius
    viento = dato["current_weather"]["windspeed"]  # km/h

    etiqueta3.configure(text=f"Temperatura: {temperatura}°C\nViento: {viento} km/h", )
    # Llamar la función por primera vez
    app.after(60000, obtenerClima)  # actualiza cada 60 segundos

# -----------------------------------------------------------------------------
# Función para mostrar  un consejo
def consejo():
    url = "	https://api.adviceslip.com/advice"
    consejos = requests.get(url).json()
    consejo = consejos["slip"]["advice"]
    messagebox.showinfo("Consejo del día", consejo)
# funcion para cerrar la ventana
def cerrar():
    app.destroy()
app = Tk()
app.title("Reloj ")
app.resizable(False, False)
# etiqueta para mostrar la hora
etiqueta1 = Label(app, text="", )
etiqueta1.grid(row=0, column=0, padx=5, pady=5, columnspan=1)

etiqueta3 = Label(app, text="", )
etiqueta3.grid(row=2, column=0, padx=5, pady=5,columnspan=1)
# Botón para mostrar un consejo
boton1 = Button(app, text="Mostrar consejo" , command=consejo)
boton1.grid(row=3, column=0, padx=2, pady=5)
boton2=Button(app, text="Salir", command=cerrar)
boton2.grid(row=3, column=1)
obtenerClima()


app.mainloop()