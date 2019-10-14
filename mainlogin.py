import sqlite3
from tkinter import *  
from tkinter import messagebox   
class connectdb:
    def __init__(self,namefile):
        self.conn = sqlite3.connect(namefile)
    def login(self,username,password):
        cur = self.conn.cursor()
        result = cur.execute("select count(*) from userinfo where username=? and password=?",(username,password))
        for i in result:
            for d in i:
                data = d
        return data
    def close(self):
        self.conn.close()
class controlmain:
    def __init__(self,obj):
        self.objcontrol  = obj
        self.conn  = connectdb('test.db')
    def login(self):
        username = self.objcontrol.Entry1.get()
        password = self.objcontrol.Entry2.get()
        result = self.conn.login(username,password)
        if result ==1:
            self.conn.close()
            from pageemployee import employee_support
            employee_support.start() 
        else :
            messagebox.showerror("error","not found user")
            
    def cleartextbox(self):
        self.settext(self.objcontrol.Entry1,"")
        self.settext(self.objcontrol.Entry2,"")
    def settext(self,obj,text):
        try:
            obj.delete(0,END)
            obj.insert(0,text)
        except :
            pass
    