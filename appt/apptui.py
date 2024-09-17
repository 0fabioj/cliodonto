import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

from style import *

class ApptUi(tk.Frame):
    def __init__(self):
        super().__init__()

        self.style = CStyle()
        self.configure(background=background_color)
        self.configure(highlightbackground="wheat")
        self.configure(highlightcolor=on_background_color)

        # Title
        ttk.Label(
            self, text=' Agenda', style="Title.TLabel"
        ).pack(side='top', fill='x')
        
        # Toolbar
        toolbar = self.create_toolbar() 
        toolbar.pack(fill='x')
        ttk.Separator(self, orient='horizontal').pack(fill='x')
        
        # Treeview
        center = self.create_center()
        center.pack(fill='both', expand=True, padx=3, pady=3)

        # Filter
        filterbar = self.create_filter() 
        #filterbar.pack(side='left', anchor='nw', pady=36)
        filterbar.pack(anchor='nw', padx=3, pady=(0,3))        


    def create_toolbar(self) -> ttk.Frame:
        toolbar = ttk.Frame(self, style="Toolbar.TFrame")

        add_img = tk.PhotoImage(file="img/add.png")        
        self.btn_add = ttk.Button(toolbar, image=add_img, compound='left',
                             text="Adicionar", padding=(3,3,2,2))
        self.btn_add.img_ref = add_img
        self.btn_add.grid(row = 0, column=0, sticky='nsew', padx=(6,0), pady=6)
        
        return toolbar


    def on_close_window(self):
        self.destroy()
   

    def create_filter(self) -> ttk.Frame:
        filterbar = ttk.Frame(self, relief='groove')

        ttk.Label(filterbar, text='Filtros').grid(row=0, column=0)
        ttk.Label(filterbar, text='Paciente').grid(row=1, column=0)

        searchbar = ttk.Frame(filterbar, style='Transparent.TFrame')
        searchbar.grid(row=2, column=0, columnspan=2)
        self.search_var = tk.StringVar()
        pesquisa = ttk.Entry(searchbar, width=24
                             ,textvariable=self.search_var)
        pesquisa.grid(row = 0, column = 1)
        search_img = tk.PhotoImage(file = "img/search.png")
        lbl_search = ttk.Label(searchbar, image=search_img)
        lbl_search.grid(row = 0, column = 0)
        lbl_search.img_ref = search_img
        clear_img = tk.PhotoImage(file = "img/close.png")
        lbl_clear = ttk.Label(searchbar, image=clear_img)
        lbl_clear.grid(row=0, column=2)
        lbl_clear.img_ref = clear_img
        lbl_clear.bind("<Button-1>", lambda event: pesquisa.delete(0,'end'))

        ttk.Label(filterbar, text='Intervalo').grid(row=1, column=2)
        ttk.Label(filterbar, text='Inicio').grid(row=2, column=2)
        self.filter_date1 = DateEntry(filterbar, locale='pt_BR', width='10')
        self.filter_date1.grid(row=2, column=3)
        ttk.Label(filterbar, text='Final').grid(row=3, column=2)
        self.filter_date2 = DateEntry(filterbar, locale='pt_BR', width='10')
        self.filter_date2.grid(row=3, column=3)
        
        
        for child in filterbar.winfo_children():
            child.grid_configure(sticky='nw', padx=3, pady=2)

        return filterbar 


    def create_center(self) -> ttk.Frame:
        center = ttk.Frame(self)

        sel_date = ttk.Frame(center)
        sel_date.pack()

        self.btn_today = ttk.Button(sel_date, text='Hoje')
        self.btn_today.grid(row=0, column=0, padx=(0,30))
        
        next_img = tk.PhotoImage(file="img/forward.png")
        prev_img = tk.PhotoImage(file="img/back.png")
        self.btn_prev = ttk.Button(sel_date, image=prev_img)
        self.btn_prev.img_ref = prev_img
        self.btn_prev.grid(row=0, column=1)
        self.btn_next = ttk.Button(sel_date, image=next_img)
        self.btn_next.img_ref = next_img
        self.btn_next.grid(row=0, column=3)
        self.date_var = tk.StringVar(sel_date)
        lbl_date = ttk.Label(sel_date, textvariable=self.date_var)
        lbl_date.grid(row=0, column=2)

        colsdata = ('id','bookdate','booktime','patient',
                    'student','assistant','teacher','status')
        self.tbl_1 = ttk.Treeview(center, show='headings',
                                  columns=colsdata)
        
        self.tbl_1.heading('#1', text='Id', anchor='w')
        self.tbl_1.heading('#2', text='Data', anchor='w')
        self.tbl_1.heading('#3', text='Horário', anchor='w')
        self.tbl_1.heading('#4', text='Paciente', anchor='w')
        self.tbl_1.heading('#5', text='Aluno', anchor='w')
        self.tbl_1.heading('#6', text='Assistente', anchor='w')
        self.tbl_1.heading('#7', text='Professor', anchor='w')
        self.tbl_1.heading('#8', text='Situação', anchor='w')
        
        self.tbl_1.column('#1', width=0, stretch=False)
        self.tbl_1.column('#2', width=84, stretch=False)
        self.tbl_1.column('#3', width=70, stretch=False)
        self.tbl_1.column('#4', width=150, stretch=True)
        self.tbl_1.column('#5', width=190, stretch=True)
        self.tbl_1.column('#6', width=190, stretch=True)
        self.tbl_1.column('#7', width=150, stretch=True)
        self.tbl_1.column('#8', width=84, stretch=False)
        
        vscrlbar = ttk.Scrollbar(center, orient ="vertical", 
                                   command = self.tbl_1.yview)

        self.tbl_1.configure(yscrollcommand = vscrlbar.set)
        
        vscrlbar.pack(side='right', fill='y')
        self.tbl_1.pack(side='right', fill='both', expand=True, pady=6)
        
        return center
