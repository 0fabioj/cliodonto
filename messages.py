from tkinter import messagebox

class CMessages:
	
    def showerror_database(self, msg):
        messagebox.showerror("Erro de banco de dados", msg)


    def showquestion_del(self, msg):
        res = messagebox.askokcancel("Confirmacao de exclusao", msg)
        return res


    def showerror_emptyfield(self, msg):
        messagebox.showerror("Campo obrigatorio", msg)
