import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry

from style import *
from dictionary import *

class PatientEditUi(tk.Toplevel):
    def __init__(self):
        super().__init__()
			
        self.title("Detalhes")
        self.geometry("758x484")
        self.minsize(758,484)
        self.maxsize(758,484)
        
        self.style = CStyle()
        self.configure(background=background_color)
       
        ttk.Label(
            self, text=' Detalhe do Paciente', style='Title.TLabel'
        ).pack(side='top', fill='x')

        toolbar = ttk.Frame(self, style="Toolbar.TFrame")
        toolbar.pack(side='top', fill="x")
        
        save_img = tk.PhotoImage(file = "img/save.png")
        del_img = tk.PhotoImage(file = "img/delete.png")
        close_img = tk.PhotoImage(file = "img/close.png")
        search_img = tk.PhotoImage(file = "img/search.png")
        
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
        ttk.Label(row_0, text='Id', width=14).grid(row=0, column=0)
        self.entry_id = ttk.Entry(row_0, width=12)
        self.entry_id.grid(row=0, column=1)
        row_0.grid(row=0, column=0)
        
        row_1 = ttk.Frame(profile)
        ttk.Label(row_1, text='Nome', width=14).grid(row=0, column=0)
        self.entry_name = ttk.Entry(row_1, width=50)
        self.entry_name.grid(row=0, column=1)
        row_1.grid(row=1, column=0)
        
        for child in profile.winfo_children():
            child.grid_configure(sticky='w', padx=6, pady=2)

        content = ttk.Frame(self, style='Transparent.TFrame')
        content.pack(anchor='nw')
        
        complement = ttk.Frame(content, relief='groove')
        complement.grid(row=0, column=0, rowspan=2, sticky='nw',
                        padx=(3,0), pady=(3,0))

        row_2 = ttk.Frame(complement)
        ttk.Label(row_2, text='Dt. Nascimento', width=14).grid(row=0, column=0)
        self.date_birth = DateEntry(row_2, locale='pt_BR', width=10)
        self.date_birth.grid(row=0, column=1)
        row_2.grid(row=0, column=0)

        row_3 = ttk.Frame(complement)
        ttk.Label(row_3, text='Sexo', width=14).grid(row=0, column=0)
        self.combo_gender = ttk.Combobox(row_3, values=sexos, width=10)
        self.combo_gender.current(0)
        self.combo_gender.grid(row=0, column=1)
        row_3.grid(row=1, column=0)
        
        row_4 = ttk.Frame(complement)
        ttk.Label(row_4, text='RG', width=14).grid(row=0, column=0)
        self.entry_rg = ttk.Entry(row_4, width=16)
        self.entry_rg.grid(row=0, column=1)
        row_4.grid(row=2, column=0)
        
        row_5 = ttk.Frame(complement)
        ttk.Label(row_5, text='CPF', width=14).grid(row=0, column=0)
        self.entry_cpf = ttk.Entry(row_5, width=16)
        self.entry_cpf.grid(row=0, column=1)
        row_5.grid(row=3, column=0)
        
        row_6 = ttk.Frame(complement)
        ttk.Label(row_6, text='Estado Civil', width=14).grid(row=0, column=0)
        self.combo_status = ttk.Combobox(row_6, values=estados_civis, width=8)
        self.combo_status.current(0)
        self.combo_status.grid(row=0, column=1)
        row_6.grid(row=4, column=0)
        
        row_7 = ttk.Frame(complement)
        ttk.Label(row_7, text='Ocupação', width=14).grid(row=0, column=0)
        self.entry_occupation = ttk.Entry(row_7, width=32)
        self.entry_occupation.grid(row=0, column=1)
        row_7.grid(row=5, column=0)
        
        row_8 = ttk.Frame(complement)
        ttk.Label(row_8, text='Email', width=14).grid(row=0, column=0)
        self.entry_email = ttk.Entry(row_8, width=32)
        self.entry_email.grid(row=0, column=1)
        row_8.grid(row=6, column=0)
        
        row_9 = ttk.Frame(complement)
        ttk.Label(row_9, text='Telefone 1', width=14).grid(row=0, column=0)
        self.entry_phone1 = ttk.Entry(row_9, width=16)
        self.entry_phone1.grid(row=0, column=1)
        row_9.grid(row=7, column=0)
        
        row_10 = ttk.Frame(complement)
        ttk.Label(row_10, text='Telefone 2', width=14).grid(row=0, column=0)
        self.entry_phone2 = ttk.Entry(row_10, width=16)
        self.entry_phone2.grid(row=0, column=1)
        row_10.grid(row=8, column=0)
        
        row_11 = ttk.Frame(complement)
        ttk.Label(row_11, text='CEP', width=14).grid(row=0, column=0)
        self.btn_zip = ttk.Button(row_11, padding=(3,3,2,2),
                                      image=search_img)
        self.btn_zip.img_ref = search_img
        self.btn_zip.grid(row=0, column=1)
        self.ent_zip = ttk.Entry(row_11, width=9)
        self.ent_zip.grid(row=0, column=2, padx=3)
        row_11.grid(row=9, column=0)
        
        row_12 = ttk.Frame(complement)
        ttk.Label(row_12, text='Endereço', width=14).grid(row=0, column=0)
        self.ent_address = ttk.Entry(row_12, width=42)
        self.ent_address.grid(row=0, column=1)
        row_12.grid(row=10, column=0)
        
        row_13 = ttk.Frame(complement)
        ttk.Label(row_13, text='Número', width=14).grid(row=0, column=0)
        self.entry_number = ttk.Entry(row_13, width=6)
        self.entry_number.grid(row=0, column=1)
        row_13.grid(row=11, column=0)
        
        row_14 = ttk.Frame(complement)
        ttk.Label(row_14, text='Complemento', width=14).grid(row=0, column=0)
        self.entry_complement = ttk.Entry(row_14, width=32)
        self.entry_complement.grid(row=0, column=1)
        row_14.grid(row=12, column=0)
        
        row_15 = ttk.Frame(complement)
        ttk.Label(row_15, text='Cidade', width=14).grid(row=0, column=0)
        self.ent_city = ttk.Entry(row_15, width=42)
        self.ent_city.grid(row=0, column=1)
        row_15.grid(row=13, column=0)
        
        row_16 = ttk.Frame(complement)
        ttk.Label(row_16, text='Situação', width=14).grid(row=0, column=0)
        self.var_status = tk.IntVar(value=1)
        check_status = ttk.Checkbutton(row_16, text="Ativo",
                                            variable=self.var_status)
        check_status.grid(row=0, column=1)
        row_16.grid(row=14, column=0)
        
        for child in complement.winfo_children():
            child.grid_configure(sticky='w', padx=6, pady=2)
        
        colsdata = ('id','date')
        frame_tree = ttk.Label(content, relief='groove')
        frame_tree.grid(row=0, column=1,
                        padx=(3,0), pady=(3,0))
        self.total_1 = ttk.Label(frame_tree)
        self.total_1.pack(fill=tk.BOTH, padx=6, pady=(6,0))

        self.tbl_consultas = ttk.Treeview(frame_tree, height=6,
                                          show='headings', columns=colsdata)       
        self.tbl_consultas.heading('#1', text='Id', anchor='w')
        self.tbl_consultas.heading('#2', text='Data', anchor='w')        
        self.tbl_consultas.column('#1', minwidth=30, width=50, stretch=False)
        self.tbl_consultas.column('#2', minwidth=100, width=200, stretch=True)       
        vscrlbar = ttk.Scrollbar(frame_tree, orient ="vertical", 
                                   command = self.tbl_consultas.yview)
        self.tbl_consultas.configure(yscrollcommand = vscrlbar.set)
        vscrlbar.pack(side='right', fill='y', padx=(0,3), pady=3)
        self.tbl_consultas.pack(expand=True, fill="both", padx=(6,0), pady=(0,6))

        colsdata2 = ('id','date')
        frame_tree2 = ttk.Label(content, relief='groove')
        frame_tree2.grid(row=1, column=1,
                        padx=(3,0), pady=(3,0))
        self.total_2 = ttk.Label(frame_tree2)
        self.total_2.pack(fill=tk.BOTH, padx=6, pady=(6,0))

        self.tbl_anamnese = ttk.Treeview(frame_tree2, height=6,
                                         show='headings', columns=colsdata2)       
        self.tbl_anamnese.heading('#1', text='Id', anchor='w')
        self.tbl_anamnese.heading('#2', text='Data', anchor='w')        
        self.tbl_anamnese.column('#1', minwidth=30, width=50, stretch=False)
        self.tbl_anamnese.column('#2', minwidth=100, width=200, stretch=True)       
        vscrlbar2 = ttk.Scrollbar(frame_tree2, orient ="vertical", 
                                   command = self.tbl_anamnese.yview)
        self.tbl_anamnese.configure(yscrollcommand = vscrlbar2.set)
        vscrlbar2.pack(side='right', fill='y', padx=(0,3), pady=3)
        self.tbl_anamnese.pack(expand=True, fill="both", padx=(6,0), pady=(0,6))


    def set_appttotal(self, total):
        self.total_1.config(text="Consultas ({})".format(total))


    def set_appttotal2(self, total):
        self.total_2.config(text="Anamneses ({})".format(total))
