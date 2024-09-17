import tkinter as tk
from tkinter import ttk
from style import *

class SearchUi(tk.Toplevel):
    def __init__(self):
        super().__init__()

        self.title("Buscar")
        self.geometry("440x280")
        self.minsize(440,280)
        self.maxsize(440,280)
        
        self.style = CStyle()
        self.configure(background=background_color)

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
        
        # Filtro
        filterbar = ttk.Frame(self, style='Transparent.TFrame')
        filterbar.pack()

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

        self.status_var = tk.StringVar(value=1)
        self.filter_status = ttk.Checkbutton(filterbar, text='Ativos'
                                             ,variable=self.status_var)
        self.filter_status.grid(row=0, column=1, sticky='e')
        
        # Tabela
        center = ttk.Frame(self)
        center.pack(side='bottom', fill='x')
        
        colsdata_1 = ('id','nome')
        self.tbl_1 = ttk.Treeview(center, show='headings',
                                  columns=colsdata_1, height=12) 
        self.tbl_1.heading('#1', text='Id', anchor='w')
        self.tbl_1.heading('#2', text='Nome', anchor='w')
        self.tbl_1.column('#1', width=100, stretch=False)
        self.tbl_1.column('#2', width=260, stretch=True)
        vscrlbar_1 = ttk.Scrollbar(center, orient='vertical',
                                   command = self.tbl_1.yview)
        self.tbl_1.configure(yscrollcommand = vscrlbar_1.set)
        vscrlbar_1.pack(side='right', fill='y')
        self.tbl_1.pack(expand=True, fill='x')
