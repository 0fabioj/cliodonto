import tkinter as tk
from tkinter import ttk

from database import Database
import peewee as pw
from models import Student
from graduating.enrolleditui import EnrollEditUi

class CEnrollEdit:
    def __init__(self, parent, data, callback):
        super().__init__()

        self.ui = EnrollEditUi() 
        self.data = data
        self.callback = callback
        self.alunos = []
        
        self.new = False
        if self.data[0] == 0:
            self.new = True
            
        self.newGrad = False
			
        self.ui.btn_save.configure(command=lambda: self.return_row_values())
        self.fill_cb_student()
        
        if self.new == False:
            self.fill_data(data)


    def fill_cb_student(self):
        self.alunos = self.get_all_students()
        self.ui.cb_student.configure(values=[s.name for s in self.alunos])
        self.ui.cb_student.configure(state='readonly')


    def get_all_students(self):
        return Student.select()


    def fill_data(self, data):
        index = 0
        for s in self.alunos:
            if s.id == int(data[1]):
                self.ui.cb_student.current(index)
                break
            index += 1

 
    def return_row_values(self):
        s_index = self.ui.cb_student.current()
        ra = self.alunos[s_index].id
        
        row_value = [ra, self.ui.cb_student.get(),
                     self.ui.var_status.get()]
        self.callback(row_value)
        self.ui.destroy()
