import tkinter as tk
from tkinter import ttk
from datetime import datetime

import peewee as pw
from database import Database
from models import Patient, Appointment
from models import ZipCode, City, Country

from dictionary import *
from messages import CMessages
from patient.search import CSearch
from patient.patienteditui import PatientEditUi

class CPatientEdit:
    def __init__(self, parent, data):
        super().__init__()

        self.ui = PatientEditUi() 
        self.data = data
        
        self.new = False
        if self.data[0] == 0:
            self.new = True

        self.ontop = False

        self.ui.btn_save.configure(command=lambda: self.save_patient())
        self.ui.btn_del.configure(command=lambda: self.delete_patient())
        self.ui.btn_zip.configure(command=lambda: self.on_btn_address_click())
        self.ui.ent_zip.bind("<FocusOut>", self.on_ent_address_focus_out)
        self.ui.ent_zip.bind("<Return>", self.on_ent_address_focus_out)

        if self.new == False:
            self.fill_data(data)
            self.ui.entry_id.configure(state='readonly')
        else:
            self.ui.entry_id.insert(0, self.get_nextid())
            self.ui.entry_id.configure(state='readonly')
            self.ui.btn_del.configure(state='disable')


    def get_nextid(self):
        return Patient.select(pw.fn.IFNULL(pw.fn.MAX(
                              Patient.id) + 1, 1)).scalar()


    def get_appointments(self):
        return Appointment.select(
            Appointment.id, Appointment.apptdate).where(
            Appointment.patient==int(self.ui.entry_id.get()))


    def fill_table(self):
        appointments = self.get_appointments()
        for row in self.ui.tbl_consultas.get_children():
            self.ui.tbl_consultas.delete(row)
        for appt in appointments:
            self.ui.tbl_consultas.insert('','end',
                                 values=(appt.id, appt.apptdate))
        self.ui.set_appttotal(len(appointments))
                                         
                                         
    def fill_data(self, data):
        self.patid = data[0]

        pat = (Patient
                .select()
                .where(Patient.id==data[0])
                .get())

        self.ui.entry_id.insert(0, data[0])
        self.ui.entry_name.insert(0, pat.name)
        self.ui.combo_gender.current(pat.gender)
        self.ui.entry_rg.insert(0, pat.rg)
        self.ui.entry_cpf.insert(0, pat.cpf)
        self.ui.date_birth.set_date(pat.birthdate)
        self.ui.combo_status.current(int(pat.maritalstatus))
        self.ui.entry_occupation.insert(0, pat.occupation)
        self.ui.entry_email.insert(0, pat.email)
        self.ui.entry_phone1.insert(0, pat.phone)
        self.ui.entry_phone2.insert(0, pat.phone2)
        self.ui.ent_zip.insert(0, pat.address)
        if pat.address:
            address_ok = self.fill_address(pat.address)
        self.ui.entry_number.insert(0, pat.addressnumber)
        self.ui.entry_complement.insert(0, pat.addresscomplement)
        self.fill_table()


    def prepare_patient(self):
        return {'id':int(self.ui.entry_id.get()),
		        'name':self.ui.entry_name.get(),
		        'gender':sexos.index(self.ui.combo_gender.get()),
		        'rg':self.ui.entry_rg.get(),
		        'cpf':self.ui.entry_cpf.get(),
		        'birthdate':self.ui.date_birth.get_date(),
		        'maritalstatus':estados_civis.index(self.ui.combo_status.get()),
		        'occupation':self.ui.entry_occupation.get(),
		        'email':self.ui.entry_email.get(),
		        'phone':self.ui.entry_phone1.get(),
		        'phone2':self.ui.entry_phone2.get(),
		        'address':self.ui.ent_address.get(),
		        'addressnumber':self.ui.entry_number.get(),
		        'addresscomplement':self.ui.entry_complement.get()}
        

    def get_all_address(self):
        return ZipCode.select()


    def fill_address(self, zipcode):
        str_address = ''
        str_city = ''
        res = False
        address = ZipCode.select().where(ZipCode.id==zipcode).get()
        if address:
            res = True
            str_address = address.address
            str_city = "{}/{} - {}".format(address.city.name,
                                           address.city.abbr,
                                           address.city.country.name)

        self.ui.ent_address.configure(state='normal')
        self.ui.ent_city.configure(state='normal')
        self.ui.ent_address.delete(0, 'end')
        self.ui.ent_city.delete(0, 'end')
        self.ui.ent_address.insert(0, str_address)
        self.ui.ent_city.insert(0, str_city)
        self.ui.ent_address.configure(state='readonly')
        self.ui.ent_city.configure(state='readonly')
        return res


    def on_ent_address_focus_out(self, key):
        id_ = self.ui.ent_zip.get()
        if id_:
            address_ok = self.fill_address(id_)
            if not address_ok:
                self.ui.ent_zip.delete(0, 'end')


    # TOP WINDOW
    def setflag(self):
        self.ontop = False


    def on_top_destroy(self, event):
        if event.widget == event.widget.winfo_toplevel():
            self.setflag()


    def show_search(self, search):
        if not self.ontop:
            top = search.ui
            top.bind('<Destroy>', self.on_top_destroy)
        self.ontop = True


    # SEARCH ON CLICK
    def callback_address(self, item):
        self.ui.ent_zip.delete(0, 'end')
        self.ui.ent_zip.insert(0, item[0])
        self.fill_address(item[0])


    def on_btn_address_click(self):
        search = CSearch(self, self.get_all_address(), self.callback_address)
        self.show_search(search)


    def save_patient_db(self, data):
        try:
            Database().db.connect()
            if self.new == True:
                rows = Patient.create(**data)
            else:
                query = Patient.update(**data).where(
                           Patient.id==data['id'])
                query.execute()
            Database().db.close()
        except pw.OperationalError as ex:
            print(ex.args)
            CMessages().showerror_database(ex.args)


    def save_patient(self):
        data = self.prepare_patient()
        self.save_patient_db(data)
        self.ui.destroy()


    def delete_patient_db(self):
        try:
            Database().db.connect()
            p = Patient.get(Patient.id==self.ui.entry_id.get())
            p.delete_instance()
            Database().db.close()
        except pw.IntegrityError as ex:
            CMessages().showerror_database(ex.args)


    def delete_patient(self):
        res = CMessages().showquestion_del(
            "Deseja excluir paciente?"
        )
        if res:
            self.delete_patient_db()
            self.ui.destroy()
