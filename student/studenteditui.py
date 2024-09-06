import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from style import *
from dictionary import *

class StudentEditUi(tk.Toplevel):
    def __init__(self):
        super().__init__()
			
        self.title("Detalhes")
        self.geometry("636x380")
        self.minsize(636,380)
        self.maxsize(636,380)
        
        self.style = CStyle()
        self.configure(background=background_color)
       
        ttk.Label(
            self, text=' Detalhe do Aluno', style='Title.TLabel'
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
        ttk.Label(row_0, text='RA', width=8).grid(row=0, column=0)
        self.entry_ra = ttk.Entry(row_0, width=12)
        self.entry_ra.grid(row=0, column=1, padx=3)
        row_0.grid(row=0, column=0)
        
        row_1 = ttk.Frame(profile)
        ttk.Label(row_1, text='Nome', width=8).grid(row=0, column=0)
        self.entry_name = ttk.Entry(row_1, width=40)
        self.entry_name.grid(row=0, column=1, padx=3)
        row_1.grid(row=1, column=0)
        
        for child in profile.winfo_children():
            child.grid_configure(sticky='w', padx=6, pady=2)

        content = ttk.Frame(self, style='Transparent.TFrame')
        content.pack(anchor='nw')
        
        complement = ttk.Frame(content, relief='groove')
        complement.grid(row=0, column=0, sticky='nw',
                        padx=(3,0), pady=(3,0))

        row_2 = ttk.Frame(complement)
        ttk.Label(row_2, text='Telefone', width=8).grid(row=0, column=0)
        self.entry_phone = ttk.Entry(row_2, width=16)
        self.entry_phone.grid(row=0, column=1, padx=3)
        row_2.grid(row=0, column=0)

        row_3 = ttk.Frame(complement)
        ttk.Label(row_3, text='Email', width=8).grid(row=0, column=0)
        self.entry_email = ttk.Entry(row_3, width=32)
        self.entry_email.grid(row=0, column=1, padx=3)
        row_3.grid(row=1, column=0)
        
        row_4 = ttk.Frame(complement)
        ttk.Label(row_4, text='Situação', width=8).grid(row=0, column=0)
        self.var_status = tk.IntVar(value=1)
        check_status = ttk.Checkbutton(row_4, text="Ativo",
                                            variable=self.var_status)
        check_status.grid(row=0, column=1)
        row_4.grid(row=2, column=0)
        
        for child in complement.winfo_children():
            child.grid_configure(sticky='w', padx=6, pady=2)

        # TURMA
        frame_grad = ttk.Frame(content, relief='groove')
        frame_grad.grid(row=1, column=0,
                        sticky='nw', padx=(3,0), pady=(3,0))
        
        frame_grad_header = ttk.Frame(frame_grad)
        frame_grad_header.pack(fill=tk.BOTH, padx=3, pady=(3,0))  
        self.total_2 = ttk.Label(frame_grad_header)
        self.total_2.pack(fill=tk.BOTH, padx=3, pady=(3,0))                                     
        colsdata2 = ('gradid','grad','status')
        self.tbl_2 = ttk.Treeview(frame_grad, show='headings',
                                  columns=colsdata2, height=6)       
        self.tbl_2.heading('#1', text='GradId', anchor='w')
        self.tbl_2.heading('#2', text='Turma', anchor='w')
        self.tbl_2.heading('#3', text='Situação', anchor='w')
        self.tbl_2.column('#1', width=0, stretch=False)
        self.tbl_2.column('#2', width=220, stretch=False)
        self.tbl_2.column('#3', width=80, stretch=False)
        vscrlbar2 = ttk.Scrollbar(frame_grad, orient='vertical',
                                 command = self.tbl_2.yview)
        self.tbl_2.configure(yscrollcommand = vscrlbar2.set)
        vscrlbar2.pack(side='right', fill='y')
        self.tbl_2.pack(expand=True, fill='x', padx=(6,0), pady=(0,6))
        
        # Consultas
        colsdata = ('id','date')
        frame_tree = ttk.Label(content, relief='groove')
        frame_tree.grid(row=0, column=1, rowspan=2,
                        padx=(3,0), pady=(3,0))
        self.total_1 = ttk.Label(frame_tree)
        self.total_1.pack(fill=tk.BOTH, padx=6, pady=(6,0))

        self.tbl_consultas = ttk.Treeview(frame_tree, show='headings', columns=colsdata)       
        self.tbl_consultas.heading('#1', text='Id', anchor='w')
        self.tbl_consultas.heading('#2', text='Data', anchor='w')        
        self.tbl_consultas.column('#1', minwidth=30, width=50, stretch=False)
        self.tbl_consultas.column('#2', minwidth=100, width=200, stretch=True)       
        vscrlbar = ttk.Scrollbar(frame_tree, orient ="vertical", 
                                   command = self.tbl_consultas.yview)
        self.tbl_consultas.configure(yscrollcommand = vscrlbar.set)
        vscrlbar.pack(side='right', fill='y', padx=(0,3), pady=3)
        self.tbl_consultas.pack(expand=True, fill="both", padx=(6,0), pady=(0,6))


    def set_appttotal(self, total):
        self.total_1.config(text="Consultas ({})".format(total))


    def set_appttotal2(self, total):
        self.total_2.config(text="Matriculas ({})".format(total))
