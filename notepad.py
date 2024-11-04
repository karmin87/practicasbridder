import tkinter
import os    
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
 
class Notepad:
 
    __root = Tk()
 
    # ventana por defecto con altura y ancho
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
     
    # barra de desplazamiento
    __thisScrollBar = Scrollbar(__thisTextArea)     
    __file = None
 
    def __init__(self,**kwargs):
 
        # icono de la ventana
        try:
                self.__root.wm_iconbitmap("Notepad.ico") 
        except:
                pass
 
        # tamaño de la ventana por defecto
 
        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass
 
        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass
 
        # titulo de la ventana
        self.__root.title("Untitled - Notepad")
 
        # centrar la ventana
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()
     
        # para alinear a la izquierda
        left = (screenWidth / 2) - (self.__thisWidth / 2) 
         
        # para alinear a la derecha
        top = (screenHeight / 2) - (self.__thisHeight /2) 
         
        # para arriba y abajo
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top)) 
 
        # para hacer que el area de texto sea auto redimensionable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)
 
        # agregar controles (widget)
        self.__thisTextArea.grid(sticky = N + E + S + W)
         
        # para abrir un nuevo archivo
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)    
         
        # para abrir un archivo ya existente
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)
         
        # para guardar el archivo actual
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)    
 
        # para crear una linea en el dialogo        
        self.__thisFileMenu.add_separator()                                         
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)     
         
        # para dar una funcionalidad de cortar 
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)             
     
        # para dar una funcionalidad de copiar    
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)         
         
        # para dar una funcionalidad de pegar
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)         
         
        # para dar una funcionalidad de edicion
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)     
         
        # para crear una funcionalidad de descripcion de la aplicacion
        self.__thisHelpMenu.add_command(label="About Notepad",
                                        command=self.__showAbout) 
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)
 
        self.__root.config(menu=self.__thisMenuBar)
 
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                    
         
        # la barra de desplazamiento se ajustara automaticamente segun el contenido        
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)     
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
     
         
    def __quitApplication(self):
        self.__root.destroy()
        # exit()
 
    def __showAbout(self):
        showinfo("Notepad","Mrinal Verma")
 
    def __openFile(self):
         
        self.__file = askopenfilename(defaultextension=".txt",
                                      filetypes=[("All Files","*.*"),
                                        ("Text Documents","*.txt")])
 
        if self.__file == "":
             
            # no hay archivo para abrir
            self.__file = None
        else:
             
            # intentar abrir el archivo
            # cambiar el titulo de la ventana
            self.__root.title(os.path.basename(self.__file) + " - Notepad")
            self.__thisTextArea.delete(1.0,END)
 
            file = open(self.__file,"r")
 
            self.__thisTextArea.insert(1.0,file.read())
 
            file.close()
 
         
    def __newFile(self):
        self.__root.title("Untitled - Notepad")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)
 
    def __saveFile(self):
 
        if self.__file == None:
            # guardar como nuevo archivo
            self.__file = asksaveasfilename(initialfile='Untitled.txt',
                                            defaultextension=".txt",
                                            filetypes=[("All Files","*.*"),
                                                ("Text Documents","*.txt")])
 
            if self.__file == "":
                self.__file = None
            else:
                 
                # intentar guardar el archivo
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                 
                # cambiar el titulo de la ventana
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                 
             
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()
 
    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")
 
    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")
 
    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")
 
    def run(self):
 
        # ejecutar la aplicacion principal
        self.__root.mainloop()
 
 
 
 
# ejecutar la aplicacion principal
notepad = Notepad(width=600,height=400)
notepad.run()