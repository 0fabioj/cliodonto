import tkinter as tk
from tkinter import ttk

from models import Teacher 
from teacher.teacherui import TeachersUi
from teacher.teacherdetail import CTeacher
from database import Database


class CTeachers:
    def __init__(self):
        super().__init__()
       
        self.ui = TeachersUi()
        self.ontop = False
        
        self.ui.search_var.trace("w", self.refresh_list)
        self.ui.filter_status.configure(command=self.refresh_list)
        self.ui.btn_add.configure(command=lambda: self.new_entry())
        self.ui.tbl_1.bind("<ButtonRelease-1>", 
                                          lambda event: self.show_detail(event))
        self.refresh_list()
    

    def refresh_list(self, *args):
        search_term = self.ui.search_var.get()
        status_term = self.ui.status_var.get()
        professores = []
        count = 0
        if status_term == '0':
            professores = self.getAllProfessores()
        else:
            professores = self.getProfessoresAtivos()

        for row in self.ui.tbl_1.get_children():
                self.ui.tbl_1.delete(row)

        if len(search_term) > 0:
            for p in professores:
                if search_term.lower() in (str(p.id) + p.name.lower()):
                    self.ui.tbl_1.insert('','end',
                                  values=(p.id,p.name,p.email,p.phone,p.cro,p.status))
                    count += 1
        else:
            for p in professores:
                self.ui.tbl_1.insert('','end',
                                  values=(p.id,p.name,p.email,p.phone,p.cro,p.status))
                count += 1
        self.ui.set_msgstatus(str(count) + " professor(es)")


    def getAllProfessores(self):
        return Teacher.select().order_by(Teacher.name.asc())


    def getProfessoresAtivos(self):
        return Teacher.select().where(Teacher.status=='1').order_by(Teacher.name.asc())


    def show_detail(self, event):
        selectedItem = self.ui.tbl_1.selection()[0]
        item = self.ui.tbl_1.focus()
        data = self.ui.tbl_1.item(item, "values")
        self.top(data)


    def new_entry(self):
        data = [0]
        self.top(data)


    def setflag(self):
        self.ontop = False


    def on_top_destroy(self, event):
        if event.widget == event.widget.winfo_toplevel():
            self.setflag()
            self.refresh_list()


    def top(self, data):
        if not self.ontop:
            detail = CTeacher(self, data)
            top = detail.ui
            top.bind('<Destroy>', self.on_top_destroy)
        self.ontop = True
