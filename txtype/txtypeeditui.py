import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from style import *
from dictionary import *

class TxTypeEditUi(tk.Toplevel):
    def __init__(self):
        super().__init__()
			
        self.title("Detalhes")
        self.geometry("420x220")
        self.minsize(420,220)
        self.maxsize(420,220)
        
        self.style = CStyle()
        self.configure(background=background_color)
       
        ttk.Label(
            self, text=' Detalhe do Tipo de Tratamento', style='Title.TLabel'
        ).pack(side='top', fill='x')

        toolbar = ttk.Frame(self, style="Toolbar.TFrame")
        toolbar.pack(side='top', fill="x")
        
        save_img = tk.PhotoImage(file = "img/save.png")
        del_img = tk.PhotoImage(file = "img/delete.png")
        close_img = tk.PhotoImage(file = "img/close.png")
        
        self.btn_save = ttk.Button(toolbar, padding=(3,3,2,2), image=save_img)
        self.btn_save.img_ref = save_img
        self.btn_save.grid(row=0, column=0, padx=(3,0), pady=3)
        self.btn_del = ttk.Button(toolbar, padding=(3,3,2,2), image=del_img)
        self.btn_del.img_ref = del_img
        self.btn_del.grid(row=0, column=1, padx=(3,0), pady=3)
        btn_close = ttk.Button(toolbar, padding=(3,3,2,2), image=close_img,
                               command=lambda: self.destroy())
        btn_close.img_ref = close_img
        btn_close.grid(row=0, column=2, padx=(3,0), pady=3)
       
        ttk.Separator(self, orient='horizontal').pack(fill='x')
        profile = ttk.Frame(self, relief='groove')
        profile.pack(anchor='nw', padx=(3,0), pady=(3,0))
        
        row_0 = ttk.Frame(profile)
        ttk.Label(row_0, text='Id', width=8).grid(row=0, column=0)
        self.entry_id = ttk.Entry(row_0, width=12)
        self.entry_id.grid(row=0, column=1, padx=3)
        row_0.grid(row=0, column=0)
        
        row_1 = ttk.Frame(profile)
        ttk.Label(row_1, text='Nome', width=8).grid(row=0, column=0)
        self.entry_name = ttk.Entry(row_1, width=40)
        self.entry_name.grid(row=0, column=1, padx=3)
        row_1.grid(row=1, column=0)
        
        row_2 = ttk.Frame(profile)
        ttk.Label(row_2, text='Situação', width=8).grid(row=0, column=0)
        self.var_status = tk.IntVar(value=1)
        check_status = ttk.Checkbutton(row_2, text="Ativo",
                                            variable=self.var_status)
        check_status.grid(row=0, column=1)
        row_2.grid(row=2, column=0)
        
        for child in profile.winfo_children():
            child.grid_configure(sticky='w', padx=6, pady=2)
