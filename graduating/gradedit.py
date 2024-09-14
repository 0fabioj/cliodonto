import tkinter as tk
from tkinter import ttk

import peewee as pw
from database import Database
from models import Graduating, Enrolled

from dictionary import *
from messages import CMessages
from graduating.gradeditui import GraduatingEditUi
from graduating.enrolledit import CEnrollEdit

class CGraduatingEdit:
    def __init__(self, parent, data):
        super().__init__()

        self.ui = GraduatingEditUi() 
        self.data = data
        self.gradid = 0
        self.ontop = False
        
        self.new = False
        if self.data[0] == 0:
            self.new = True
			
        self.ui.btn_save.configure(command=lambda: self.save_grad())
        self.ui.btn_del.configure(command=lambda: self.delete_grad())

        self.ui.btn_gradadd.configure(command=lambda: self.on_btn_gradadd_click())
        self.ui.tbl_2.bind("<Insert>", self.on_tbl_2_insert_key_pressed)
        self.ui.btn_graddel.configure(command=lambda: self.on_btn_graddel_click())
        self.ui.tbl_2.bind("<Delete>", self.on_tbl_2_del_key_pressed)

        if self.new == False:
            self.fill_data(data)
            self.ui.ent_id.configure(state='readonly')
        else:
            self.ui.ent_id.insert(0, self.get_nextid())
            self.ui.ent_id.configure(state='readonly')
            self.ui.btn_del.configure(state='disable')


    def get_nextid(self):
        return Graduating.select(pw.fn.IFNULL(pw.fn.MAX(
                              Graduating.id) + 1, 1)).scalar()


    def get_gradid(self):
        return int(self.gradid) 

                                         
    def fill_data(self, data):
        self.gradid = data[0]
        self.ui.ent_id.insert(0, data[0])
        self.ui.ent_name.insert(0, data[1])
        self.ui.ent_semester.insert(0, data[2])
        self.ui.ent_year.insert(0, data[3])
        self.fill_enroll(self.get_gradid())


    def add_row_enroll(self, rowvalues):
        self.ui.tbl_2.insert('','end',values=(rowvalues))


    def get_enroll(self, gradid):
        return Enrolled.select().where(
            Enrolled.graduating==gradid)


    def fill_enroll(self, gradid):
        alunos = self.get_enroll(gradid)
        #'id':int("{}{}{}".format(self.get_apptid(),data[2],data[0])),
        for row in self.ui.tbl_2.get_children():
            self.ui.tbl_2.delete(row)
        for a in alunos:
            self.ui.tbl_2.insert('','end',
                                 values=(a.student,
                                         a.student.name,
                                         a.status))
        self.ui.set_appttotal2(len(alunos))


    def prepare_grad(self):
        return {'id':int(self.ui.ent_id.get()),
		        'name':self.ui.ent_name.get(),
		        'semester':self.ui.ent_semester.get(),
		        'year':self.ui.ent_year.get()}


    def save_grad_db(self, data):
        try:
            Database().db.connect()
            if self.new == True:
                rows = Graduating.create(**data)
            else:
                query = Graduating.update(**data).where(
                           Graduating.id==data['id'])
                query.execute()
            Database().db.close()
        except pw.OperationalError as ex:
            print(ex.args)
            CMessages().showerror_database(ex.args)


    def save_grad(self):
        data = self.prepare_grad()
        self.save_grad_db(data)
        self.save_enroll_db()
        self.ui.destroy()


    def delete_grad_db(self):
        try:
            Database().db.connect()
            p = Graduating.get(Graduating.id==self.ui.ent_id.get())
            p.delete_instance()
            Database().db.close()
        except pw.IntegrityError as ex:
            CMessages().showerror_database(ex.args)


    def delete_grad(self):
        res = CMessages().showquestion_del(
            "Deseja excluir turma?"
        )
        if res:
            self.delete_enroll_db(self.get_gradid())
            self.delete_grad_db()
            self.ui.destroy()


    # Alunos
    def setflag(self):
        self.ontop = False


    def on_top_destroy(self, event):
        if event.widget == event.widget.winfo_toplevel():
            self.setflag()


    def on_tb_2_click(self, event):
        selectedItem = self.ui.tbl_2.selection()[0]
        item = self.ui.tbl_2.focus()
        data = self.ui.tbl_2.item(item, "values")
        self.top_enroll(data)


    def on_btn_gradadd_click(self):
        data = [0]
        self.top_enroll(data)


    def on_tbl_2_insert_key_pressed(self, key):
        self.on_btn_gradadd_click()


    def on_btn_graddel_click(self):
        selectedItem = self.ui.tbl_2.selection()[0]
        row = self.ui.tbl_2.focus()
        self.ui.tbl_2.delete(row)


    def on_tbl_2_del_key_pressed(self, key):
        self.on_btn_graddel_click()


    def top_enroll(self, data):
        if not self.ontop:
            enroll = CEnrollEdit(self, data, self.add_row_enroll)
            top = enroll.ui
            top.bind('<Destroy>', self.on_top_destroy)
        self.ontop = True


    def prepare_enroll(self, data):
        return {'student':data[0],
		        'graduating':self.get_gradid(),
		        'status':data[2]}


    def save_enroll_db(self):
        self.delete_enroll_db(self.get_gradid())
        try:
            Database().db.connect()
            for row in self.ui.tbl_2.get_children():
                data = self.ui.tbl_2.item(row, "values")
                sttm = self.prepare_enroll(data)
                rows = Enrolled.create(**sttm)
            Database().db.close()
        except pw.OperationalError as ex:
            CMessages().showerror_database(ex.args)


    def delete_enroll_db(self, gradid):
        try:
            Database().db.connect()
            nrows = (Enrolled
                     .delete()
                     .where(Enrolled.graduating==gradid)
                     .execute())        
            Database().db.close()
        except pw.OperationalError:
            print("Não foi possível realizar a operação.")
