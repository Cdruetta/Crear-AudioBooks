import tkinter as tk
from tkinter import filedialog
import pyttsx3
import PyPDF2

def listar_vidas():
    voces = engine.getProperty('voices')
    for index, voz in enumerate(voces):
        print(f"ID: {index} - Nombre: {voz.name} - Idioma: {voz.languages}")

def convertir_pdf_audio():
    archivo_pdf = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if archivo_pdf:
        texto = ""
        with open(archivo_pdf, 'rb') as pdf_file:
            lector_pdf = PyPDF2.PdfReader(pdf_file)
            for pagina in lector_pdf.pages:
                texto += pagina.extract_text()
        engine.setProperty('voice', voces[0].id)  # Cambia el índice según la voz que quieras
        engine.save_to_file(texto, 'salida.mp3')
        engine.runAndWait()
        etiqueta.config(text="¡Audio creado en 'salida.mp3'!")

# Crear ventana
ventana = tk.Tk()
ventana.title("Convertidor de PDF a Audio")
ventana.geometry("500x300")

# Inicializar el motor de texto a voz
engine = pyttsx3.init()
voces = engine.getProperty('voices')  # Obtener las voces disponibles

# Mostrar las voces en la consola (opcional)
listar_vidas()

# Botón para seleccionar PDF y convertir
boton_convertir = tk.Button(ventana, text="Seleccionar PDF y convertir a audio", command=convertir_pdf_audio, font=("Arial", 14))
boton_convertir.pack(pady=40)

# Etiqueta de estado
etiqueta = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta.pack(pady=10)

ventana.mainloop()




