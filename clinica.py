import tkinter as tk
from tkinter import ttk
import locale
from style import *
from settings import Settings
from about import CAbout

from patient.patient import CPatient
from student.student import CStudent
from teacher.teacher import CTeachers
from course.course import CCourse
from txtype.txtype import CTxType
from appt.appt import CAppt
from graduating.grad import CGraduating

class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
        self.title("Clinica de Odontologia")
        self.geometry("1080x600+80+80")
        self.minsize(1080,600)
        self.style = CStyle()
        self.configure(background=background_color)
        
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Configurações", command=self.open_settings)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=quit)
        menubar.add_cascade(label="Arquivo", menu=filemenu)

        tablemenu = tk.Menu(menubar, tearoff=0)
        tablemenu.add_command(label="Paciente",
                              command=self.open_list_paciente)
        tablemenu.add_command(label="Aluno",
                              command=self.open_list_aluno)
        tablemenu.add_command(label="Professor",
                              command=self.open_list_professor)
        tablemenu.add_command(label="Disciplina",
                              command=self.open_list_disciplina)
        tablemenu.add_command(label="Tipo de tratamento",
                              command=self.open_list_tratamento)
        tablemenu.add_command(label="Turma",
                              command=self.open_list_turma)
        menubar.add_cascade(label="Tabela", menu=tablemenu)

        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Sobre", command=self.open_about)
        menubar.add_cascade(label="Ajuda", menu=helpmenu)
        
        tk.Tk.config(self, menu=menubar)
        
        # Logo
        logo_img = tk.PhotoImage(file = "img/logo.png")
        lbl_logo = ttk.Label(self, image=logo_img)
        #lbl_logo.grid(row = 0, column = 0, sticky = 'w')
        lbl_logo.pack(fill='x')
        lbl_logo.img_ref = logo_img
        
        # Principal
        center = CAppt()

        # Rodapé
        tail = ttk.Frame(self)
        ttk.Label(tail, text='Busque conhecimento').pack(anchor='nw')
        tail.pack(side='bottom', fill='x')

        self.mainloop()


    def open_list_paciente(self):
        list_paciente = CPatient()


    def open_list_aluno(self):
        list_aluno = CStudent()


    def open_list_professor(self):
        list_professor = CTeachers()


    def open_list_disciplina(self):
        list_disciplina = CCourse()


    def open_list_tratamento(self):
        list_tratamento = CTxType()


    def open_list_turma(self):
        list_turma = CGraduating()


    def open_about(self):
        about = CAbout()


    def open_settings(self):
        settings = Settings(self) 


if __name__ == "__main__":
    Main()
