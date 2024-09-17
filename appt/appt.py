import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta 
import peewee as pw

from models import Patient, Student, Appointment, Enrolled
from appt.apptui import ApptUi
from database import Database
from appt.apptedit import CApptEdit
from dictionary import *

class CAppt:
    def __init__(self):
        super().__init__()
       
        self.ui = ApptUi()
        self.ui.pack(fill='both', expand=True)
        self.ontop = False

        today = datetime.today()
        self.one_day = timedelta(days=1)
        self.selected_date = today
        self.ui.date_var.set(self.dateformat(self.selected_date))
        self.refresh_book()

        self.ui.btn_today.configure(command=lambda: self.todaybook())
        self.ui.btn_prev.configure(command=lambda: self.prevbook())
        self.ui.btn_next.configure(command=lambda: self.nextbook())
        self.ui.search_var.trace("w", self.refresh_book)
        self.ui.btn_add.configure(command=lambda: self.new_entry())
        self.ui.tbl_1.bind("<ButtonRelease-1>", 
                            lambda event: self.show_detail(event))


    def todaybook(self):
        self.selected_date = datetime.today()
        self.ui.date_var.set(self.dateformat(self.selected_date))
        self.refresh_book()


    def prevbook(self):
        self.selected_date = self.selected_date - self.one_day
        self.ui.date_var.set(self.dateformat(self.selected_date))
        self.refresh_book()


    def nextbook(self):
        self.selected_date = self.selected_date + self.one_day
        self.ui.date_var.set(self.dateformat(self.selected_date))
        self.refresh_book()


    def dateformat(self, date):
        return date.strftime("%A %Y/%m/%d")


    def refresh_book(self, *args):
        search_term = self.ui.search_var.get()
        agenda = self.get_book_per_date(self.selected_date)
        count = 0
        for row in self.ui.tbl_1.get_children():
                self.ui.tbl_1.delete(row)

        if len(search_term) > 0:
            for a in agenda:
                if search_term.lower() in (str(a.patient) + a.patient.name.lower()):
                    self.ui.tbl_1.insert('','end',
                                  values=(a.id,a.apptdate,a.appttime,
                                          a.patient.name,
                                          a.student.name,a.assistant.name,
                                          a.teacher.name,a.status))
                    count += 1
        else:
            for a in agenda:
                self.ui.tbl_1.insert('','end',
                                  values=(a.id,a.apptdate,a.appttime,
                                          a.patient.name,
                                          a.student.name,a.assistant.name,
                                          a.teacher.name,
                                          appt_status[int(a.status)]))
                count += 1


    def get_book_per_date(self, date):
        return (Appointment
                .select()
                #.select(Appointment, Enrolled)
                #.join(Enrolled, on=(Enrolled.student == Appointment.student), attr='enroll')
                .where(Appointment.apptdate==date.strftime("%Y-%m-%d")))


    def get_appt_per_interval(self, date1, date2):
        pass


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
            self.refresh_book()


    def top(self, data):
        if not self.ontop:
            detail = CApptEdit(self, data)
            top = detail.ui
            top.bind('<Destroy>', self.on_top_destroy)
        self.ontop = True
