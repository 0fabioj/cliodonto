import tkinter as tk
from tkinter import ttk

from style import *

class PatientUi(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Pacientes - Clinica de Odontologia")
        self.geometry("800x500")
        self.minsize(800,500)
        self.style = CStyle()
        self.configure(background=background_color)
        self.configure(highlightbackground="wheat")
        self.configure(highlightcolor=on_background_color)

        # Title
        ttk.Label(
            self, text=' Lista de Pacientes', style="Title.TLabel"
        ).pack(side='top', fill='x')
        
        # Toolbar
        toolbar = self.create_toolbar() 
        toolbar.pack(fill='x')
        ttk.Separator(self, orient='horizontal').pack(fill='x')
        
        # Filter
        filterbar = self.create_filter() 
        filterbar.pack(padx=6, pady=(6,0), fill='x')
        
        # Treeview
        center = self.create_center()
        center.pack(expand=True, fill='both', padx=8, pady=8)
        

    def create_toolbar(self) -> ttk.Frame:
        toolbar = ttk.Frame(self)
        #toolbar.pack(fill='x')

        add_img = tk.PhotoImage(file="img/add.png")
        self.btn_add = ttk.Button(toolbar, image=add_img, compound='left',
                             text="Adicionar", padding=(3,3,2,2))
        self.btn_add.img_ref = add_img
        self.btn_add.grid(row = 0, column=0, sticky='nsew', padx=(6,0), pady=6)
        
        ttk.Button(
            toolbar, text="Fechar", command=lambda: self.on_close_window()
        ).grid(row=0, column=1, sticky='nsew', padx=(3,0), pady=6)
        return toolbar


    def on_close_window(self):
        self.destroy()
   

    def create_filter(self) -> ttk.Frame:
        filterbar = ttk.Frame(self, style='Transparent.TFrame')
        filterbar.grid_columnconfigure(0, weight=1) 
        filterbar.grid_columnconfigure(1, weight=1) 

        searchbar = ttk.Frame(filterbar, style='Transparent.TFrame')
        searchbar.grid(row=0, column=0, sticky='w')
        self.search_var = tk.StringVar()
        pesquisa = ttk.Entry(searchbar, width=30
                             ,textvariable=self.search_var)
        pesquisa.grid(row = 0, column = 1, sticky = 'w')
        search_img = tk.PhotoImage(file = "img/search.png")
        lbl_search = ttk.Label(searchbar, image=search_img)
        lbl_search.grid(row = 0, column = 0, sticky = 'w')
        lbl_search.img_ref = search_img
        clear_img = tk.PhotoImage(file = "img/close.png")
        lbl_clear = ttk.Label(searchbar, image=clear_img)
        lbl_clear.grid(row=0, column=2, sticky='w')
        lbl_clear.img_ref = clear_img
        lbl_clear.bind("<Button-1>", lambda event: pesquisa.delete(0,'end'))
        
        return filterbar 


    def create_center(self) -> ttk.Frame:
        center = ttk.Frame(self)

        colsdata = ('id','nome','gender','rg','cpf','birthdate',
                    'maritalstatus','occupation','email','phone',
                    'phone2','address','addressnumber','addresscomplement')
        self.tbl_1 = ttk.Treeview(center, show='headings', columns=colsdata)

        self.tbl_1.heading('#1', text='Id', anchor='w')
        self.tbl_1.heading('#2', text='Nome', anchor='w')
        self.tbl_1.heading('#3', text='Genero', anchor='w')
        self.tbl_1.heading('#4', text='RG', anchor='w')
        self.tbl_1.heading('#5', text='CPF', anchor='w')
        self.tbl_1.heading('#6', text='Nascimento', anchor='w')
        self.tbl_1.heading('#7', text='Estado', anchor='w')
        self.tbl_1.heading('#8', text='Ocupação', anchor='w')
        self.tbl_1.heading('#9', text='Email', anchor='w')
        self.tbl_1.heading('#10', text='Telefone', anchor='w')
        self.tbl_1.heading('#11', text='Telefone', anchor='w')
        self.tbl_1.heading('#12', text='Endereço', anchor='w')
        self.tbl_1.heading('#13', text='Numero', anchor='w')
        self.tbl_1.heading('#14', text='Complemento', anchor='w')
        
        self.tbl_1.column('#1', minwidth=30, width=50, stretch=False)
        self.tbl_1.column('#2', minwidth=100, width=200, stretch=True)
        self.tbl_1.column('#3', minwidth=10, width=60, stretch=False)
        self.tbl_1.column('#4', minwidth=0, width=0, stretch=False)
        self.tbl_1.column('#5', minwidth=0, width=0, stretch=False)
        self.tbl_1.column('#6', minwidth=80, width=120, stretch=False)
        self.tbl_1.column('#7', minwidth=0, width=0, stretch=False)
        self.tbl_1.column('#8', minwidth=0, width=0, stretch=False)
        self.tbl_1.column('#9', minwidth=0, width=0, stretch=False)
        self.tbl_1.column('#10', minwidth=30, width=120, stretch=False)
        self.tbl_1.column('#11', minwidth=0, width=0, stretch=False)
        self.tbl_1.column('#12', minwidth=0, width=0, stretch=False)
        self.tbl_1.column('#13', minwidth=0, width=0, stretch=False)
        self.tbl_1.column('#14', minwidth=0, width=0, stretch=False)        
        
        vscrlbar = ttk.Scrollbar(center, orient ="vertical", 
                                   command = self.tbl_1.yview)

        self.tbl_1.configure(yscrollcommand = vscrlbar.set)
        
        vscrlbar.pack(side='right', fill='y')
        self.tbl_1.pack(expand=True, fill="both")
        
        statusbar = ttk.Frame(center)
        statusbar.configure(style='Statusbar.TFrame')
        statusbar.pack(side='bottom', fill='x')
        self.lbl_status = ttk.Label(
                statusbar, text='Pronto'
        )
        self.lbl_status.pack(anchor='nw', padx=6)
        return center


    def set_msgstatus(self, msg):
        self.lbl_status.config(text=msg)
