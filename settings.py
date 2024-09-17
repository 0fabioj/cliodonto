import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import peewee as pw
from style import *
from database import Database
from models import Patient, Student, Teacher
from models import Appointment, TxType, Course, Treatment
from models import Country, City, ZipCode
from models import Graduating, Enrolled

class Settings(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        
        self.tables = (Student,Teacher,Patient,Appointment,
		          TxType,Course,Treatment)
        
        self.title("Configurações")
        self.geometry("320x290")
        
        self.style = CStyle()
        self.configure(background=surface_color)
        
        save_img = tk.PhotoImage(file = "img/save.png")
        del_img = tk.PhotoImage(file = "img/delete.png")
        close_img = tk.PhotoImage(file = "img/close.png")

        toolbar = ttk.Frame(self, style="Toolbar.TFrame")
        toolbar.pack(side='top', fill="x")

        btn_close = ttk.Button(toolbar, text="Fechar", 
                               image=close_img, compound="left",
                               command=lambda: self.destroy())
        btn_close.img_ref = close_img
        btn_close.grid(row=0, column=0, padx=(2,0), pady=2)
       
        frame = ttk.Frame(self, relief='groove')
        frame.pack(anchor='nw', padx=(3,0), pady=(3,0))

        ttk.Label(frame, text="Drop Tables").grid(row=0, column=0)
        btn_drop_tables = ttk.Button(frame, padding=1, image=del_img,
                              command=lambda: self.drop_tables())
        btn_drop_tables.img_ref = del_img
        btn_drop_tables.grid(row=0, column=1)
        
        ttk.Label(frame, text="Create Tables").grid(row=1, column=0)
        btn_create_tables = ttk.Button(frame, padding=1, image=save_img,
                              command=lambda: self.create_tables())
        btn_create_tables.img_ref = save_img
        btn_create_tables.grid(row=1, column=1)
        
        ttk.Label(frame, text="Create Zip Codes").grid(row=2, column=0)
        btn_create_cep = ttk.Button(frame, padding=1, image=save_img,
                              command=lambda: self.create_ceps())
        btn_create_cep.img_ref = save_img
        btn_create_cep.grid(row=2, column=1)

        ttk.Label(frame, text="Create Turma").grid(row=3, column=0)
        btn_create_grad = ttk.Button(frame, padding=1, image=save_img,
                              command=lambda: self.create_grad())
        btn_create_grad.img_ref = save_img
        btn_create_grad.grid(row=3, column=1)


    def drop_tables(self):
        try:
            Database().db.connect()
            Database().db.drop_tables(self.tables)
            Database().db.close()
        except pw.IntegrityError:
            print("Tabelas não existem")
        except pw.OperationalError:
            print("Não foi possível realizar a operação.")


    def create_tables(self):
        try:
            Database().db.connect()
            Database().db.create_tables(self.tables)
            Database().db.close()
        except pw.IntegrityError:
            print("Tabelas não existem")
        except pw.OperationalError:
            print("Não foi possível realizar a operação.")


    def create_ceps(self):
        tables1 = (Country, City, ZipCode)
        print(tables1)
        try:
            Database().db.connect()
            Database().db.create_tables(tables1)
            Database().db.close()
        except pw.IntegrityError:
            print("Tabelas não existem")
        except pw.OperationalError:
            print("Não foi possível realizar a operação.")


    def create_grad(self):
        tables2 = (Graduating, Enrolled)
        print(tables2)
        try:
            Database().db.connect()
            Database().db.drop_tables(tables2)
            Database().db.create_tables(tables2)
            Database().db.close()
        except pw.IntegrityError:
            print("Tabelas não existem")
        except pw.OperationalError:
            print("Não foi possível realizar a operação.")
