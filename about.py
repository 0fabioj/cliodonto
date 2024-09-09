import tkinter as tk
from tkinter import ttk

import sys

from style import *

class CAbout(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.msg = []			
        
        self.title("Sobre")
        self.geometry("380x280")
        
        self.style = CStyle()
        self.configure(background=background_color)
       
        ttk.Label(
            self, text=' Clinica de Odontologia', style='Title.TLabel'
        ).pack(side='top', fill='x')

        toolbar = ttk.Frame(self, style="Toolbar.TFrame")
        toolbar.pack(side='top', fill="x")     
        ttk.Button(toolbar, padding=(3,3,2,2), text='Fechar',
                               command=lambda: self.destroy()
                  ).grid(row=0, column=2, padx=(3,0), pady=3)  
        ttk.Separator(self, orient='horizontal').pack(fill='x')
        profile = ttk.Frame(self, relief='groove')
        profile.pack(anchor='nw', padx=(3,0), pady=(3,0))
        
        complement = ttk.Frame(self, relief='groove')
        complement.pack()

        row_0 = ttk.Frame(complement)
        ttk.Label(row_0, text='Clinica de Odontologia').grid(row=0, column=0)
        row_0.grid(row=0, column=0)

        row_1 = ttk.Frame(complement)
        lbl_1 = tk.Label(row_1)
        lbl_1.grid(row=0, column=0)
        row_1.grid(row=0, column=0)
        
        self.setup_info()
        lbl_1.configure(text="\n".join(self.msg))


    def setup_info(self):
        self.msg.append('Clinica de Odontologia')
        self.msg.append('Data: 16/06/2024')
        version = ".".join(map(str, sys.version_info[:3]))
        self.msg.append('Versões das bibliotecas: Python {} | Tkinter {}'.format(
                        version, tk.TkVersion))
        self.msg.append('Crédito: Fábio José Carnielo')
        self.msg.append('Licenças: LGPL GPL2 GPL3')
