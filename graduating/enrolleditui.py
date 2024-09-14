import tkinter as tk
from tkinter import ttk
from style import *

class EnrollEditUi(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Matricula")
        self.geometry("360x280")
        self.minsize(360,280)
        self.maxsize(360,280)
        
        self.style = CStyle()
        self.configure(background=background_color)
       
        ttk.Label(
            self, text=' Matricula', style='Title.TLabel'
        ).pack(side='top', fill='x')

        toolbar = ttk.Frame(self, style="Toolbar.TFrame")
        toolbar.pack(side='top', fill="x")
        
        save_img = tk.PhotoImage(file = "img/save.png")
        close_img = tk.PhotoImage(file = "img/close.png")
        
        self.btn_save = ttk.Button(toolbar, padding=(3,3,2,2), image=save_img)
        self.btn_save.img_ref = save_img
        self.btn_save.grid(row=0, column=0, padx=(6,0), pady=6)
        btn_close = ttk.Button(toolbar, padding=(3,3,2,2), image=close_img,
                               command=lambda: self.destroy())
        btn_close.img_ref = close_img
        btn_close.grid(row=0, column=1, padx=(3,0), pady=6)
        
        ttk.Separator(self, orient='horizontal').pack(fill='x')

        center = ttk.Frame(self, relief='groove')
        center.pack(anchor='nw')

        row_0 = ttk.Frame(center)
        ttk.Label(row_0, text='Aluno', width=8).grid(row=0, column=0)
        self.cb_student = ttk.Combobox(row_0, width=32)
        self.cb_student.grid(row=0, column=1, padx=3)
        row_0.grid(row=0, column=0)
        
        row_1 = ttk.Frame(center)
        ttk.Label(row_1, text='Situação', width=8).grid(row=0, column=0)
        self.var_status = tk.IntVar(value=1)
        check_status = ttk.Checkbutton(row_1, text="Ativo",
                                            variable=self.var_status)
        check_status.grid(row=0, column=1)
        row_1.grid(row=1, column=0)

        for child in center.winfo_children():
            child.grid_configure(sticky='nw', padx=6, pady=2)
