import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter import messagebox

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        # Titulo
        self.title('Editor de texto')
        # Configuración de pantalla y texto
        self.rowconfigure(0, minsize=600, weight=1)
        self.columnconfigure(1, minsize=600, weight=1)
        self.text_area = tk.Text(self, wrap=tk.WORD)
        # Verificación de archivo
        self.archivo = None
        self.archivo_abierto = False
        self.contenido_inicial = ""

        # Creación de menú
        self._crear_menu()
        self._crear_componente()
        
        # Configurar on_closing al evento de cierre
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def _crear_componente(self):
        self.text_area.grid(row=0, column=1, sticky='nsew')

    def _crear_menu(self):
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        archivo_menu = tk.Menu(menu_app, tearoff=0)
        menu_app.add_cascade(label='Archivo', menu=archivo_menu)
        archivo_menu.add_command(label='Abrir', command=self._abrir_archivo)
        archivo_menu.add_command(label='Guardar', command=self._guardar)
        archivo_menu.add_command(label='Guardar como', command=self._guardar_como)
        archivo_menu.add_separator()
        archivo_menu.add_command(label='Salir', command=self.quit)

    def _abrir_archivo(self):
        archivo = askopenfilename(title='Abrir archivo', filetypes=[('Archivos de texto', '*.txt'), ('Todos los archivos', '*.*')])
        if archivo:
            with open(archivo, 'r') as f:
                self.text_area.delete(1.0, tk.END)
                contenido = f.read()
                self.text_area.insert(tk.END, contenido)
                self.contenido_inicial = contenido
            self.archivo = archivo
            self.archivo_abierto = True
        else:
            self.archivo = None
            self.archivo_abierto = False
            self.contenido_inicial = ""

    def _guardar(self):
        if self.archivo_abierto:
            with open(self.archivo, 'w') as f:
                f.write(self.text_area.get(1.0, tk.END))
            self.contenido_inicial = self.text_area.get(1.0, tk.END)
        else:
            self._guardar_como()

    def _guardar_como(self):
        archivo = asksaveasfilename(title='Guardar archivo como', defaultextension='.txt', filetypes=[('Archivos de texto', '*.txt'), ('Todos los archivos', '*.*')])
        if archivo:
            with open(archivo, 'w') as f:
                f.write(self.text_area.get(1.0, tk.END))
            self.archivo = archivo
            self.archivo_abierto = True
            self.contenido_inicial = self.text_area.get(1.0, tk.END)

    # Alerta para guardar lo que no se ha guardado
    def on_closing(self):
        respuesta = None
        contenido_actual = self.text_area.get(1.0, tk.END)
        if (self.archivo_abierto and contenido_actual.strip() != self.contenido_inicial.strip()) or (not self.archivo_abierto and contenido_actual.strip()):
            respuesta = messagebox.askyesnocancel('Alerta', 'El archivo no ha sido guardado. ¿Desea guardar antes de salir?')
            if respuesta:  # Si el usuario responde 'Sí'
                self._guardar()
            elif respuesta is None:  # Si el usuario responde 'Cancelar'
                return
        self.destroy()

if __name__ == "__main__":
    app = Editor()
    app.mainloop()
