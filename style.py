import tkinter as tk
from tkinter import ttk

background_color = '#D8E1E8'
#surface_color = '#C6D3E3'
surface_color = '#D8E1E8'
surface_color_40 = '98BAD8'
surface_color_70 = '#B2CBDE'
primary_color = '#304674'
secondary_color = '#DFC98A'
error_color = '#B00020'
on_background_color = '#000000'
on_surface_color = '#000000'
on_primary_color = '#FFFFFF'
on_secondary_color = '#000000'
on_error_color = '#FFFFFF'

class CStyle():
    def __init__(self):
        super().__init__()
        
        color_style = ttk.Style()
        color_style.theme_use('default')
        #clam alt default classic
        #flat raised sunken groove ridge solid

        color_style.configure('Toplevel', background=background_color)
        color_style.configure('TFrame', background=surface_color)
        color_style.configure('Transparent.TFrame', background=background_color)
        
        # Labelframe
        color_style.configure('TLabelframe'
                              ,background=surface_color
                              ,relief='flat')
        color_style.configure('TLabelframe.Label'
                              ,background=surface_color)
        
        #Toolbar
        color_style.configure('Toolbar.TFrame'
                              ,background=surface_color_70)
        
        color_style.configure('Title.TLabel', font=('Arial', 16)
                              ,background=primary_color
                              ,foreground=on_primary_color)

        #Statusbar
        color_style.configure('Statusbar.TFrame'
                              ,background=surface_color_70)
        
        color_style.configure('Error.TLabel'
                              ,background_color=error_color
                              ,foreground=on_error_color)


        # Treeview
        color_style.configure('Treeview', background=surface_color_70, fieldbackground=surface_color_70)
        color_style.configure('Treeview.Heading', background=secondary_color)
        color_style.map('Treeview.Heading', background=[('active',secondary_color)])
        

        color_style.configure('Horizontal.TScrollbar', troughcolor=surface_color)
        color_style.configure('TLabel', background=surface_color)
        color_style.configure('TCheckbutton', background=surface_color)
        color_style.configure('TButton', background=secondary_color )
        
        color_style.configure('TNotebook', background=surface_color)
        #color_style.configure('TNotebook', background=[('selected', '#dfc98a')])
        color_style.configure('TNotebook.Tab', background=surface_color)
        
        color_style.map('TEntry', fieldbackground=[('focus', secondary_color)])
        color_style.configure('Patient.TLabel', font='TkTextFont 9 bold')
        #from tkinter import font
        #print(font.nametofont('TkTextFont').actual())
        #{'family': 'Bitstream Vera Sans', 'size': 9, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}



