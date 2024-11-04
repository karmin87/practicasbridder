
 
from tkinter import *
from tkinter import messagebox
 
# declara una lista global para almacenar todas las tareas        
tasks_list = []
 
# variable global para contar las tareas
counter = 1
 
    # Función para verificar errores de entrada cuando
# no se proporciona ninguna entrada en el campo de tarea
def inputError() :
     
    # revisa si el campo de entrada de tarea está vacío o no
    if enterTaskField.get() == "" :
         
        # muestra el mensaje de error
        messagebox.showerror("Input Error")
         
        return 0
     
    return 1
 
# Función para limpiar el contenido
# del campo de número de tarea
def clear_taskNumberField() :
     
    # limpia el contenido del campo de número de tarea
    taskNumberField.delete(0.0, END)
 
# Función para limpiar el contenido
# del campo de entrada de tarea
def clear_taskField() :
 
    # limpia el contenido del campo de entrada de tarea
    enterTaskField.delete(0, END)
     
# Función para insertar el contenido
# del campo de entrada de tarea en el área de texto
def insertTask():
 
    global counter
     
    # revisa si hay un error
    value = inputError()
 
    # si ocurre un error, entonces devuelve
    if value == 0 :
        return
 
    # obtiene la cadena de tarea concatenada
    # con el carácter de nueva línea
    content = enterTaskField.get() + "\n"
 
    # almacena la tarea en la lista
    tasks_list.append(content)
 
    # inserta el contenido del campo de entrada de tarea en el área de texto
    # agrega una tarea una por una
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)
 
    # incrementa
    counter += 1
 
    # llama a la función para eliminar el contenido del campo de tarea
    clear_taskField()
 
# función para eliminar la tarea especificada
def delete() :
     
    global counter
     
    # maneja el error de tarea vacía
    if len(tasks_list) == 0 :
        messagebox.showerror("No task")
        return
 
    # obtiene el número de tarea, que se requiere eliminar
    number = taskNumberField.get(1.0, END)
 
    # revisa si hay un error de entrada cuando
    # no se proporciona ninguna entrada en el campo de número de tarea
    if number == "\n" :
        messagebox.showerror("input error")
        return
     
    else :
        task_no = int(number)
 
    # llama a la función para eliminar el contenido
    # del campo de número de tarea
    clear_taskNumberField()
     
    # elimina la tarea especificada de la lista
    tasks_list.pop(task_no - 1)
 
    # decrementa
    counter -= 1
     
    # se elimina todo el contenido del área de texto
    TextArea.delete(1.0, END)
 
    # reescribe la tarea después de eliminar una tarea a la vez
    for i in range(len(tasks_list)) :
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + tasks_list[i])
     
 
# Driver code 
if __name__ == "__main__" :
 
    # crea una ventana GUI
    gui = Tk()
 
    # establece el color de fondo de la ventana GUI
    gui.configure(background = "light green")
 
    # establece el título de la ventana GUI
    gui.title("ToDo App")
 
    # establece la configuración de la ventana GUI
    gui.geometry("250x300")
 
    # crea una etiqueta: Entrar tu tarea
    enterTask = Label(gui, text = "Enter Your Task", bg = "light green")
 
    # crea una caja de texto
    # para escribir la tarea
    enterTaskField = Entry(gui)
 
    # creando el botón Submit y colocándolo en la ventana raíz
    # cuando el usuario presione el botón, se ejecuta el comando o
    # función asociada al botón
    Submit = Button(gui, text = "Submit", fg = "Black", bg = "Red", command = insertTask)
 
    # crea un área de texto para la ventana raíz
    # con una altura de 13 y un ancho de 25
    # el área de texto es para escribir el contenido
    TextArea = Text(gui, height = 5, width = 25, font = "lucida 13")
 
    # crea una etiqueta: Número de tarea para eliminar
    taskNumber = Label(gui, text = "Delete Task Number", bg = "blue")
                        
    taskNumberField = Text(gui, height = 1, width = 2, font = "lucida 13")
 
    # crea un botón Delete y lo coloca en la ventana raíz
    # cuando el usuario presione el botón, se ejecuta el comando o
    # función asociada al botón.
    delete = Button(gui, text = "Delete", fg = "Black", bg = "Red", command = delete)
 
    # crea un botón Exit y lo coloca en la ventana raíz
    # cuando el usuario presione el botón, se ejecuta el comando o
    # función asociada al botón.
    Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)
 
    # el método grid se utiliza para colocar
    # los widgets en las posiciones respectivas
    # en una estructura similar a una tabla.
    enterTask.grid(row = 0, column = 2)
 
    # ipadx establece el tamaño horizontal de la caja de entrada
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)
                        
    Submit.grid(row = 2, column = 2)
         
    # padx proporciona un margen horizontal desde la ventana raíz hasta el widget.
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)
                        
    taskNumber.grid(row = 4, column = 2, pady = 5)
                        
    taskNumberField.grid(row = 5, column = 2)
 
    # pady proporciona un margen vertical desde el widget.                  
    delete.grid(row = 6, column = 2, pady = 5)
                        
    Exit.grid(row = 7, column = 2)
 
    # inicia la GUI 
    gui.mainloop()