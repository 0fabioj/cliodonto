import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from style import *

class ApptEditUi(tk.Toplevel):
    def __init__(self):
        super().__init__()
			
        self.title("Consulta")
        self.geometry("800x640")
        self.minsize(800,640)
        self.maxsize(800,640)
        
        self.style = CStyle()
        self.configure(background=background_color)
       
        head = ttk.Frame(self)
        head.pack(side='top', fill='x')
        
        frame_l = ttk.Frame(head)
        self.lbl_title = ttk.Label(frame_l, style='Title.TLabel')
        self.lbl_title.pack(fill='both', expand=True)
        frame_l.pack(side='left', fill='both', expand=True)
        
        frame_r = ttk.Frame(head)
        ttk.Label(frame_r, text='Situação').grid(row=0, column=0)
        self.box_status = ttk.Combobox(frame_r, width=12)
        self.box_status.grid(row=0, column=1)
        self.lbl_canceled = ttk.Label(frame_r, width=10)
        self.lbl_canceled.grid(row=0, column=2)
        self.date_canceled = DateEntry(frame_r, locale='pt_BR', width='10')
        self.date_canceled.grid(row=0, column=3)
        frame_r.pack(side='right')
        
        
        toolbar = ttk.Frame(self, style="Toolbar.TFrame")
        toolbar.pack(side='top', fill="x")
        
        save_img = tk.PhotoImage(file = "img/save.png")
        del_img = tk.PhotoImage(file = "img/delete.png")
        close_img = tk.PhotoImage(file = "img/close.png")
        search_img = tk.PhotoImage(file = "img/search.png")
        
        self.btn_save = ttk.Button(toolbar, padding=(3,3,2,2), compound='left',
                               text='Salvar', image=save_img)
        self.btn_save.img_ref = save_img
        self.btn_save.grid(row=0, column=0, padx=(6,0), pady=6)
        self.btn_del = ttk.Button(toolbar, padding=(3,3,2,2), compound='left',
                               text='Excluir', image=del_img)
        self.btn_del.img_ref = del_img
        self.btn_del.grid(row=0, column=1, padx=(3,0), pady=6)
        btn_close = ttk.Button(toolbar, padding=(3,3,2,2), compound='left',
                               text='Cancelar', image=close_img,
                               command=lambda: self.destroy())
        btn_close.img_ref = close_img
        btn_close.grid(row=0, column=2, padx=(3,0), pady=6)
        
        ttk.Separator(self, orient='horizontal').pack(fill='x')

        center = ttk.Frame(self)
        center.pack(anchor='nw')
        
        # FRAME AGENDAMENTO
        profile = ttk.Frame(center, relief='groove')
        profile.grid(row=0, column=0)
        
        row_0 = ttk.Frame(profile)
        ttk.Label(row_0, text='Paciente', width=9).grid(row=0, column=0)
        self.btn_patient = ttk.Button(row_0, padding=(3,3,2,2),
                                      image=search_img)
        self.btn_patient.img_ref = search_img
        self.btn_patient.grid(row=0, column=1)
        self.ent_patient = ttk.Entry(row_0, width=9)
        self.ent_patient.grid(row=0, column=2, padx=3)
        self.lbl_patient = ttk.Label(row_0, width=35,
                                     style='Patient.TLabel')
        self.lbl_patient.grid(row=0, column=3)
        row_0.grid(row=0, column=0, columnspan=2)
        
        row_1 = ttk.Frame(profile)
        ttk.Label(row_1, text='Serviço', width=9).grid(row=0, column=0)
        self.cb_type = ttk.Combobox(row_1, width=20)
        self.cb_type.grid(row=0, column=1, columnspan=2)
        row_1.grid(row=1, column=0, columnspan=2)
        
        row_2 = ttk.Frame(profile)
        ttk.Label(row_2, text='Data', width=9).grid(row=0, column=0)
        self.date_appt = DateEntry(row_2, locale='pt_BR', width='10')
        self.date_appt.grid(row=0, column=1)
        row_2.grid(row=2, column=0, columnspan=2)
        
        row_3 = ttk.Frame(profile)
        ttk.Label(row_3, text='Horário', width=9).grid(row=0, column=0)
        self.hour_appt = ttk.Spinbox(row_3, from_=8, to=22, width=2)
        self.hour_appt.grid(row=0, column=1)
        self.min_appt = ttk.Spinbox(row_3, from_=0, to=55, increment=5, width=2)
        self.min_appt.grid(row=0, column=2)
        ttk.Label(row_3, text='(HH:MM)').grid(row=0, column=3)
        row_3.grid(row=3, column=0, columnspan=2)
        
        row_4 = ttk.Frame(profile)
        ttk.Label(row_4, text='Duração', width=9).grid(row=0, column=0)
        self.lenh_appt = ttk.Spinbox(row_4, from_=0, to=22, width=2)
        self.lenh_appt.grid(row=0, column=1)
        self.lenm_appt = ttk.Spinbox(row_4, from_=0, to=55, increment=5, width=2)
        self.lenm_appt.grid(row=0, column=2)
        ttk.Label(row_4, text='(HH:MM)').grid(row=0, column=3)
        row_4.grid(row=4, column=0, columnspan=2)
        
        row_5 = ttk.Frame(profile)
        ttk.Label(row_5, text='Aluno', width=9).grid(row=0, column=0)
        self.btn_student = ttk.Button(row_5, padding=(3,3,2,2),
                                      image=search_img)
        self.btn_student.img_ref = search_img
        self.btn_student.grid(row=0, column=1)
        self.ent_student = ttk.Entry(row_5, width=8)
        self.ent_student.grid(row=0, column=2, padx=3)
        self.lbl_student = ttk.Label(row_5)
        self.lbl_student.grid(row=0, column=3)
        row_5.grid(row=5, column=0, columnspan=2)
        
        row_6 = ttk.Frame(profile)
        ttk.Label(row_6, text='Assistente', width=9).grid(row=0, column=0)
        self.btn_assistant = ttk.Button(row_6, padding=(3,3,2,2),
                                        image=search_img)
        self.btn_assistant.img_ref = search_img
        self.btn_assistant.grid(row=0, column=1)
        self.ent_assistant = ttk.Entry(row_6, width=8)
        self.ent_assistant.grid(row=0, column=2, padx=3)
        self.lbl_assistant = ttk.Label(row_6)
        self.lbl_assistant.grid(row=0, column=3)
        row_6.grid(row=6, column=0, columnspan=2)
        
        row_7 = ttk.Frame(profile)
        ttk.Label(row_7, text='Professor', width=9).grid(row=0, column=0)
        self.btn_teacher = ttk.Button(row_7, padding=(3,3,2,2),
                                      image=search_img)
        self.btn_teacher.img_ref = search_img
        self.btn_teacher.grid(row=0, column=1)
        self.ent_teacher = ttk.Entry(row_7, width=8)
        self.ent_teacher.grid(row=0, column=2, padx=3)
        self.lbl_teacher = ttk.Label(row_7)
        self.lbl_teacher.grid(row=0, column=3)
        row_7.grid(row=7, column=0, columnspan=2)

        for child in profile.winfo_children():
            child.grid_configure(sticky='nw', padx=6, pady=2)
        
        # FRAME PROCEDIMENTO
        frame_tx = ttk.Frame(center, relief='groove')
        frame_tx.grid(row=1, column=0)
        
        frame_tx_header = ttk.Frame(frame_tx)
        frame_tx_header.pack(fill=tk.BOTH, padx=6, pady=(6,0))
        ttk.Label(frame_tx_header,
                  text='Procedimentos').pack(side='left')
        add_img = tk.PhotoImage(file="img/add.png")        
        self.btn_procadd = ttk.Button(frame_tx_header, image=add_img,
                                      padding=(3,3,1,1))
        self.btn_procadd.img_ref = add_img
        self.btn_procadd.pack(side='right')
        self.btn_procdel = ttk.Button(frame_tx_header, image=del_img,
                                      padding=(3,3,1,1))
        self.btn_procdel.img_ref = del_img
        self.btn_procdel.pack(side='right')            
                                             
        colsdata = ('txid','tx','catid','cat','obs')
        self.tbl_1 = ttk.Treeview(frame_tx, show='headings',
                                  columns=colsdata, height=8)       
        self.tbl_1.heading('#1', text='Id', anchor='w')
        self.tbl_1.heading('#2', text='Procedimento', anchor='w')
        self.tbl_1.heading('#3', text='Id', anchor='w')
        self.tbl_1.heading('#4', text='Disciplina', anchor='w')
        self.tbl_1.heading('#5', text='Observação', anchor='w')
        self.tbl_1.column('#1', width=0, stretch=False)
        self.tbl_1.column('#2', width=120, stretch=False)
        self.tbl_1.column('#3', width=0, stretch=False)
        self.tbl_1.column('#4', width=120, stretch=False)
        self.tbl_1.column('#5', width=208, stretch=True)
        vscrlbar = ttk.Scrollbar(frame_tx, orient='vertical',
                                 command = self.tbl_1.yview)
        self.tbl_1.configure(yscrollcommand = vscrlbar.set)
        vscrlbar.pack(side='right', fill='y')
        self.tbl_1.pack(expand=True, fill='x', padx=(6,0), pady=(0,6))

        # FRAME CONSULTAS
        frame_appt = ttk.Label(center, relief='groove')
        frame_appt.grid(row=0, column=1)    
        ttk.Label(frame_appt,
                  text='Consultas do paciente').pack(fill=tk.BOTH,
                                                     padx=6, pady=(6,0))
        colsdata_2 = ('date','time','len','status')
        self.tbl_2 = ttk.Treeview(frame_appt, show='headings',
                                  columns=colsdata_2, height=8) 
        self.tbl_2.heading('#1', text='Data', anchor='w')
        self.tbl_2.heading('#2', text='Horário', anchor='w')
        self.tbl_2.heading('#3', text='Duração', anchor='w')
        self.tbl_2.heading('#4', text='Sit.', anchor='w')
        self.tbl_2.column('#1', width=86, stretch=False)
        self.tbl_2.column('#2', width=70, stretch=False)
        self.tbl_2.column('#3', width=70, stretch=False)
        self.tbl_2.column('#4', width=40, stretch=True)
        vscrlbar_2 = ttk.Scrollbar(frame_appt, orient='vertical',
                                   command = self.tbl_2.yview)
        self.tbl_2.configure(yscrollcommand = vscrlbar_2.set)
        vscrlbar_2.pack(side='right', fill='y')
        self.tbl_2.pack(expand=True, fill='x', padx=(6,0), pady=(0,6))
        
        # FRAME ANOTAÇÕES
        frame_note = ttk.Frame(center, relief='groove')
        frame_note.grid(row=1, column=1)
        
        ttk.Label(frame_note,
                  text='Anotações da consulta').pack(fill=tk.BOTH,
                                                     padx=6, pady=(3,0))
        self.tex_note1 = tk.Text(frame_note, height=5, width=39)
        self.tex_note1.configure(font='TkTextFont 9 normal')
        self.tex_note1.pack(padx=6, pady=(0,6))
        ttk.Label(frame_note,
                  text='Anotações do paciente').pack(fill=tk.BOTH,
                                                     padx=6, pady=(3,0))
        self.tex_note2 = tk.Text(frame_note, height=5, width=39)
        self.tex_note2.configure(font='TkTextFont 9 normal')
        self.tex_note2.pack(padx=6, pady=(0,6))
        
        # frame center
        for child in center.winfo_children():
            child.grid_configure(sticky='nw', padx=(6,0), pady=(6,0))

        status_msg = ttk.Label(self, text="Pronto")
        status_msg.pack(side='bottom', fill='x', padx=4)


    def set_title(self, msg):
        msg = " Consulta: {}".format(msg)
        self.lbl_title.config(text=msg)


    def set_lbl_canceled(self, msg):
        msg = " data: {}".format(msg)
        self.lbl_canceled.config(text=msg)
