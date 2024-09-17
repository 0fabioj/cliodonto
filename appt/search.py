import tkinter as tk
from tkinter import ttk

from database import Database
import peewee as pw
from models import Patient, Student, Teacher
from appt.searchui import SearchUi

class CSearch:
    def __init__(self, parent, data, callback):
        super().__init__()

        self.ui = SearchUi() 
        self.data = data
        self.callback = callback
        self.fill_data(data)
        
        self.ui.tbl_1.bind("<ButtonRelease-1>", 
                            lambda event: self.return_row_values(event))


    def fill_data(self, data):
        for row in self.ui.tbl_1.get_children():
            self.ui.tbl_1.delete(row)
        for item in data:
            self.ui.tbl_1.insert('','end',
                                 values=(item.id, item.name))


    def return_row_values(self, event):
        selectedItem = self.ui.tbl_1.selection()[0]
        item = self.ui.tbl_1.focus()
        row_value = self.ui.tbl_1.item(item, "values")
        
        self.callback(row_value)
        self.ui.destroy()
