import sqlite3
from tkinter import *
from mainlogin import connectdb
class empcontrol(connectdb):
    def __init__(self,w):
        self.conn = sqlite3.connect('test.db')
        self.objcontrol = w
        self.loadid()
    def loadid(self):
        cur = self.conn.cursor()
        result = cur.execute("select emp_id from employee")
        data = [] 
        for i in result:
            for d in i:
                data.append(d)
        self.objcontrol.Listbox1.delete(0,END)
        indexview = 1
        for i in data:
            self.objcontrol.Listbox1.insert(indexview,i)
            indexview+=1

    def onselect(self,e):
        try:
            w=e.widget
            index =int(w.curselection()[0])
            value = w.get(index)
            self.key = value
            result = self.loaddetail(self.key)
            self.settext(self.objcontrol.Entry1,result[0])
            self.settext(self.objcontrol.Entry2,result[1])
            self.settext(self.objcontrol.Entry3,result[2])
        except :
            pass
    def loaddetail(self,where):
        cur = self.conn.cursor()
        result = cur.execute("select * from employee where emp_id = ? ",(where,) )
        data = [] 
        for i in result:
            for d in i:
                data.append(d)
        return data
    def addemployee(self):
        cur = self.conn.cursor()
        cur.execute("insert into employee values('"+str(self.objcontrol.Entry1.get())+"','"+str(self.objcontrol.Entry2.get())+"','"+str(self.objcontrol.Entry3.get())+"')")
        self.conn.commit()
        self.loadid()
    def editemployee(self):
        cur = self.conn.cursor()
        cur.execute("update employee set emp_name ='"+str(self.objcontrol.Entry2.get())+"',emp_last = '"+str(self.objcontrol.Entry3.get())+"' where emp_id = '"+str(self.objcontrol.Entry1.get())+ "'")
        self.conn.commit()
        self.loadid()       
    def delemployee(self):
        cur = self.conn.cursor()
        cur.execute("delete from employee where emp_id = ? ",(self.key,))
        self.conn.commit()
        self.loadid()
    def settext(self,obj,text):
        try:
            obj.delete(0,END)
            obj.insert(0,text)
        except :
            pass
        
    
