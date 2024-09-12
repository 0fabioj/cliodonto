import tkinter as tk
from tkinter import ttk

import peewee as pw
from database import Database
from models import TxType

from dictionary import *
from messages import CMessages
from txtype.txtypeeditui import TxTypeEditUi

class CTxTypeEdit:
    def __init__(self, parent, data):
        super().__init__()

        self.ui = TxTypeEditUi() 
        self.data = data
        
        self.new = False
        if self.data[0] == 0:
            self.new = True
			
        self.ui.btn_save.configure(command=lambda: self.save_txtype())
        self.ui.btn_del.configure(command=lambda: self.delete_txtype())

        if self.new == False:
            self.fill_data(data)
            self.ui.entry_id.configure(state='readonly')
        else:
            self.ui.entry_id.insert(0, self.get_nextid())
            self.ui.entry_id.configure(state='readonly')
            self.ui.btn_del.configure(state='disable')


    def get_nextid(self):
        return TxType.select(pw.fn.IFNULL(pw.fn.MAX(
                              TxType.id) + 1, 1)).scalar()
                                         
                                         
    def fill_data(self, data):
        self.ui.entry_id.insert(0, data[0])
        self.ui.entry_name.insert(0, data[1])
        self.ui.var_status.set(int(data[2]))


    def prepare_txtype(self):
        return {'id':int(self.ui.entry_id.get()),
		         'name':self.ui.entry_name.get(),
		         'status':self.ui.var_status.get()}
        

    def save_txtype_db(self, data):
        try:
            Database().db.connect()
            if self.new == True:
                rows = TxType.create(**data)
            else:
                query = TxType.update(**data).where(
                           TxType.id==data['id'])
                query.execute()
            Database().db.close()
        except pw.OperationalError as ex:
            print(ex.args)
            CMessages().showerror_database(ex.args)


    def save_txtype(self):
        data = self.prepare_txtype()
        self.save_txtype_db(data)
        self.ui.destroy()


    def delete_txtype_db(self):
        try:
            Database().db.connect()
            p = TxType.get(TxType.id==self.ui.entry_id.get())
            p.delete_instance()
            Database().db.close()
        except pw.IntegrityError as ex:
            CMessages().showerror_database(ex.args)


    def delete_txtype(self):
        res = CMessages().showquestion_del(
            "Deseja excluir tipo de tratamento?"
        )
        if res:
            self.delete_txtype_db()
            self.ui.destroy()
