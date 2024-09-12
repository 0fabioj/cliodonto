import tkinter as tk
from tkinter import ttk

import peewee as pw
from database import Database
from models import Course

from dictionary import *
from messages import CMessages
from course.courseeditui import CourseEditUi

class CCourseEdit:
    def __init__(self, parent, data):
        super().__init__()

        self.ui = CourseEditUi() 
        self.data = data
        
        self.new = False
        if self.data[0] == 0:
            self.new = True
			
        self.ui.btn_save.configure(command=lambda: self.save_course())
        self.ui.btn_del.configure(command=lambda: self.delete_course())

        if self.new == False:
            self.fill_data(data)
            self.ui.entry_id.configure(state='readonly')
        else:
            self.ui.entry_id.insert(0, self.get_nextid())
            self.ui.entry_id.configure(state='readonly')
            self.ui.btn_del.configure(state='disable')


    def get_nextid(self):
        return Course.select(pw.fn.IFNULL(pw.fn.MAX(
                              Course.id) + 1, 1)).scalar()
                                         
                                         
    def fill_data(self, data):
        self.ui.entry_id.insert(0, data[0])
        self.ui.entry_name.insert(0, data[1])
        self.ui.entry_abbr.insert(0, data[2])
        self.ui.var_status.set(int(data[3]))


    def prepare_course(self):
        return {'id':int(self.ui.entry_id.get()),
		         'name':self.ui.entry_name.get(),
		         'abbr':self.ui.entry_abbr.get(),
		         'status':self.ui.var_status.get()}
        

    def save_course_db(self, data):
        try:
            Database().db.connect()
            if self.new == True:
                rows = Course.create(**data)
            else:
                query = Course.update(**data).where(
                           Course.id==data['id'])
                query.execute()
            Database().db.close()
        except pw.OperationalError as ex:
            print(ex.args)
            CMessages().showerror_database(ex.args)


    def save_course(self):
        data = self.prepare_course()
        self.save_course_db(data)
        self.ui.destroy()


    def delete_course_db(self):
        try:
            Database().db.connect()
            p = Course.get(Course.id==self.ui.entry_id.get())
            p.delete_instance()
            Database().db.close()
        except pw.IntegrityError as ex:
            CMessages().showerror_database(ex.args)


    def delete_course(self):
        res = CMessages().showquestion_del(
            "Deseja excluir disciplina?"
        )
        if res:
            self.delete_course_db()
            self.ui.destroy()
