import tkinter as tk
from tkinter import ttk

import peewee as pw
from database import Database
from models import Student, Appointment, Enrolled

from dictionary import *
from messages import CMessages
from student.studenteditui import StudentEditUi

class CStudentEdit:
    def __init__(self, parent, data):
        super().__init__()

        self.ui = StudentEditUi() 
        self.data = data
        self.studentid = 0
        
        self.new = False
        if self.data[0] == 0:
            self.new = True
			
        self.ui.btn_save.configure(command=lambda: self.save_student())
        self.ui.btn_del.configure(command=lambda: self.delete_student())

        if self.new == False:
            self.fill_data(data)
            self.ui.entry_ra.configure(state='readonly')
        else:
            self.ui.btn_del.configure(state='disable')


    def get_appointments(self):
        return Appointment.select(
            Appointment.id, Appointment.apptdate).where(
            Appointment.student==int(self.ui.entry_ra.get()))


    def fill_table(self):
        appointments = self.get_appointments()
        for row in self.ui.tbl_consultas.get_children():
            self.ui.tbl_consultas.delete(row)
        for appt in appointments:
            self.ui.tbl_consultas.insert('','end',
                                 values=(appt.id, appt.apptdate))
        self.ui.set_appttotal(len(appointments))
                                         
                                         
    def fill_data(self, data):
        self.studentid = data[0]
        self.ui.entry_ra.insert(0, data[0])
        self.ui.entry_name.insert(0, data[1])
        self.ui.entry_email.insert(0, data[2])
        self.ui.entry_phone.insert(0, data[3])
        self.ui.var_status.set(int(data[4]))
        self.fill_table()
        self.fill_enroll(data[0])


    def add_row_enroll(self, rowvalues):
        self.ui.tbl_2.insert('','end',values=(rowvalues))


    def get_enroll(self, studentid):
        return Enrolled.select().where(
            Enrolled.student==studentid)


    def fill_enroll(self, studentid):
        turmas = self.get_enroll(studentid)
        for row in self.ui.tbl_2.get_children():
            self.ui.tbl_2.delete(row)
        for t in turmas:
            turma_str = "{}SEM {} {}".format(t.graduating.semester,
                                         t.graduating.name,
                                         t.graduating.year)
            self.ui.tbl_2.insert('','end',
                                 values=(t.graduating,
                                         turma_str,
                                         t.status))
        self.ui.set_appttotal2(len(turmas))


    def get_studentid(self):
        return int(self.studentid)


    def prepare_student(self):
        return {'id':int(self.ui.entry_ra.get()),
		        'name':self.ui.entry_name.get(),
		        'email':self.ui.entry_email.get(),
		        'phone':self.ui.entry_phone.get(),
		        'status':self.ui.var_status.get()}
        

    def save_student_db(self, data):
        try:
            Database().db.connect()
            if self.new == True:
                rows = Student.create(**data)
            else:
                query = Student.update(**data).where(
                           Student.id==data['id'])
                query.execute()
            Database().db.close()
        except pw.OperationalError as ex:
            print(ex.args)
            CMessages().showerror_database(ex.args)


    def save_student(self):
        data = self.prepare_student()
        self.save_student_db(data)
        self.ui.destroy()


    def delete_student_db(self):
        try:
            Database().db.connect()
            p = Student.get(Student.id==self.ui.entry_ra.get())
            p.delete_instance()
            Database().db.close()
        except pw.IntegrityError as ex:
            CMessages().showerror_database(ex.args)


    def delete_student(self):
        res = CMessages().showquestion_del(
            "Deseja excluir aluno?"
        )
        if res:
            self.delete_student_db()
            self.ui.destroy()
