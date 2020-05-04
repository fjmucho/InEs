"""
Fem illustration: 0.0.6

Your first GUI application - the top level window
Adding some widgets

@Tkinter GUI Application Development
"""
__author__ = 'F. Jimenez Mucho'
__title__ = 'Structural Analysis Matrix'
__date__ = '06/04/2020'
__version__ = 'InEs 0.0.6'
__license__ = 'GNU GPLv3'


import sys
PYTHON_VERSION = sys.version_info.major

if PYTHON_VERSION < 3:
    try:
        import Tkinter
    except ImportError:
        raise ImportError("Se requiere el modulo ...")
else:
    try:
        import tkinter as tk
        import tkinter.messagebox as msgbox
        import platform
        from tkinter import ttk, font, filedialog
        import tkinter.tix as tix
    except ImportError:
        raise ImportError("Se requiere el modulo ...")

# Constante
PROGRAM_NAME  = "Structural Analysis Matrix" 
FILE_ICO_LOGO = "iconapp.ico"
info1 = platform.system()
info2 = platform.node()
info3 = platform.machine()
mensaje = " " + info1+" "+info3+": "+info2
file_name = None

class AppFem(tk.Tk): 
    WINSize=  '500x300+0+0'
    WINSizeX, WINSizeY= 300, 230
    winBackgroundColor="#ccc"
    def __init__(self):
        super().__init__()
        self.title(PROGRAM_NAME)
        self.iconbitmap(FILE_ICO_LOGO)
        self.geometry(self.WINSize)
        self.minsize(self.WINSizeX,self.WINSizeY)
        self.config(bg=self.winBackgroundColor)

        self.initUI();

    def initUI(self):
        # DECLARAR VARIABLE PARA MOSTRAR
        ## 
        self.checkedMenuBar = tk.BooleanVar()
        self.checkedMenuBar.trace("w", self.markCheckedMenuBar)
        ## 
        self.checkedToolBar = tk.BooleanVar()
        self.checkedToolBar.trace("w", self.markChecked)
        ## 
        self.checkedSideBar = tk.BooleanVar()
        self.checkedSideBar.trace("w", self.markChecked)
        ## BARRA DE ESTADO:        
        self.checkedStatusBar = tk.BooleanVar()
        # self.checkedStatusBar.trace("w", self.onStatebarWindow)
        self.checkedStatusBar.set(True)
        ## 
        self.checkedConsole = tk.BooleanVar()
        self.checkedConsole.trace("w", self.markChecked)


        self.menuBar = tk.Menu(self)  # menu begins

        self.file_menu = tk.Menu(self.menuBar, tearoff=0)
        self.file_menu.add_command(label='New Model', accelerator="Ctrl+N", command=self.newModelStruct)
        self.file_menu.add_command(label="Open", accelerator="Ctrl+O", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", accelerator="Ctrl+S", command=self.modelSave)
        self.file_menu.add_command(label="Save as...", accelerator="Ctrl+Shift+S", command=self.modelSaveAs)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Quit - Exit", accelerator="Ctrl-Q", command=self.destroy)
        
        self.edit_menu = tk.Menu(self.menuBar, tearoff=0)
        self.edit_menu.add_command(label="Undo", accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", accelerator="Ctrl+Y")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy", accelerator="Ctrl+C")
        self.edit_menu.add_command(label="Cut", accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Paste", accelerator="Ctrl+V")
        
        self.view_menu = tk.Menu(self.menuBar, tearoff=0)
        self.view_menu.add_checkbutton(label="Show Menu", onvalue=True,
                                offvalue=False, variable=self.checkedMenuBar)
        self.view_menu.add_checkbutton(label="Show toolbar", onvalue=True,
                                offvalue=False, variable=self.checkedToolBar)
        self.view_menu.add_checkbutton(label="Show Side bar", onvalue=True,
                                offvalue=False, variable=self.checkedSideBar)
        self.view_menu.add_checkbutton(label="Show Status bar", 
                                variable=self.checkedStatusBar,
                                onvalue=True,
                                offvalue=False,
                                command=self.onStatebarWindow)
        self.view_menu.add_checkbutton(label="Show Console", onvalue=True,
                                offvalue=False, variable=self.checkedConsole)
        self.view_menu.add_checkbutton(label="Show Command UIConsole Only")
        self.view_menu.add_separator()
        
        self.tools_menu = tk.Menu(self.menuBar, tearoff=0)
        self.tools_menu.add_command(label="Command Palette...")
        self.tools_menu.add_command(label="Build")
        self.tools_menu.add_command(label="Cancel Build")
        self.tools_menu.add_command(label="Build Results")
        self.tools_menu.add_command(label="Save Build Results")
        self.tools_menu.add_separator()
        self.tools_menu.add_command(label="Macros")
        
        
        self.prefereces_menu = tk.Menu(self.menuBar, tearoff=0)
        self.prefereces_menu.add_command(label="Settings - Default")
        self.prefereces_menu.add_command(label="Settings - User")
        self.prefereces_menu.add_separator()
        self.prefereces_menu.add_command(label="Color Scheme...")
        self.prefereces_menu.add_command(label="Theme...")
        self.prefereces_menu.add_separator()
        self.prefereces_menu.add_command(label="Package Control")

        self.help_menu = tk.Menu(self.menuBar, tearoff=0)
        self.help_menu.add_command(label="Documentation")
        self.help_menu.add_command(label="Twitter")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Update Licence")
        self.help_menu.add_command(label="Remove Licence")
        self.help_menu.add_separator()
        self.help_menu.add_command(label="Changelog Calendar...")
        self.help_menu.add_command(label="About", command=self.onAboutWindow)

        self.menuBar.add_cascade(label='File', menu=self.file_menu)
        self.menuBar.add_cascade(label='Edit', menu=self.edit_menu)
        self.menuBar.add_cascade(label='View', menu=self.view_menu)
        self.menuBar.add_cascade(label='tools', menu=self.tools_menu)
        self.menuBar.add_cascade(label='prefereces', menu=self.prefereces_menu)
        self.menuBar.add_cascade(label='help', menu=self.help_menu)

        # ------------command:comandos - key:teclado----------------
        ## File
        self.bind("<Control-n>", lambda event: self.onDeverlopment())
        self.bind("<Control-N>", lambda event: self.onDeverlopment())
        self.bind("<Control-o>", lambda event: self.onDeverlopment())
        self.bind("<Control-O>", lambda event: self.onDeverlopment())
        self.bind("<Control-s>", lambda event: self.onDeverlopment())
        self.bind("<Control-S>", lambda event: self.onDeverlopment())
        self.bind("<Control-q>", lambda event: self.onCloseWindow())
        self.bind("<Control-Q>", lambda event: self.onCloseWindow())
        ## Edit
        self.bind("<Control-c>", lambda event: self.onDeverlopment())
        self.bind("<Control-C>", lambda event: self.onDeverlopment())
        ## Tools
        self.bind("<Control-b>", lambda event: self.onDeverlopment())
        self.bind("<Control-B>", lambda event: self.onDeverlopment())

    # menu ends
        self.config(menu=self.menuBar)

        # DEFINIR BARRA DE ESTADO:
        # Muestra información del equipo
        self.barraest = tk.Label(self, text="mensaje", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.barraest.pack(side=tk.BOTTOM, fill=tk.X)



# crear nuevo modelo
    def newModelStruct(self):
        newTypeStruct = tk.Toplevel()
        newTypeStruct.iconbitmap(FILE_ICO_LOGO)
        newTypeStruct.geometry("470x200")
        newTypeStruct.resizable(width=False, height=False)
        newTypeStruct.title("Definir el tipo de estructura...")
        fuente = font.Font(weight='normal')
        marcoTS = ttk.Frame(newTypeStruct, padding=(10, 10, 10, 10))
        marcoTS.pack(expand=False)
        imgLogo=tk.PhotoImage(file='./logo-57x57.png')
        # ----
        pnl_1 = tk.LabelFrame(marcoTS, padx=15, pady=10, text="Seleccione la estructura")
        pnl_1.pack(padx=10, pady=5)
        # --- button icons
        btn0ts = tk.Button(pnl_1,text='nuevo').grid(row=0, column=0, sticky=tk.W)
        btn1ts = tk.Button(pnl_1,text='grid_only').grid(row=0, column=1, sticky=tk.W)
        btn2ts = tk.Button(pnl_1,text='beam').grid(row=0, column=2, sticky=tk.W)
        btn3ts = tk.Button(pnl_1,text='truss2D').grid(row=0, column=3, sticky=tk.W)
        btn4ts = tk.Button(pnl_1,text='truss3D').grid(row=0, column=4, sticky=tk.W)
        btn5ts = tk.Button(pnl_1,text='frame2d').grid(row=0, column=5, sticky=tk.W)
        # boton Deshabilitado
        # boton.config(state = 'disabled')
        # --- labels
        tk.Label(pnl_1, text="Nuevo").grid(row=1, column=0)
        tk.Label(pnl_1, text="Grid only").grid(row=1, column=1)
        tk.Label(pnl_1, text="Beam").grid(row=1, column=2)
        tk.Label(pnl_1, text="2D Truss").grid(row=1, column=3)
        tk.Label(pnl_1, text="3D Truss").grid(row=1, column=4)
        tk.Label(pnl_1, text="2D Frame").grid(row=1, column=5)
        # --- campo de entrada y label
        pnl_2 = tk.LabelFrame(marcoTS, padx=15, pady=10, text="Unidad de medidad.")
        pnl_2.pack(padx=10, pady=5)
        tk.Label(pnl_2, text="Unidad.").grid(row=0)
        tk.Entry(pnl_2).grid(row=0, column=1, sticky=tk.W)
        newTypeStruct.transient(self)   # para agregar en la ventana principal
        self.wait_window(newTypeStruct) # para mantener en la ventana principal

        # return tstruct;
    def onDeverlopment(self):
        print('Pruebas')

    # abrir modelo guardado 
    def open_file(event=None):
        input_file_name = tk.filedialog.askopenfilename(defaultextension=".jm", 
            initialdir='/',
            filetypes=[("Json matrix", "*.jm *.json"), ("Paper calc", "*.xlsx"),
            ("Text documents", "*.txt"),("All Files", "*.*")])
        if input_file_name:
            global file_name
            file_name = input_file_name
            ventana.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
            content_text.delete(1.0, END)
            with open(file_name) as _file:
                content_text.insert(1.0, _file.read())
    # ----------guardar todos los archivos--------
    def modelSaveAs(event=None):
        input_file_name = tk.filedialog.asksaveasfilename(defaultextension=".txt",
        filetypes=[("Json Matrix Documents", "*.jm"), ("Paper calc", "*.xlsx"),
        ("calc...", "*.csv"), ("Text Documents", "*.txt")])
        if input_file_name:
            global file_name
            file_name = input_file_name
            write_to_file(file_name)
            ventana.title('{} - {}'.format(os.path.basename(file_name), PROGRAM_NAME))
        return "break"
    # ---------------grardar un archivo-----------
    def modelSave(event=None):
        global file_name
        if not file_name:
            print('llamada ay que solucionar')
            msgbox.showinfo(message='No esta implementado ....')
            # save_as()
        else:
            print('falta implementar')
            msgbox.showinfo(message='No esta implementado ....')
            # write_to_file(file_name)
        return "break"
# end funciones de ejecucion


    def markCheckedMenuBar(self, *args):
        print(self.checkedMenuBar.get())
        msgbox.showinfo(message='No esta implementado por completo ....')

    def markChecked(self, *args):
        print('falta implementar checkeds...')
        msgbox.showinfo(message='No esta implementado por completo ....')

    # def f_web(self):
    #     ''' Abrir página web en navegador Internet '''
    #     pag1 = 'http://.com/'
    #     webbrowser.open_new_tab(pag1)
    def onStatebarWindow(self):
        ''' Ocultar o Mostrar barra de checkedStatusBar '''
        if self.checkedStatusBar.get() == False:
            self.barraest.pack_forget()
        else:
            self.barraest.pack(side=tk.BOTTOM, fill=tk.X)
    
    def onAboutWindow(self):
        ''' Definir ventana de diálogo 'Acerca de' '''
        acerca = tk.Toplevel()
        acerca.iconbitmap(FILE_ICO_LOGO)
        acerca.geometry("320x170")
        acerca.resizable(width=False, height=False)
        acerca.title("Acerca de ...")
        fuente = font.Font(weight='normal')
        marcoAcercaDe = ttk.Frame(acerca, padding=(10, 10, 10, 10))
        marcoAcercaDe.pack( expand=False)
        imgLogo=tk.PhotoImage(file='./logo-57x57.png')
        etiq1 = tk.Label(marcoAcercaDe, image=imgLogo, relief='ridge') # relief='raised'
        etiq1.pack(padx=10, pady=10, ipadx=10, ipady=10)
        etiq2 = tk.Label(marcoAcercaDe, text="UNI "+__version__+"\n"+mensaje, foreground='blue')
        etiq2.pack(padx=10)
        etiq3 = tk.Label(marcoAcercaDe, text= "Descrion ...")
        etiq3.pack(padx=10)
        acerca.transient(self)
        self.wait_window(acerca)

    def onCloseWindow(self):
        ''' Salir de la aplicación '''
        self.destroy()
        # quit()
        return 0


def main():
    ventana=AppFem()
    ventana.mainloop()

if __name__ == '__main__':
    main()
