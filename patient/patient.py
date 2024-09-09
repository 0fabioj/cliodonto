import tkinter as tk
from tkinter import ttk

from models import Patient 
from patient.patientui import PatientUi
from patient.patientedit import CPatientEdit
from database import Database
from dictionary import *

class CPatient:
    def __init__(self):
        super().__init__()
       
        self.ui = PatientUi()
        self.ontop = False
        
        self.ui.search_var.trace("w", self.refresh_list)
        self.ui.btn_add.configure(command=lambda: self.new_entry())
        self.ui.tbl_1.bind("<ButtonRelease-1>", 
                                          lambda event: self.show_detail(event))
        self.refresh_list()
    

    def refresh_list(self, *args):
        search_term = self.ui.search_var.get()
        pacientes = self.getAllPatients()
        count = 0

        for row in self.ui.tbl_1.get_children():
                self.ui.tbl_1.delete(row)

        if len(search_term) > 0:
            for p in pacientes:
                if search_term.lower() in (str(p.id) + p.name.lower()):
                    self.ui.tbl_1.insert('','end',
                                  values=(p.id,p.name,
                                          genders[int(p.gender)][0],
                                          p.rg,p.cpf,p.birthdate,
                                          p.maritalstatus,p.occupation,
                                          p.email,p.phone,p.phone2,
                                          p.address,p.addressnumber,
                                          p.addresscomplement))
                    count += 1
        else:
            for p in pacientes:
                self.ui.tbl_1.insert('','end',
                                  values=(p.id,p.name,
                                          genders[int(p.gender)][0],
                                          p.rg,p.cpf,p.birthdate,
                                          p.maritalstatus,p.occupation,
                                          p.email,p.phone,p.phone2,
                                          p.address,p.addressnumber,
                                          p.addresscomplement))
                count += 1
        self.ui.set_msgstatus(str(count) + " paciente(s)")


    def getAllPatients(self):
        return Patient.select().order_by(Patient.name.asc())


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
            detail = CPatientEdit(self, data)
            top = detail.ui
            top.bind('<Destroy>', self.on_top_destroy)
        self.ontop = True
