import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from style import *
from dictionary import *

class GraduatingEditUi(tk.Toplevel):
    def __init__(self):
        super().__init__()
			
        self.title("Detalhes")
        self.geometry("600x480")
        self.minsize(600,480)
        self.maxsize(600,480)
        
        self.style = CStyle()
        self.configure(background=background_color)
       
        ttk.Label(
            self, text=' Detalhe da Turma', style='Title.TLabel'
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
        self.ent_id = ttk.Entry(row_0, width=12)
        self.ent_id.grid(row=0, column=1, padx=3)
        row_0.grid(row=0, column=0)
        
        row_1 = ttk.Frame(profile)
        ttk.Label(row_1, text='Nome', width=8).grid(row=0, column=0)
        self.ent_name = ttk.Entry(row_1, width=40)
        self.ent_name.grid(row=0, column=1, padx=3)
        row_1.grid(row=1, column=0)
        
        row_2 = ttk.Frame(profile)
        ttk.Label(row_2, text='Semestre', width=8).grid(row=0, column=0)
        self.ent_semester = ttk.Entry(row_2, width=8)
        self.ent_semester.grid(row=0, column=1, padx=3)
        row_2.grid(row=2, column=0)
        
        row_3 = ttk.Frame(profile)
        ttk.Label(row_3, text='Ano', width=8).grid(row=0, column=0)
        self.ent_year = ttk.Entry(row_3, width=8)
        self.ent_year.grid(row=0, column=2, padx=3)
        row_3.grid(row=3, column=0)
        
        for child in profile.winfo_children():
            child.grid_configure(sticky='w', padx=6, pady=2)

        # Alunos
        frame_grad = ttk.Frame(self, relief='groove')
        frame_grad.pack(anchor='nw', padx=(3,0), pady=(3,0))
        
        frame_grad_header = ttk.Frame(frame_grad)
        frame_grad_header.pack(fill=tk.BOTH, padx=6, pady=(6,0))
        self.total_2 = ttk.Label(frame_grad_header)
        self.total_2.pack(side='left')
        add_img = tk.PhotoImage(file="img/add.png")        
        self.btn_gradadd = ttk.Button(frame_grad_header, image=add_img,
                                      padding=(3,3,1,1))
        self.btn_gradadd.img_ref = add_img
        self.btn_gradadd.pack(side='right')
        self.btn_graddel = ttk.Button(frame_grad_header, image=del_img,
                                      padding=(3,3,1,1))
        self.btn_graddel.img_ref = del_img
        self.btn_graddel.pack(side='right')            
                                             
        colsdata2 = ('ra','name','status','consultas','anamneses')
        self.tbl_2 = ttk.Treeview(frame_grad, show='headings',
                                  columns=colsdata2, height=16)       
        self.tbl_2.heading('#1', text='RA', anchor='w')
        self.tbl_2.heading('#2', text='Aluno', anchor='w')
        self.tbl_2.heading('#3', text='Situação', anchor='w')
        self.tbl_2.heading('#4', text='Consultas', anchor='w')
        self.tbl_2.heading('#5', text='Anamneses', anchor='w')
        self.tbl_2.column('#1', width=92, stretch=False)
        self.tbl_2.column('#2', width=240, stretch=True)
        self.tbl_2.column('#3', width=80, stretch=False)
        self.tbl_2.column('#4', width=80, stretch=False)
        self.tbl_2.column('#5', width=80, stretch=False)
        vscrlbar2 = ttk.Scrollbar(frame_grad, orient='vertical',
                                 command = self.tbl_2.yview)
        self.tbl_2.configure(yscrollcommand = vscrlbar2.set)
        vscrlbar2.pack(side='right', fill='y')
        self.tbl_2.pack(expand=True, fill='x', padx=(6,0), pady=(0,6))


    def set_appttotal2(self, total):
        self.total_2.config(text="Alunos ({})".format(total))
