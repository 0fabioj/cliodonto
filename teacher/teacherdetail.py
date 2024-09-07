import tkinter as tk
from tkinter import ttk

import peewee as pw
from database import Database
from models import Teacher, Appointment

from dictionary import *
from messages import CMessages
from teacher.teacherdetailui import TeacherDetailUi

class CTeacher:
    def __init__(self, parent, data):
        super().__init__()

        self.ui = TeacherDetailUi() 
        self.data = data
        
        self.new = False
        if self.data[0] == 0:
            self.new = True
			
        self.ui.btn_save.configure(command=lambda: self.save_teacher())
        self.ui.btn_del.configure(command=lambda: self.delete_teacher())

        if self.new == False:
            self.fill_data(data)
            self.ui.entry_id.configure(state='readonly')
        else:
            self.ui.entry_id.insert(0, self.get_nextid())
            self.ui.entry_id.configure(state='readonly')
            self.ui.btn_del.configure(state='disable')


    def get_nextid(self):
        return Teacher.select(pw.fn.IFNULL(pw.fn.MAX(
                              Teacher.id) + 1, 1)).scalar()


    def get_appointments(self):
        return Appointment.select(
            Appointment.id, Appointment.apptdate).where(
            Appointment.teacher==int(self.ui.entry_id.get()))


    def fill_table(self):
        appointments = self.get_appointments()
        for row in self.ui.tbl_consultas.get_children():
            self.ui.tbl_consultas.delete(row)
        for appt in appointments:
            self.ui.tbl_consultas.insert('','end',
                                 values=(appt.id, appt.apptdate))
        self.ui.set_appttotal(len(appointments))
                                         
                                         
    def fill_data(self, data):
        self.ui.entry_id.insert(0, data[0])
        self.ui.entry_name.insert(0, data[1])
        self.ui.entry_email.insert(0, data[2])
        self.ui.entry_phone.insert(0, data[3])
        self.ui.entry_cro.insert(0, data[4])
        self.ui.var_status.set(int(data[5]))
        self.fill_table()


    def prepare_teacher(self):
        return {'id':int(self.ui.entry_id.get()),
		         'name':self.ui.entry_name.get(),
		         'email':self.ui.entry_email.get(),
		         'phone':self.ui.entry_phone.get(),
		         'cro':self.ui.entry_cro.get(),
		         'status':self.ui.var_status.get()}
        

    def save_teacher_db(self, data):
        try:
            Database().db.connect()
            if self.new == True:
                rows = Teacher.create(**data)
            else:
                query = Teacher.update(**data).where(
                           Teacher.id==data['id'])
                query.execute()
            Database().db.close()
        except pw.OperationalError as ex:
            print(ex.args)
            CMessages().showerror_database(ex.args)


    def save_teacher(self):
        data = self.prepare_teacher()
        self.save_teacher_db(data)
        self.ui.destroy()


    def delete_teacher_db(self):
        try:
            Database().db.connect()
            p = Teacher.get(Teacher.id==self.ui.entry_id.get())
            p.delete_instance()
            Database().db.close()
        except pw.IntegrityError as ex:
            CMessages().showerror_database(ex.args)


    def delete_teacher(self):
        res = CMessages().showquestion_del(
            "Deseja excluir professor?"
        )
        if res:
            self.delete_teacher_db()
            self.ui.destroy()
