import tkinter as tk
from tkinter import ttk
from style import *

class TxEditUi(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Procedimento")
        self.geometry("360x280")
        self.minsize(360,280)
        self.maxsize(360,280)
        
        self.style = CStyle()
        self.configure(background=background_color)
       
        ttk.Label(
            self, text=' Procedimento', style='Title.TLabel'
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

        center = ttk.Frame(self)
        center.pack(anchor='nw')

        profile = ttk.Frame(center, relief='groove')
        profile.grid(row=0, column=0)
        
        field_disciplina = ttk.LabelFrame(profile, text='Disciplina')
        self.combo_disciplina = ttk.Combobox(field_disciplina, width=36)
        self.combo_disciplina.pack()
        field_disciplina.grid(row=0, column=0)
        
        field_procedimento = ttk.LabelFrame(profile, text='Procedimento')
        self.combo_procedimento = ttk.Combobox(field_procedimento, width=36)
        self.combo_procedimento.pack()
        field_procedimento.grid(row=1, column=0)
        
        field_obs = ttk.LabelFrame(profile, text='Obs.')
        self.entry_obs = tk.Text(field_obs, height=5, width=42)
        self.entry_obs.configure(font='TkTextFont 9 normal')
        self.entry_obs.pack()
        field_obs.grid(row=2, column=0)

        for child in profile.winfo_children():
            child.grid_configure(sticky='nw', padx=6, pady=2)
        
        status_msg = ttk.Label(self, text="Pronto")
        status_msg.pack(side='bottom', fill='x', padx=4)
