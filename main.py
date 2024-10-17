import customtkinter as ctk
import subprocess
import webbrowser
from funciones_bd import Data
from tkinter import ttk
from tkinter import *
from tkinter import messagebox as msg

# Inicializar CustomTkinter
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

# Crear ventana principal
root = ctk.CTk()
root.title("Ingreso de Datos")
root.geometry("600x500")

# Función para ejecutar Flask
def ejecutar_flask():
    subprocess.Popen(['python', 'C:\\Users\\USER\\Desktop\\menu\\app.py'])
    url = 'http://127.0.0.1:5000/'
    webbrowser.open(url)

oData = Data()
# Función para llenar la tabla
def llenarTabla(table):
    datos = oData.consultarUsuarios()
    for fila in datos:
        table.insert("", END, text=fila[0], values=(fila[1], fila[2]))
def limpiarTabla(table):
    for fila in table.get_children():
        table.delete(fila)

# Función para cambiar el estado de los botones
def estadoBtn1(estado):
    btn_guardar.configure(state=estado)
    btn_eliminar.configure(state=estado)
    btn_cancelar.configure(state=estado)
def estadoBtn2(estado):
    btn_enviar.configure(state=estado)
    btn_editar.configure(state=estado)

# Función para limpiar los campos
def limpiarCampos():
        entry_usuario.delete(0, END)
        entry_email.delete(0, END)

# Función para insertar un usuario
def insertarUsuario():
    if len(entry_usuario.get()) != 0 and len(entry_email.get()) != 0:
            oData.insertarUsuario(entry_usuario.get(), entry_email.get())
            limpiarTabla(table)
            llenarTabla(table)
            limpiarCampos()
            msg.showinfo('Datos de usuarios', 'El usuario se ha agregado correctamente...')
            entry_usuario.focus()
    else:
        msg.showinfo('Datos de usuarios', 'Debe digitar los datos obligatorios...')
        entry_usuario.focus()

# Función para actualizar un usuario
def actualizarUsuario():
    if len(entry_usuario.get()) != 0 and len(entry_email.get()) != 0:
            oData.editarUsuario(id, entry_usuario.get(), entry_email.get())
            limpiarTabla(table)
            llenarTabla(table)
            limpiarCampos()
            estadoBtn2('normal')
            estadoBtn1('disabled')
            msg.showinfo('Datos de usuarios', 'El usuario se ha actualizado correctamente...')
            entry_usuario.focus()

# Función para seleccionar un usuario
def seleccionarUsuario():
    global id
    sele = table.focus()
    sw = table.item(sele, 'text')
    if sw == '':
        msg.showwarning('Editar', 'Debes seleccionar un usuario...')
    else:
        id = sw
        limpiarCampos()
        inftabla = table.item(sele, 'values')
        entry_usuario.insert(0, inftabla[0])
        entry_email.insert(0, inftabla[1])
        estadoBtn2('disabled')
        estadoBtn1('normal')
        entry_usuario.focus()

# Función para eliminar un usuario
def fEliminarUsuario(table):
    sele = table.focus()
    sw = table.item(sele, 'text')
    if sw == '':
        msg.showwarning('Editar', 'Debes seleccionar una marca...')
    else:
        inftabla =  table.item(sele, 'values')
        dato = inftabla[0]+'?'
        men = msg.askquestion('Eliminar Usuario', 'Está seguro de Eliminar el usuario '+dato)
        if men == msg.YES:
            eli = oData.eliminarUsuario(sw)
            if eli == 1:
                limpiarTabla(table)
                llenarTabla(table)
                limpiarCampos()
                msg.showinfo('Eliminar Usuario', 'Usuario eliminado...')
            else:
                msg.showinfo('Eliminar Usuario', 'No se pudo eliminar el usuario...')
        estadoBtn1('disabled')
        estadoBtn2('normal')
        entry_usuario.focus()

# Función para cancelar
def cancelar():
    limpiarCampos()
    estadoBtn1('disabled')
    estadoBtn2('normal')
    entry_usuario.focus()

def actuTabla(table):
    limpiarTabla(table)
    llenarTabla(table)

# Crear etiquetas y entradas para Usuario y Email
label_usuario = ctk.CTkLabel(root, text="Usuario:")
label_usuario.place(relx=0.25, rely=0.1, anchor="center")
entry_usuario = ctk.CTkEntry(root, placeholder_text="Ingrese su usuario", width=200)
entry_usuario.place(relx=0.5, rely=0.1, anchor="center")

label_email = ctk.CTkLabel(root, text="Email:")
label_email.place(relx=0.25, rely=0.2, anchor="center")
entry_email = ctk.CTkEntry(root, placeholder_text="Ingrese su Email", width=200) 
entry_email.place(relx=0.5, rely=0.2, anchor="center")

# Crear frame boton
frame_boton = ctk.CTkFrame(root)
frame_boton.place(relx=0.5, rely=0.4, anchor="center")
frm_btn_web = ctk.CTkFrame(root, height=100, width=150, fg_color="#242424")
frm_btn_web.place(relx=0.7, rely=0.17, anchor="w")

# botones
btn_enviar = ctk.CTkButton(frame_boton, text="Enviar", width=100, command=insertarUsuario)
btn_enviar.pack(side="left", padx=5)
btn_eliminar = ctk.CTkButton(frame_boton, text="Eliminar", fg_color="red", width=100, command=lambda: fEliminarUsuario(table))
btn_eliminar.pack(side="left", padx=5)
btn_editar = ctk.CTkButton(frame_boton, text="Editar", fg_color="yellow", text_color="black", width=100, command=seleccionarUsuario)
btn_editar.pack(side="left", padx=5)
btn_guardar = ctk.CTkButton(frame_boton, text="Guardar", fg_color="green", width=100, command=actualizarUsuario)
btn_guardar.pack(side="left", padx=5)
btn_cancelar = ctk.CTkButton(frame_boton, text="Cancelar", fg_color="gray", text_color="black", width=100, command=cancelar)
btn_cancelar.pack(side="left", padx=5)
btn_web = ctk.CTkButton(frm_btn_web, text="Abrir en la Web", fg_color="lightblue", text_color="black", width=100, command=ejecutar_flask)
btn_web.place(relx=0.2, rely=0)
btn_actu_tabla = ctk.CTkButton(frm_btn_web, text="Actualizar Tabla", fg_color="pink", text_color="black", width=100, command=lambda: actuTabla(table))
btn_actu_tabla.place(relx=0.17, rely=0.5)

# Configurar estilo para Treeview
style = ttk.Style()
style.configure("Treeview", font=("Helvetica", 14))
style.configure("Treeview.Heading", font=("Helvetica", 16, "bold")) 

# Crear tabla
frame = ctk.CTkFrame(root, width=540)
frame.place(relx=0.05, rely=0.55)
table = ttk.Treeview(frame, columns=("c1", "c2"), show="headings")
table.column('#0', width=60, anchor='w')
table.column('c1', width=200, anchor='e')
table.column('c2', width=465, anchor='e')
table.heading('#0', text='ID', anchor='center')
table.heading('c1', text='Usuario', anchor='center')
table.heading('c2', text='Email', anchor='center')
table.pack(fill="both", expand=1)

# llamar a las funciones
llenarTabla(table)
estadoBtn1('disabled')
estadoBtn2('normal')

root.mainloop()