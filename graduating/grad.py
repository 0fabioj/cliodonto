import tkinter as tk
from tkinter import ttk

from models import Graduating, Enrolled
from graduating.gradui import GraduatingUi
from graduating.gradedit import CGraduatingEdit
from database import Database
from peewee import *


class CGraduating:
    def __init__(self):
        super().__init__()
       
        self.ui = GraduatingUi()
        self.ontop = False
        
        self.ui.search_var.trace("w", self.refresh_list)
        self.ui.filter_status.configure(command=self.refresh_list)
        self.ui.btn_add.configure(command=lambda: self.new_entry())
        self.ui.tbl_1.bind("<ButtonRelease-1>", 
                                          lambda event: self.show_detail(event))
        self.refresh_list()
    

    def refresh_list(self, *args):
        search_term = self.ui.search_var.get()
        turmas = []
        count = 0
        turmas = self.getAllGraduating()

        for row in self.ui.tbl_1.get_children():
                self.ui.tbl_1.delete(row)

        if len(search_term) > 0:
            for t in turmas:
                if search_term.lower() in (str(t.id) + t.name.lower()):
                    self.ui.tbl_1.insert('','end',
                                  values=(t.id,t.name,t.semester,t.year,
                                          self.getCountEnrolled(t.id)))
                    count += 1
        else:
            for t in turmas:
                self.ui.tbl_1.insert('','end',
                                  values=(t.id,t.name,t.semester,t.year,
                                          self.getCountEnrolled(t.id)))
                count += 1
        self.ui.set_msgstatus(str(count) + " Turma(s)")


    def getAllGraduating(self):
        return Graduating.select().order_by(Graduating.name.asc())


    def getCountEnrolled(self, gradid):
        #return Enrolled.select().count()#.where(Enrolled.graduating == gradid)
        #return Enrolled.select(fn.Count(Enrolled.graduating).alias('count')).group_by(Enrolled.graduating)
        return Enrolled.select(fn.Count(Enrolled.graduating)).where(Enrolled.graduating == gradid).scalar()


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
            detail = CGraduatingEdit(self, data)
            top = detail.ui
            top.bind('<Destroy>', self.on_top_destroy)
        self.ontop = True
