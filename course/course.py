import tkinter as tk
from tkinter import ttk

from models import Course 
from course.courseui import CourseUi
from course.courseedit import CCourseEdit
from database import Database


class CCourse:
    def __init__(self):
        super().__init__()
       
        self.ui = CourseUi()
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
        disciplinas = []
        count = 0
        if status_term == '0':
            disciplinas = self.getAllCourses()
        else:
            disciplinas = self.getCoursesAtivos()

        for row in self.ui.tbl_1.get_children():
                self.ui.tbl_1.delete(row)

        if len(search_term) > 0:
            for d in disciplinas:
                if search_term.lower() in (str(d.id) + d.name.lower()):
                    self.ui.tbl_1.insert('','end',
                                  values=(d.id,d.name,d.abbr,d.status))
                    count += 1
        else:
            for d in disciplinas:
                self.ui.tbl_1.insert('','end',
                                  values=(d.id,d.name,d.abbr,d.status))
                count += 1
        self.ui.set_msgstatus(str(count) + " disciplinas(s)")


    def getAllCourses(self):
        return Course.select().order_by(Course.name.asc())


    def getCoursesAtivos(self):
        return Course.select().where(Course.status=='1').order_by(Course.name.asc())


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
            detail = CCourseEdit(self, data)
            top = detail.ui
            top.bind('<Destroy>', self.on_top_destroy)
        self.ontop = True
