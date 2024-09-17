import tkinter as tk
from tkinter import ttk

from database import Database
import peewee as pw
from models import Course, TxType
from appt.txeditui import TxEditUi

class CTxEdit:
    def __init__(self, parent, data, callback):
        super().__init__()

        self.ui = TxEditUi() 
        self.data = data
        self.callback = callback
        self.disciplinas = []
        self.tipos_procedimentos = []
        
        self.new = False
        if self.data[0] == 0:
            self.new = True
            
        self.newAppt = False
			
        self.ui.btn_save.configure(command=lambda: self.return_row_values())
        self.fill_combo_disciplinas()
        self.fill_combo_procedimentos()
        
        if self.new == False:
            self.fill_data(data)


    def fill_combo_disciplinas(self):
        self.disciplinas = self.get_all_categories()
        self.ui.combo_disciplina.configure(values=[d.name for d in self.disciplinas])
        self.ui.combo_disciplina.configure(state='readonly')


    def get_all_categories(self):
        return Course.select()


    def fill_combo_procedimentos(self):
        self.tipos_procedimentos = self.get_all_proctypes()
        self.ui.combo_procedimento.configure(values=[p.name for p in self.tipos_procedimentos])
        self.ui.combo_procedimento.configure(state='readonly')


    def get_all_proctypes(self):
        return TxType.select()


    def fill_data(self, data):
        # 0  id
        # 1  category id
        # 2  category name
        # 3  proctype id
        # 4  proctype name
        # 5  obs 
        print(data)
        self.ui.entry_obs.insert(0, data[5])

        index = 0
        for d in self.disciplinas:
            if d.id == int(data[1]):
                self.ui.combo_disciplina.current(index)
                break
            index += 1
        
        index = 0
        for p in self.tipos_procedimentos:
            if p.id == int(data[3]):
                self.ui.combo_procedimento.current(index)
                break
            index += 1

 
    def return_row_values(self):
        d_index = self.ui.combo_disciplina.current()
        course_id = self.disciplinas[d_index].id
        tp_index = self.ui.combo_procedimento.current()
        txtype_id = self.tipos_procedimentos[tp_index].id
        
        row_value = [txtype_id, self.ui.combo_procedimento.get(),
                     course_id, self.ui.combo_disciplina.get(),
                     self.ui.entry_obs.get('1.0','end-1c')]
        self.callback(row_value)
        self.ui.destroy()
