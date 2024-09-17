import tkinter as tk
from tkinter import ttk
from datetime import datetime, date

from database import Database
import peewee as pw
from models import Patient, Student, Teacher
from models import Appointment, Treatment, Course, TxType
from appt.appteditui import ApptEditUi
from appt.txedit import CTxEdit
from appt.search import CSearch
from messages import CMessages
from dictionary import *

class CApptEdit:
    def __init__(self, parent, data):
        super().__init__()

        self.ui = ApptEditUi() 
        self.data = data
        self.apptid = 0
        
        self.new = False
        if self.data[0] == 0:
            self.new = True
            self.next_id = (Appointment
                            .select(pw.fn.IFNULL(pw.fn.MAX(Appointment.id) + 1, 1))
                            .scalar())
            self.apptid = self.next_id
            
        self.ontop = False
        
        self.ui.box_status.configure(values=appt_status)
        self.ui.box_status.current(0)
        self.ui.date_canceled.configure(state='disable')
			
        self.ui.btn_save.configure(command=lambda: self.save_appt())
        self.ui.btn_del.configure(command=lambda: self.delete_appt())
        self.ui.btn_patient.configure(command=lambda: self.on_btn_patient_click())
        
        self.ui.box_status.bind("<<ComboboxSelected>>", self.on_box_status_change)
        
        self.ui.ent_patient.bind("<FocusOut>", self.on_ent_patient_focus_out)
        self.ui.ent_patient.bind("<Return>", self.on_ent_patient_focus_out)
        #self.ui.ent_patient.bind("<Tab>", self.on_ent_patient_focus_out)
        self.ui.btn_student.configure(command=lambda: self.on_btn_student_click())
        self.ui.ent_student.bind("<FocusOut>", self.on_ent_student_focus_out)
        self.ui.ent_student.bind("<Return>", self.on_ent_student_focus_out)
        #self.ui.ent_student.bind("<Tab>", self.on_ent_student_focus_out)
        self.ui.btn_assistant.configure(command=lambda: self.on_btn_assistant_click())
        self.ui.ent_assistant.bind("<FocusOut>", self.on_ent_assistant_focus_out)
        self.ui.ent_assistant.bind("<Return>", self.on_ent_assistant_focus_out)
        #self.ui.ent_assistant.bind("<Tab>", self.on_ent_assistant_focus_out)
        self.ui.btn_teacher.configure(command=lambda: self.on_btn_teacher_click())
        self.ui.ent_teacher.bind("<FocusOut>", self.on_ent_teacher_focus_out)
        self.ui.ent_teacher.bind("<Return>", self.on_ent_teacher_focus_out)
        #self.ui.ent_teacher.bind("<Tab>", self.on_ent_teacher_focus_out)
        
        self.ui.btn_procadd.configure(command=lambda: self.on_btn_procadd_click())
        self.ui.tbl_1.bind("<Insert>", self.on_tbl_1_insert_key_pressed)
        self.ui.btn_procdel.configure(command=lambda: self.on_btn_procdel_click())
        self.ui.tbl_1.bind("<Delete>", self.on_tbl_1_del_key_pressed)
        
        if self.new == False:
            self.fill_data(data)
        else:
            self.ui.btn_del.configure(state='disable')
            self.ui.set_title(self.next_id)


    def fill_data(self, data):
        self.ui.set_title(data[0])
        self.apptid = data[0]

        appt = (Appointment
                .select()
                #.join(Patient)
                .where(Appointment.id==data[0])
                .get())
        
        self.ui.box_status.current(appt.status)
        self.ui.ent_patient.insert(0, appt.patient)
        var_age = date.today().year - appt.patient.birthdate.year
        var_patient = "{} ({} anos)".format(appt.patient.name,
                                            var_age)
        self.ui.lbl_patient.configure(text=var_patient)
        self.ui.date_appt.set_date(appt.apptdate)
        #self.ui.hour_appt.set(appt.appttime[:2])
        self.ui.hour_appt.set(appt.appttime.hour)
        #self.ui.min_appt.set(appt.appttime[3:-3])
        self.ui.min_appt.set(appt.appttime.minute)
        self.ui.lenh_appt.set(appt.apptlen.hour)
        self.ui.lenm_appt.set(appt.apptlen.minute)      
        self.ui.ent_student.insert(0, appt.student)
        self.ui.lbl_student.configure(text=appt.student.name)
        self.ui.ent_assistant.insert(0, appt.assistant)
        self.ui.lbl_assistant.configure(text=appt.assistant.name)
        self.ui.ent_teacher.insert(0, appt.teacher)
        self.ui.lbl_teacher.configure(text=appt.teacher.name)
        self.ui.tex_note1.insert(1.0, appt.note1)
        self.ui.tex_note2.insert(1.0, appt.note2)
        
        self.fill_tx(appt.id)
        self.fill_appt_patient(appt.patient)


    def add_row_treatment(self, rowvalues):
        self.ui.tbl_1.insert('','end',values=(rowvalues))


    def get_treatments(self, apptid):
        return Treatment.select().join(
            Course, on=(Course.id == Treatment.course)).join(
            TxType, on=(TxType.id == Treatment.txtype)).where(
            Treatment.appt==apptid)


    def fill_tx(self, apptid):
        tratamentos = self.get_treatments(apptid)
        for row in self.ui.tbl_1.get_children():
            self.ui.tbl_1.delete(row)
        for t in tratamentos:
            self.ui.tbl_1.insert('','end',
                                 values=(t.txtype, t.txtype.name,
                                         t.course, t.course.name,
                                         t.note1))


    def get_appointments(self, id_):
        return Appointment.select().where(
            Appointment.patient==id_)


    def fill_appt_patient(self, id_):
        appointments = self.get_appointments(id_)
        for row in self.ui.tbl_2.get_children():
            self.ui.tbl_2.delete(row)
        for item in appointments:
            self.ui.tbl_2.insert('','end',values=(item.apptdate,
                                                  item.appttime,
                                                  item.apptlen,
                                                  item.status))
        #self.ui.set_appttotal(len(appointments))


    def on_box_status_change(self, event) :
        if appt_status.index(self.ui.box_status.get()) == 3:
            self.ui.date_canceled.configure(state='enable')
        else:
            self.ui.date_canceled.configure(state='disable')


    # SAVE & DELETE
    def get_apptid(self):
        return int(self.apptid)


    def prepare_appt(self):
        var_patient = self.ui.ent_patient.get()
        if not var_patient:
            CMessages().showerror_emptyfield('Paciente deve ser selecionado')
            return

        var_student = self.ui.ent_student.get()
        if not var_student:
            CMessages().showerror_emptyfield('Aluno deve ser selecionado')
            return

        var_assistant = self.ui.ent_assistant.get()
        if not var_assistant:
            CMessages().showerror_emptyfield('Assistente deve ser selecionado')
            return

        var_teacher = self.ui.ent_teacher.get()
        if not var_teacher:
            CMessages().showerror_emptyfield('Professor deve ser selecionado')
            return
            
        var_timeappt = "{}:{}".format(self.ui.hour_appt.get(),
                                      self.ui.min_appt.get())
        var_lenappt = "{}:{}".format(self.ui.lenh_appt.get(),
                                      self.ui.lenm_appt.get())
        return {'id':self.get_apptid(),
		        'patient':int(var_patient),
		        'typeappt':1,
		        'apptdate':self.ui.date_appt.get_date(),
		        'appttime':var_timeappt,
		        'apptlen':var_lenappt,
			    'student':int(var_student),
				'assistant':int(var_assistant),
			    'teacher':int(var_teacher),
				'note1':self.ui.tex_note1.get('1.0','end-1c'),
				'note2':self.ui.tex_note2.get('1.0','end-1c'),
				'status':appt_status.index(self.ui.box_status.get()),
			    'created':'',
				'modified':'',
			    'canceled':''}


    def save_appt_db(self, data):
        try:
            Database().db.connect()
            if self.new == True:
                rows = Appointment.create(**data)
            else:
                query = Appointment.update(**data).where(
                           Appointment.id==data['id'])
                query.execute()
            Database().db.close()
        except pw.OperationalError as ex:
            print(ex.args)
            CMessages().showerror_database(ex.args)


    def save_appt(self):
        data = self.prepare_appt()
        if data:
            self.save_appt_db(data)
            self.save_treatments_db()
            self.ui.destroy()


    def delete_appt_db(self):
        try:
            Database().db.connect()
            p = Appointment.get(Appointment.id==self.get_apptid())
            p.delete_instance()
            Database().db.close()
        except pw.OperationalError as ex:
            CMessages().showerror_database(ex.args)


    def delete_appt(self):
        msg = "Deseja excluir consulta {} ?".format(self.get_apptid())
        res = CMessages().showquestion_del(msg)
        if res:
            self.delete_treatments_db(self.get_apptid())
            self.delete_appt_db()
            self.ui.destroy()


    def get_all_patients(self):
        return Patient.select()


    def get_all_students(self):
        return Student.select()


    def get_all_teachers(self):
        return Teacher.select()


    def get_patient_age(self, id_):
        try:
            birthdate = (Patient
                         .select(Patient.birthdate)
                         .where(Patient.id==id_).scalar())
            return date.today().year - birthdate.year
        except Patient.DoesNotExist:
            return 0
        except AttributeError:
            return 0


    # ENTRY ON FOCUS OUT
    def on_ent_patient_focus_out(self, key):
        try:
            id_ = self.ui.ent_patient.get()
            name = (Patient.select(Patient.name)
                           .where(Patient.id==int(id_))
                           .scalar())
        except pw.OperationalError as ex:
            print(ex.args)
            CMessages().showerror_database(ex.args)
        else:        
            if name:
                var_patient = "{} ({} anos)".format(name,
                                                    self.get_patient_age(id_))
                self.ui.lbl_patient.configure(text=var_patient)
                self.fill_appt_patient(id_)
            else:
                self.ui.ent_patient.delete(0, 'end')
                self.ui.lbl_patient.configure(text='')            


    def on_ent_student_focus_out(self, key):
        id_ = self.ui.ent_student.get()
        if id_:
            name = Student.select(Student.name).where(Student.id==id_).scalar()
            if name:
                self.ui.lbl_student.configure(text=name)
            else:
                self.ui.ent_student.delete(0, 'end')
                self.ui.lbl_student.configure(text='')


    def on_ent_assistant_focus_out(self, key):
        id_ = self.ui.ent_assistant.get()
        if id_:
            name = Student.select(Student.name).where(Student.id==id_).scalar()
            if name:
                self.ui.lbl_assistant.configure(text=name)
            else:
                self.ui.ent_assistant.delete(0, 'end')
                self.ui.lbl_assistant.configure(text='')


    def on_ent_teacher_focus_out(self, key):
        id_ = self.ui.ent_teacher.get()
        if id_:
            name = Teacher.select(Teacher.name).where(Teacher.id==id_).scalar()
            if name:
                self.ui.lbl_teacher.configure(text=name)
            else:
                self.ui.ent_teacher.delete(0, 'end')
                self.ui.lbl_teacher.configure(text='')		


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
    def callback_patient(self, item):
        self.ui.ent_patient.delete(0, 'end')
        self.ui.ent_patient.insert(0, item[0])
        var_patient = "{} ({} anos)".format(item[1],
                                            self.get_patient_age(item[0]))
        self.ui.lbl_patient.configure(text=var_patient)
        self.fill_appt_patient(item[0])


    def on_btn_patient_click(self):
        search = CSearch(self, self.get_all_patients(), self.callback_patient)
        self.show_search(search)


    def callback_student(self, item):
        self.ui.ent_student.delete(0, 'end')
        self.ui.ent_student.insert(0, item[0])
        self.ui.lbl_student.configure(text=item[1])


    def on_btn_student_click(self):
        search = CSearch(self, self.get_all_students(), self.callback_student)
        self.show_search(search)


    def callback_assistant(self, item):
        self.ui.ent_assistant.delete(0, 'end')
        self.ui.ent_assistant.insert(0, item[0])
        self.ui.lbl_assistant.configure(text=item[1])


    def on_btn_assistant_click(self):
        search = CSearch(self, self.get_all_students(), self.callback_assistant)
        self.show_search(search)


    def callback_teacher(self, item):
        self.ui.ent_teacher.delete(0, 'end')
        self.ui.ent_teacher.insert(0, item[0])
        self.ui.lbl_teacher.configure(text=item[1])


    def on_btn_teacher_click(self):
        search = CSearch(self, self.get_all_teachers(), self.callback_teacher)
        self.show_search(search)


    # Treatment
    def on_tb_proc_click(self, event):
        selectedItem = self.ui.tbl_1.selection()[0]
        item = self.ui.tbl_1.focus()
        data = self.ui.tbl_1.item(item, "values")
        self.top_tx(data)


    def on_btn_procadd_click(self):
        data = [0]
        self.top_tx(data)


    def on_tbl_1_insert_key_pressed(self, key):
        self.on_btn_procadd_click()


    def on_btn_procdel_click(self):
        selectedItem = self.ui.tbl_1.selection()[0]
        row = self.ui.tbl_1.focus()
        self.ui.tbl_1.delete(row)


    def on_tbl_1_del_key_pressed(self, key):
        self.on_btn_procdel_click()


    def top_tx(self, data):
        if not self.ontop:
            treatment = CTxEdit(self, data, self.add_row_treatment)
            top = treatment.ui
            top.bind('<Destroy>', self.on_top_destroy)
        self.ontop = True


    def prepare_tx(self, data):
        return {'id':int("{}{}{}".format(self.get_apptid(),data[2],data[0])),
		        'appt':self.get_apptid(),
		        'note1':data[4],
		        'txtype':data[2],
		        'course':data[0]}


    def save_treatments_db(self):
        self.delete_treatments_db(self.get_apptid())
        try:
            Database().db.connect()
            for row in self.ui.tbl_1.get_children():
                data = self.ui.tbl_1.item(row, "values")
                sttm = self.prepare_tx(data)
                rows = Treatment.create(**sttm)
            Database().db.close()
        except pw.OperationalError as ex:
            CMessages().showerror_database(ex.args)


    def delete_treatments_db(self, apptid):
        try:
            Database().db.connect()
            nrows = (Treatment
                     .delete()
                     .where(Treatment.appt==apptid)
                     .execute())        
            print('Delete treatments where appt is ({})'.format(apptid)) 
            Database().db.close()
        except pw.OperationalError:
            print("Não foi possível realizar a operação.")

